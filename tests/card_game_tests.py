import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cards=[]
        self.cards.append([Card("S",i) for i in range(1,13)])
        self.cards.append([Card("H",i) for i in range(1,13)])
        self.cards.append([Card("C",i) for i in range(1,13)])
        self.cards.append([Card("D",i) for i in range(1,13)])
        self.game=CardGame()