import unittest
from Pandemic.python_files.Objects import *


class TestDeck(unittest.TestCase):
    """
    Test Cases for the deck
    """
    def test_shuffle_infection_deck(self):
        """
        Deck should be shuffled at initialization
        """
        infection_deck1 = InfectionDeck()
        infection_deck2 = InfectionDeck()
        infection_deck3 = InfectionDeck()
        infection_deck4 = InfectionDeck()
        self.assertFalse(infection_deck1
                             == infection_deck2
                             == infection_deck3
                             == infection_deck4)

    def test_shuffle_player_deck(self):
        player_deck1 = PlayerDeck()
        player_deck2 = PlayerDeck()
        player_deck3 = PlayerDeck()
        player_deck4 = PlayerDeck()
        self.assertFalse(player_deck1
                         == player_deck2
                         == player_deck3
                         == player_deck4)


class TestCardDrawEffects(unittest.TestCase):

    def setUp(self):
        self.deck = PlayerDeck()
        self.player = Player("medic")

    def test_draw__city_player_card(self):
        card = self.deck.draw_card()
        while card.name == "EPIDEMIC":
            card = self.deck.draw_card()
        if card.name != "EPIDEMIC":
            self.player.hand.append(card)

        print("This is the city_test", self.player.hand)
        cities_in_hand = [player_card.name for player_card in self.player.hand]
        self.assertTrue(card.name in cities_in_hand)

    def test_check(self):
        print("This is test_check")
        print(self.player.hand)


class TestPlayerAction(unittest.TestCase):

    def setUp(self):
        self.player = Player("medic")

    def test_0_action(self):
        self.player.acions = 0
        self.player.add_action(1)
        pass

    def test_1_action(self):
        self.player.acions = 1
        self.player.add_action(2)
        pass

    def test_2_action(self):
        self.player.acions = 2
        self.player.add_action(2)
        pass

    def test_3_action(self):
        self.player.acions = 3
        self.player.add_action(2)
        pass

    def test_4_action(self):
        self.player.acions = 4
        self.player.add_action(2)
        pass

    def test_5_action(self):
        self.player.acions = 5
        pass





if __name__ == "__main__":
    unittest.main()



