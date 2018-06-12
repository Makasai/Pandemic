"""
This file will contain definition of all used objects for "Pandemic"
"""
import abc
from random import shuffle
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_format)


class City:
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.neighbors = []
        self.players = []
        self.cubes = {"red": 0,
                      "blue": 0,
                      "yellow": 0,
                      "black": 0}
        self.research_center = False


class Player:
    def __init__(self, name):
        self.name = name
        self._location = "Georgia"
        self.hand = []
        self.actions = 0

        @property
        def location(self):
            return self._location

        @location.setter
        def location(self, city):
            self._location = city

        def action_factory(self, action_name):




        ## Movement ##
        def drive(self):
            pass

        def fly(self, card):
            # check card.name
            pass


        def cure(self):
            # You can only cure in the city you are at
            pass

        @classmethod
        def trade(cls, giver, receiver, card):
            """
            Card can be traded between players granted that:
            1) giver and receiver are at same location
            2) card being traded matches both players' location
            """
            pass

        def build_research(self, card):
            # check card.name == self._location
            print("Research Center built!")


        def use_event_card(self, card):
            # check card is an event
            # maybe I can check if it has a certain method?
            # event card will probably inherit from class Card
            pass


class Card:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def card_draw_effect(self):
        pass


class EventCard:
    """
    Each card will have a different ability...so...
    """
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def ability(self):
        """
        This method will execute event card's ability
        Abstract, so each event card will inherit from this class, and implement
        ability method

        Each event card is it's own class...that's the only way I know
        """
        print("This is an abstract method. Implement in child class")


class Fly(EventCard):

    def ability(self, city):
        """
        Consumes card to move player directly to city named on the card
        """
        print("you can fly directly to this city!")


class BuildResearch(EventCard):

    def ability(self, city):
        """
        Exactly the same as using a matching city card to build RC in the current player's current
        location
        """


class Epidemic(EventCard):

    def ability(self):
        """
        Triggers Epidemic mechanic
            1) draw bottom card of infection deck and place 3 infection cubes on that location, matching
            the city's color. If there are already cubes of the same color on the city -> outbreak
                i.e. if Mumbai is drawn, check if there are any cubes on that location already.
        """


class Deck:
    def __init__(self):
        self.deck = self.initial_deck_with_cities()

    @staticmethod
    def initial_deck_with_cities():
        """
        Builds new deck and shuffles it
        :return: Shuffled deck
        """
        deck = []
        red = ["Tokya", "Osaka", "Taipei"]
        blue = ["Atlanta", "Washington", "Montreal"]
        yellow = ["Miami", "Los Angeles", "Mexico City"]
        black = ["Cairo", "Delhi", "Kolkata"]
        for city_name in red:
            deck.append(Card(city_name, "RED"))
        for city_name in blue:
            deck.append(Card(city_name, "BLUE"))
        for city_name in yellow:
            deck.append(Card(city_name, "YELLOW"))
        for city_name in black:
            deck.append(Card(city_name, "BLACK"))
        shuffle(deck)

        return deck

    def draw_card(self):
        return self.deck.pop()

class InfectionDeck(Deck):
    def __init__(self):
        super().__init__()


class PlayerDeck(Deck):
    def __init__(self):
        super().__init__()


    @staticmethod
    def include_epidemic_cards():
        """
        Need to shuffle in the epidemic cards. Split deck (which includes cities+events
        into 4 piles. Add epidemic card and shuffle each. Concat lists together
        """
        pass
