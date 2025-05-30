#!/usr/bin/env python3

import json
import sys


def card_name(card_id, path="ygoprodeck_database.json"):
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: File '{path}' is not valid JSON.")
        return

    for group in data.values():
        for card in group:
            if str(card.get("id")) == str(card_id):
                return str(card.get("name"))

    print(f"No card found with ID {card_id}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: card_name.py <card_id>")
        sys.exit(1)

    card_id = sys.argv[1]
    card_name(card_id)
