import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cards=[]
        self.cards.append([Card("S",i) for i in range(1,14)])
        self.cards.append([Card("H",i) for i in range(1,14)])
        self.cards.append([Card("D",i) for i in range(1,14)])
        self.cards.append([Card("C",i) for i in range(1,14)])
        self.game=CardGame()
    
    def test_cards_have_attributes(self):
        self.assertEqual(self.cards[0][0].value,1)
        self.assertEqual(self.cards[0][0].suit,"S")
        self.assertEqual(self.cards[3][12].value,13)
        self.assertEqual(self.cards[3][12].suit,"C")
    
    def test_check_for_ace(self):
        self.assertTrue(self.game.check_for_ace(self.cards[0][0]))
        self.assertFalse(self.game.check_for_ace(self.cards[0][1]))
    
    def test_highest_card(self):
        self.assertEqual(self.game.highest_card(self.cards[0][0],self.cards[0][1]),self.cards[0][1])
        self.assertEqual(self.game.highest_card(self.cards[0][1],self.cards[0][0]),self.cards[0][1])
    
    def test_highest_suit(self):
        self.assertEqual(self.game.highest_card(self.cards[0][0],self.cards[1][0]),self.cards[0][1])
        self.assertEqual(self.game.highest_card(self.cards[1][0],self.cards[0][0]),self.cards[0][0])