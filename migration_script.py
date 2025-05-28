import os
import json
import psycopg2

# Database connection config
conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Path to your folder containing language subfolders
BASE_DIR = "./yugioh-card-history"

for language in os.listdir(BASE_DIR):
    lang_path = os.path.join(BASE_DIR, language)
    if not os.path.isdir(lang_path):
        continue

    for filename in os.listdir(lang_path):
        if filename.endswith(".json"):
            with open(os.path.join(lang_path, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                
                cursor.execute("""
                    INSERT INTO cards (
                        id, type, name, english_attribute, localized_attribute,
                        effect_text, level, atk, def, properties, language
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (id) DO NOTHING
                """, (
                    data.get("id"),
                    data.get("type"),
                    data.get("name"),
                    data.get("englishAttribute"),
                    data.get("localizedAttribute"),
                    data.get("effectText"),
                    data.get("level"),
                    data.get("atk"),
                    data.get("def"),
                    data.get("properties", []),
                    language
                ))

conn.commit()
cursor.close()
conn.close()
