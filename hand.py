from card import Card

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def numberStarter(self):
        result = 0 
        for card in self.cards:
            result = result + 1 if card.isStarter else result
        return result
    
    def numberNonEngine(self):
        result = 0 
        for card in self.cards:
            result = result if card.isEngine else result + 1
        return result
        
    def numberBricks(self):
        result = 0 
        for card in self.cards:
            result = result + 1 if card.isBrick else result
        return result

    def summary(self):
        numberStarter = 0
        numberNonEngine = 0
        numberBricks = 0
        for card in self.cards:
            numberBricks = numberBricks + 1 if card.isBrick else numberBricks
            numberNonEngine = numberNonEngine if card.isEngine else numberNonEngine + 1
            numberStarter = numberStarter + 1 if card.isStarter else numberStarter
        print(f"Non-Engines: {numberNonEngine}, Bricks: {numberBricks}, Starter: {numberStarter}")

    def __repr__(self):
        result = ""
        for card in self.cards:
            result = result + ", " + card.__repr__()
        return result