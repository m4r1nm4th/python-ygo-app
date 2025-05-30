import psycopg2
import re

def load_deck_from_ydk(path_to_ydk, db_config):
    """
    Parses a YDK file into main, extra, and side decks,
    fetches card data for each unique card from the DB,
    then reconstructs decks preserving duplicates.
    
    Returns:
      {
        'main': [card_dict, card_dict, ...],  # with duplicates
        'extra': [...],
        'side': [...]
      }
    """
    
    deck_sections = {
        'main': [],
        'extra': [],
        'side': []
    }
    
    current_section = None
    
    with open(path_to_ydk) as f:
        for line in f:
            line = line.strip()
            if line == "#main":
                current_section = 'main'
            elif line == "#extra":
                current_section = 'extra'
            elif line == "!side":
                current_section = 'side'
            elif current_section and re.match(r'^\d{8}$', line):
                deck_sections[current_section].append(int(line))
    
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    
    # Get all unique card ids to fetch from DB
    unique_ids = set(deck_sections['main'] + deck_sections['extra'] + deck_sections['side'])
    
    if not unique_ids:
        cursor.close()
        conn.close()
        return {'main': [], 'extra': [], 'side': []}
    
    placeholders = ','.join(['%s'] * len(unique_ids))
    query = f"SELECT * FROM cards WHERE id IN ({placeholders})"
    cursor.execute(query, list(unique_ids))
    
    colnames = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    
    # Map card_id to card dict
    card_map = {row[colnames.index('id')]: dict(zip(colnames, row)) for row in rows}
    
    # Rebuild the decks with duplicates, using the card_map
    result = {}
    for section in ['main', 'extra', 'side']:
        result[section] = [card_map[card_id] for card_id in deck_sections[section]]
    
    cursor.close()
    conn.close()
    
    return result


# Example usage:
db_config = {
    'dbname': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword',
    'host': 'localhost'
}

deck_data = load_deck_from_ydk("Decks/Azamina_Kashtira_Crystron.ydk", db_config)
print("Main deck cards:")
for card in deck_data['main']:
    print(card['name'])

print("\nExtra deck cards:")
for card in deck_data['extra']:
    print(card['name'])

print("\nSide deck cards:")
for card in deck_data['side']:
    print(card['name'])

