class Card:

    def __init__(self, name):
        self.name = name
        self.isBrick = False
        self.isStarter = False

    def __repr__(self):
        return self.name


class NonEngineCard(Card):

    def __init__(self, name):
        self.isEngine = False
        super().__init__(name)


class EngineCard(Card):

    def __init__(self, name):
        self.isEngine = True
        super().__init__(name)

    def setComboCards(self, cards):
        self.cards = cards

    def setBrick(self):
        self.isBrick = True

    def setStarter(self):
        self.isStarter = True
