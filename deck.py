from card import Card
from hand import Hand
from cardName import card_name
import random
import re
from load_db_card_info_from_ydk import load_deck_from_ydk as ldfy


class Deck:
    def __init__(self, main=[], extra=[], side=[]):
        self.main = main
        self.extra = extra
        self.side = side

    def add_card(self, card, section='main'):
        if section not in ('main', 'extra', 'side'):
            raise ValueError("section must be 'main', 'extra', or 'side'")
        getattr(self, section).append(card)

    def __repr__(self):
        def cards_str(cards):
            return "\n  " + "\n  ".join(repr(card) for card in cards) if cards else " (empty)"

        return (
            f"Deck:\n"
            f"Main:{cards_str(self.main)}\n"
            f"Extra:{cards_str(self.extra)}\n"
            f"Side:{cards_str(self.side)}"
        )

    def drawHand(self):
        return Hand(random.sample(self.main, 5))

def load_deck_from_ydk(path_to_ydk):
    db_config = {
        'dbname': 'mydatabase',
        'user': 'myuser',
        'password': 'mypassword',
        'host': 'localhost'
    }
    return Deck(**ldfy(path_to_ydk,db_config))


def myDeck1():
    return load_deck_from_ydk('Decks/Azamina_Kashtira_Crystron.ydk')
