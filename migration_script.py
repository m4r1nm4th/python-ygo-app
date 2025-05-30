import os
import json
import psycopg2

conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="localhost"
)
cursor = conn.cursor()

with open("ygoprodeck_database.json") as f:
    data = json.load(f)

for card in data["data"]:
    # Insert card
    cursor.execute("""
        INSERT INTO cards (id, name, type, human_readable_card_type, frame_type, description, race, archetype, ygoprodeck_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, (
        card["id"],
        card["name"],
        card.get("type"),
        card.get("humanReadableCardType"),
        card.get("frameType"),
        card.get("desc"),
        card.get("race"),
        card.get("archetype"),
        card.get("ygoprodeck_url")
    ))

    # Insert card_sets
    for cs in card.get("card_sets", []):
        cursor.execute("""
            INSERT INTO card_sets (card_id, set_name, set_code, set_rarity, set_rarity_code, set_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            card["id"],
            cs.get("set_name"),
            cs.get("set_code"),
            cs.get("set_rarity"),
            cs.get("set_rarity_code"),
            float(cs.get("set_price", 0))
        ))

    # Insert card_images
    for ci in card.get("card_images", []):
        cursor.execute("""
            INSERT INTO card_images (card_id, image_url, image_url_small, image_url_cropped)
            VALUES (%s, %s, %s, %s)
        """, (
            card["id"],
            ci.get("image_url"),
            ci.get("image_url_small"),
            ci.get("image_url_cropped")
        ))

    # Insert card_prices
    for cp in card.get("card_prices", []):
        cursor.execute("""
            INSERT INTO card_prices (card_id, cardmarket_price, tcgplayer_price, ebay_price, amazon_price, coolstuffinc_price)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            card["id"],
            float(cp.get("cardmarket_price", 0)),
            float(cp.get("tcgplayer_price", 0)),
            float(cp.get("ebay_price", 0)),
            float(cp.get("amazon_price", 0)),
            float(cp.get("coolstuffinc_price", 0))
        ))

conn.commit()
cursor.close()
conn.close()
