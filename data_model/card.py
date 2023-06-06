"""
Author:     Chris Knowles
File:       card.py
Version:    1.0.0
Notes:      Standard playing card class
"""
# Imports
from engine import gconsts


# Classes
class Card:
    """
    Standard playing card class - class variables:
        none
    """
    def __init__(self, value_name, suit_name):
        """
        Initialiser - instance variables:
            __value_name: value name of this instance, as string (from gconsts.VALUE_NAMES consts),
                          property with read only access
            __suit_name: suit name of this instance, as string (from gconsts.SUIT_NAMES consts),
                         property with read only access

        :param value_name: value name of this card
        :param suit_name: suit name of this card
        """
        self.__value_name = value_name
        self.__suit_name = suit_name

    @property
    def value_name(self):
        return self.__value_name

    @property
    def value_symbol(self):
        return gconsts.VALUE_SYMBOLS[gconsts.VALUE_NAMES.index(self.value_name)]

    @property
    def value(self):
        # Get value of the card from its index in the gconsts.VALUE_NAMES array plus one
        v = gconsts.VALUE_NAMES.index(self.value_name) + 1

        # Check if value is for an Ace, if so then set value to 14 (one greater than a King)
        if v == gconsts.ACE_LOW_VALUE:
            v = gconsts.ACE_HIGH_VALUE

        return v

    @property
    def suit_name(self):
        return self.__suit_name

    @property
    def suit_symbol(self):
        return gconsts.SUIT_SYMBOLS[gconsts.SUIT_NAMES.index(self.suit_name)]

    @property
    def suit(self):
        # Get suit value of the card from its index in the gconsts.SUIT_NAMES array
        return gconsts.SUIT_NAMES.index(self.suit_name)

    @property
    def is_joker(self):
        # Non-joker cards return False
        return False

    def value_delta(self, card):
        """
        Return the difference in value of the supplied card from the value of this card, a negative delta
        indicates that the supplied card is of a higher value than this card, a positive delta indicates
        that this card is of higher value and a delta of zero indicates that the two cards are of equal
        value

        :param card: card to calculate the value delta of from this card value

        :return value delta
        """
        return self.value - card.value

    def equal_values(self, card):
        """
        Return True if the value of the supplied card is equal to the value of this card, return False
        otherwise

        :param card: card to check value with this card's value

        :return True if values equal, False otherwise
        """
        return self.value == card.value

    def equal_suits(self, card):
        """
        Return True if the suit of the supplied card is equal to the suit of this card, return False
        otherwise

        :param card: card to check suit with this card's suit

        :return True if suits equal, False otherwise
        """
        return self.suit_name == card.suit_name

    def __str__(self):
        """
        To string method

        :return string representation of this card instance
        """
        return "{0}{1}".format(self.value_symbol, self.suit_symbol)
