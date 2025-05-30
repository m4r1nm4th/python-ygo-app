from card import *
from hand import Hand
import random


class Deck:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def __repr__(self):
        result = ""
        for card in self.cards:
            result = result + ", " + card.__repr__()
        return result

    def drawHand(self):
        return Hand(random.sample(self.cards, 5))


def myDeck1():
    myDeck = Deck()
    smiger = EngineCard('Kristron Smiger')
    smiger.setStarter()
    myDeck.addCard(smiger)
    myDeck.addCard(smiger)
    myDeck.addCard(smiger)
    fuwalos = NonEngineCard('Mulcharmy Fuwalos')
    myDeck.addCard(fuwalos)
    myDeck.addCard(fuwalos)
    myDeck.addCard(fuwalos)
    ash = NonEngineCard('Ash Blossom')
    myDeck.addCard(ash)
    myDeck.addCard(ash)
    myDeck.addCard(ash)
    imperm = NonEngineCard('Infinite Impermanence')
    myDeck.addCard(imperm)
    myDeck.addCard(imperm)
    myDeck.addCard(imperm)
    droll = NonEngineCard('Droll and Lock Bird')
    myDeck.addCard(droll)
    myDeck.addCard(droll)
    myDeck.addCard(droll)
    droplet = NonEngineCard('Forbidden Droplet')
    myDeck.addCard(droplet)
    myDeck.addCard(droplet)
    myDeck.addCard(droplet)
    ttt = NonEngineCard('Triple Tactics Talent')
    myDeck.addCard(ttt)
    calledBy = NonEngineCard('Called By The Grave')
    myDeck.addCard(calledBy)
    foolish = EngineCard('Foolish Burial')
    foolish.setStarter()
    myDeck.addCard(foolish)
    inclusion = EngineCard('Kristron Inclusion')
    inclusion.setStarter()
    myDeck.addCard(inclusion)
    myDeck.addCard(inclusion)
    myDeck.addCard(inclusion)
    tristaros = EngineCard('Kristron Tristaros')
    tristaros.setStarter()
    myDeck.addCard(tristaros)
    myDeck.addCard(tristaros)
    myDeck.addCard(tristaros)
    citree = EngineCard('Kristron Citree')
    citree.setBrick()
    myDeck.addCard(citree)
    thystvern = EngineCard('Kristron Thystvern')
    thystvern.setBrick()
    myDeck.addCard(thystvern)
    cluster = EngineCard('Kristron Cluster ')
    cluster.setBrick()
    myDeck.addCard(cluster)
    sulfador = EngineCard('Kristron Sulfador')
    myDeck.addCard(sulfador)
    myDeck.addCard(sulfador)
    sulfefnir = EngineCard('Kristron Sulfefnir')
    myDeck.addCard(sulfefnir)
    myDeck.addCard(sulfefnir)
    myDeck.addCard(sulfefnir)
    tidal = EngineCard('Tidal, Dragon Ruler of Waterfalls')
    myDeck.addCard(tidal)
    myDeck.addCard(tidal)
    fenrir = EngineCard('Kashtira Fenrir')
    myDeck.addCard(fenrir)
    myDeck.addCard(fenrir)
    unicorn = EngineCard('Kashtira Unicorn')
    myDeck.addCard(unicorn)
    wraitsoth = EngineCard('Wraithsoth')
    myDeck.addCard(wraitsoth)
    myDeck.addCard(wraitsoth)
    birth = EngineCard('Kashtira Birth')
    myDeck.addCard(birth)
    return myDeck
