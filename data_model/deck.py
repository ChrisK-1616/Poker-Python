"""
Author:     Chris Knowles
File:       deck.py
Version:    1.0.0
Notes:      Standard deck of playing cards class, notice that the deck has been implemented
            using numpy arrays as an exercise for adopting numpy instead of raw Python lists
"""
# Imports
import numpy as np
from engine import gconsts
from data_model.card import Card
from data_model.joker import Joker


# Classes
class Deck:
    """
    Standard deck of playing card class - class variables:
        none
    """
    def __init__(self, has_jokers=False):
        """
        Initialiser - instance variables:
            __ordered_cards: collection of ordered playing cards in the deck, property with read only access
            __shuffled_cards: collection of shuffled playing cards in the deck, property with read only access

        :param has_jokers: indicates whether to include jokers in this deck or not
        """
        self.__ordered_cards = np.array([])
        self.__shuffled_cards = np.array([])

        # Generate all card values for each card suit (including two jokers if required)
        for vname in gconsts.VALUE_NAMES:
            for sname in gconsts.SUIT_NAMES:
                self.__ordered_cards = np.append(self.__ordered_cards, [Card(vname, sname)])

        if has_jokers:
            self.__ordered_cards = np.append(self.__ordered_cards, [Joker(gconsts.JOKER_NAMES[0])])
            self.__ordered_cards = np.append(self.__ordered_cards, [Joker(gconsts.JOKER_NAMES[1])])

    @property
    def ordered_cards(self):
        return self.__ordered_cards

    @property
    def shuffled_cards(self):
        return self.__shuffled_cards

    @property
    def shuffled_cards_count(self):
        return len(self.__shuffled_cards)

    def shuffle(self):
        """
        Shuffles the ordered cards into a new shuffled array of cards

        :return nothing
        """
        self.__shuffled_cards = np.copy(self.__ordered_cards)
        np.random.shuffle(self.__shuffled_cards)

    def clear_shuffled(self):
        """
        Clears the shuffled cards to an empty array of cards

        :return nothing
        """
        self.__shuffled_cards = np.array([])

    def peek_shuffled_card(self):
        """
        Returns the first card from the shuffled array of cards without removing it from the shuffled cards

        :return first card in the shuffled card array, or None if no shuffled card array
        """
        if not len(self.shuffled_cards):
            return None

        return self.shuffled_cards[0]

    def pop_shuffled_card(self):
        """
        Returns the first card from the shuffled array of cards and removes it from the shuffled cards

        :return first card in the shuffled card list, or None if no shuffled card list
        """
        if not len(self.shuffled_cards):
            return None

        ret_card = self.__shuffled_cards[0]
        self.__shuffled_cards = np.delete(self.__shuffled_cards, 0)

        return ret_card

    def push_shuffled_card(self, card, append=True):
        """
        Pushes the supplied card onto the shuffled array of cards, either to the end or the front of this array
        depending on the value of the append flag

        :param card: card to push onto the shuffled array
        :param append: if True then the pushed card is appended to end of the shuffled cards array, otherwise
                       it is added to front of shuffled cards array

        :return nothing
        """
        if append:
            self.__shuffled_cards = np.append(self.__shuffled_cards, [card])
        else:
            self.__shuffled_cards = np.insert(self.__shuffled_cards, 0, [card])

    def return_hand(self, hand, append=True, shuffled=False):
        """
        Pushes all the cards from the supplied hand to the shuffled cards array, either to the end or the front
        of this array depending on the value of the append flag, the card is also popped from the supplied hand

        :param hand: hand from which to return cards
        :param append: if True then the pushed card is appended to end of the shuffled cards array, otherwise
                       it is added to front of shuffled cards array
        :param shuffled: if True then the supplied hand is shuffled before it is returned to the deck, otherwise
                         the hand is returned to the deck in the order it is currently at

        :return nothing
        """
        if shuffled:
            hand.shuffle()

        for _ in range(hand.size):
            self.push_shuffled_card(hand.pop_card(), append)

    def __str__(self):
        """
        To string method

        :return string representation of this deck of cards instance
        """
        oc = " ".join(map(str, self.ordered_cards))
        sc = " ".join(map(str, self.shuffled_cards))
        s = "\n[{0}]\n[{1}]".format(oc if not oc == "" else "No ordered cards",
                                    sc if not sc == "" else "No shuffled cards")

        return s
