"""
Author:     Chris Knowles
File:       joker.py
Version:    1.0.0
Notes:      Joker playing card class
"""
# Imports
from data_model.card import Card
from engine import gconsts


# Classes
class Joker(Card):
    """
    Specialised joker card class - class variables:
        none
    """
    def __init__(self, name):
        """
        Initialiser - instance variables:
            __value_name: from base class
            __suit_name: from base class

        :param name: name of this joker
        """
        super().__init__(name, "*")

    @property
    def value_symbol(self):
        # Joker symbol is regarded as its name
        return self.value_name

    @property
    def value(self):
        # Jokers have value one greater than an ace
        return len(gconsts.VALUE_NAMES) + 2

    @property
    def suit_symbol(self):
        # Symbol for a joker is the star symbol
        return "*"

    @property
    def suit(self):
        # Suit value for Joker is one greater than all other suits
        return len(gconsts.SUIT_NAMES) + 1

    @property
    def is_joker(self):
        # Joker cards return True
        return True
