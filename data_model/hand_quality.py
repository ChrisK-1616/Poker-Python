"""
Author:     Chris Knowles
File:       hand_quality.py
Version:    1.0.0
Notes:      Representation of a poker hand's quality and data associated with that quality
"""
# Imports
from engine import gconsts


# Classes
class HandQuality:
    """
    Holds details of the quality of a hand - class variables:
        none
    """
    def __init__(self, value, top_card_value=0, low_card_value=0, high_card_values=None, suit=-1):
        """
        Initialiser - instance variables:
            __value: index value of the quality as taken from gconsts.HAND_QUALITIES
            __top_card_value: the top card value for straight, full house and two pairs hand qualities
            __low_card_value: the low card value for straight, full house and two pairs hand qualities
            __high_card_values: list of card values to refer to when qualities of compared hands are
                                equal, only relevant for two pairs, pair and high card quality hands
            __suit: index value of card suit for royal flush, straight flush and flush quality hands

        :param value: value of the hand quality
        :param top_card_value: top card value associated with the hand quality
        :param low_card_value: low card value associated with the hand quality (when needed)
        :param high_card_values: list of high card values associated with the hand quality (when needed)
        :param suit: suit associated with the hand quality (when needed), if not needed value is -1
        """
        self.__value = value
        self.__top_card_value = top_card_value
        self.__low_card_value = low_card_value
        self.__high_card_values = high_card_values if high_card_values else []
        self.__suit = suit

    @property
    def value(self):
        return self.__value

    @property
    def value_name(self):
        return gconsts.HAND_QUALITIES[self.value]

    @property
    def top_card_value(self):
        return self.__top_card_value

    @property
    def top_card_value_symbol(self):
        if self.top_card_value:
            return gconsts.VALUE_SYMBOLS[(self.top_card_value - 1) % len(gconsts.VALUE_SYMBOLS)]

        return None

    @property
    def top_card_value_name(self):
        if self.top_card_value:
            return gconsts.VALUE_NAMES[(self.top_card_value - 1) % len(gconsts.VALUE_NAMES)]

        return None

    @property
    def low_card_value(self):
        return self.__low_card_value

    @property
    def low_card_value_symbol(self):
        if self.low_card_value:
            return gconsts.VALUE_SYMBOLS[(self.low_card_value - 1) % len(gconsts.VALUE_SYMBOLS)]

        return None

    @property
    def low_card_value_name(self):
        if self.low_card_value:
            return gconsts.VALUE_NAMES[(self.low_card_value - 1) % len(gconsts.VALUE_NAMES)]

        return None

    @property
    def high_card_values(self):
        return self.__high_card_values

    @property
    def suit(self):
        return self.__suit

    @property
    def suit_symbol(self):
        if not self.suit == -1:
            return gconsts.SUIT_SYMBOLS[self.suit]

        return None

    @property
    def suit_name(self):
        if not self.suit == -1:
            return gconsts.SUIT_NAMES[self.suit]

        return None

    def __str__(self):
        """
        To string method

        :return string representation of this hand quality instance
        """
        s = "{0}:{1}:{2}:{3}:{4}:{5}".format(self.value, self.value_name, self.top_card_value_name,
                                             self.low_card_value_name, self.high_card_values, self.suit_name)

        return s
