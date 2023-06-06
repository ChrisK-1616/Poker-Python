"""
Author:     Chris Knowles
File:       player.py
Version:    1.0.0
Notes:      Poker game player class
"""
# Imports
import uuid
from data_model.hand import Hand


# Classes
class Player:
    """
    Poker game player class - class variables:
        nothing
    """
    def __init__(self, name, funds, max_hand_size=7):
        """
        Initialiser - instance variables:
            __ident: unique identifier of this player, as random UUID from uuid package, property
                     with read only access
            __name: name of this player, as string, property with read/write access
            __funds: current funds available for the player to use for betting, as integer, property
                     with read/write access
            __hand: current hand of cards held by this player
            __table: table player is playing at

        :param name: name of this player
        :param funds: initial funds available for the player to use for betting
        :param max_hand_size: maximum size of any hand held by this player
        """
        self.__ident = uuid.uuid4()
        self.__name = name
        self.__funds = funds
        self.__hand = Hand(max_hand_size)
        self.__table = None

    @property
    def ident(self):
        return self.__ident

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def funds(self):
        return self.__funds

    @funds.setter
    def funds(self, value):
        self.__funds = value

    @property
    def hand(self):
        return self.__hand

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        self.__table = value

    def clear_hand(self):
        """
        Clears the current hand to None

        :return nothing
        """
        self.__hand = None

    def receive_card(self, card, is_hole_card=False):
        """
        Receive a card to add to the current hand

        :param card: card to add to the current hand
        :param is_hole_card: this card is one of the hand's hole

        :return nothing
        """
        self.hand.add_card(card, is_hole_card)

    def __eq__(self, other):
        """
        Equal To method, check that this and other instance are same class and that the
        ident properties are equal

        :return: True if this instance and other instance are equal
        """
        return self.__class__ == other.__class__ and self.ident == other.ident

    def __str__(self):
        """
        To string method

        :return: string representation of this player instance
        """
        return "{0}:{1}:{2}:{3}:{4}".format(self.name, str(self.ident), self.funds,
                                            self.hand, self.table.name if self.table else "Not playing")
