"""
Author:     Chris Knowles
File:       hand.py
Version:    1.0.0
Notes:      A hand of standard playing cards class
"""
# Imports
from operator import attrgetter
from operator import itemgetter
from random import shuffle
from engine import gconsts
from data_model.hand_quality import HandQuality


# Classes
class Hand:
    """
    A hand of standard playing cards class - class variables:
        none
    """
    def __init__(self, max_size):
        """
        Initialiser - instance variables:
            __max_size: maximum number of cards in this hand, property with read only access
            __cards: collection of all playing cards currently in this hand, property with read only access
            __hole_cards: when this hand is part of a Texas Holdem style game, then these cards form the hole
            __quality: a HandQuality instance that holds details of the quality of the current hand, if None then
                       the quality of the hand has not yet been determined

        :param max_size: maximum number of cards in this hand
        """
        self.__max_size = max_size
        self.__cards = []
        self.__hole_cards = []
        self.__quality = None

    @property
    def max_size(self):
        return self.__max_size

    @property
    def cards(self):
        return self.__cards

    @property
    def hole_cards(self):
        return self.__hole_cards

    @property
    def quality(self):
        return self.__quality

    @property
    def size(self):
        # Return the current size of the hand
        return len(self.cards)

    def is_empty(self):
        """
        Returns True if hand is empty (ie. cards list is empty) or False otherwise

        :return True if hand is empty, False otherwise
        """
        return True if not self.cards else False

    def add_card(self, card, is_hole_card=False, sort=False):
        """
        Adds the supplied card into this hand, sorting if requested

        :param card: new card to add to this hand
        :param is_hole_card: this card is one of the hand's hole
        :param sort: if True then sort the card list as card is added, otherwise do not sort

        :return nothing
        """
        # Only allow a new card to be added if the hand size is less than max size, otherwise
        # abort
        if not len(self.cards) < self.max_size:
            return

        # Append added card
        self.__cards.append(card)

        # If this is a hole card then also add it to the hole
        if is_hole_card:
            self.__hole_cards.append(card)

        if sort:
            self.sort()

        # Make sure quality is redetermined if card is added
        self.determine_quality()

    def sort(self):
        """
        Sort the card list in place using the value of the cards, smaller value cards are at front of
        the list

        :return nothing
        """
        self.__cards.sort(key=attrgetter("value"))

    def shuffle(self):
        """
        Shuffle the card list in place

        :return nothing
        """
        shuffle(self.__cards)

    def find_card_with(self, value_symbol, suit_symbol):
        """
        Finds the card in this hand that has the supplied value and the supplied suit, if it exists then
        return this card, otherwise return None

        :param value_symbol: symbol of the value associated with the card to remove from this hand
        :param suit_symbol: symbol of the suit associated with the card to remove from this hand

        :return card if successfully found, None otherwise
        """
        # Get card with supplied value and suit symbols from the hand
        card = [c for c in self.cards if (c.value_symbol == value_symbol) and (c.suit_symbol == suit_symbol)]

        return None if not card else card[0]

    def is_hole_card(self, card):
        """
        Is the supplied card in the hand's hole

        :param card: card to check if is in the hand's hole

        :return True if is hole card, False otherwise
        """
        card = [c for c in self.hole_cards if (c.value_symbol == card.value_symbol) and
                (c.suit_symbol == card.suit_symbol)]

        return False if not card else True

    def peek_card(self):
        """
        Returns the card at the front of the hand without removing it from the hand

        :return card found at the front of the hand, or None if current hand is empty
        """
        # Check if hand is currently empty
        if self.is_empty():
            return None

        return self.cards[0]

    def pop_card(self):
        """
        Returns the card at the front of the hand and then removes it from the hand

        :return card found at the front of the hand, or None if current hand is empty
        """
        # Check if hand is currently empty
        if self.is_empty():
            return None

        card = self.__cards.pop(0)

        # If card is in the hand's hole then also remove from the hole
        if self.is_hole_card(card):
            self.hole_cards.remove(card)

        # Make sure quality is redetermined if card is popped
        self.determine_quality()

        return card

    def peek_card_at(self, index):
        """
        Returns the card at supplied index from this hand without removing it from the hand

        :param index: zero-based index of the card to pop from the hand, if this is outside the bounds of the
                      current hand size the operation fails and returns None

        :return card found at supplied index from the hand, or None if supplied index is outside bounds of the
                current hand
        """
        # Outside the bounds of the current hand
        if index < 0 or index >= self.size:
            return None

        return self.cards[index]

    def pop_card_at(self, index):
        """
        Returns the card at supplied index from this hand and then removes it from the hand

        :param index: zero-based index of the card to pop from the hand, if this is outside the bounds of the
                      current hand size the operation fails and returns None

        :return card found at supplied index from the hand, or None if supplied index is outside bounds of the
                current hand
        """
        # Outside the bounds of the current hand
        if index < 0 or index >= self.size:
            return None

        card = self.__cards.pop(index)

        # If card is in the hand's hole then also remove from the hole
        if self.is_hole_card(card):
            self.hole_cards.remove(card)

        # Make sure quality is redetermined if card is popped
        self.determine_quality()

        return card

    def remove_card(self, card):
        """
        Removes the supplied card from this hand (if it exists)

        :param card: card to remove from this hand

        :return nothing
        """
        # If hand is empty then immediately return
        if self.is_empty():
            return

        self.__cards.remove(card)

        # If card is in the hand's hole then also remove from the hole
        if self.is_hole_card(card):
            self.hole_cards.remove(card)

        # Make sure quality is redetermined if card is removed
        self.determine_quality()

    def remove_card_with(self, value_symbol, suit_symbol):
        """
        Removes the card from this hand that has the supplied value and the supplied suit (if it exists)

        :param value_symbol: symbol of the value associated with the card to remove from this hand
        :param suit_symbol: symbol of the suit associated with the card to remove from this hand

        :return True if successfully removed, False otherwise
        """
        # Find card with supplied value and suit symbol
        card = self.find_card_with(value_symbol, suit_symbol)

        if not card:
            return False

        self.remove_card(card)

        # If card is in the hand's hole then also remove from the hole
        if self.is_hole_card(card):
            self.hole_cards.remove(card)

        return True

    def clear(self):
        """
        Clears the hand to have no cards, including hole cards

        :return nothing
        """
        self.__cards = []
        self.__hole_cards = []

        # Make sure quality is redetermined if hand is cleared
        self.determine_quality()

    def determine_quality(self):
        """
        Using Poker rules, determine the quality of the current hand, the various quality measures are to be
        found in the gconsts.HAND_QUALITIES const, the finalised determined quality of the hand is stored
        in the self.__quality property of this hand

        :return nothing
        """
        # If hand is empty then the quality is set as None
        if self.is_empty():
            self.__quality = None

        # Make sure the hand is sorted
        self.sort()

        # Get the duplicated card values as these are likely to be used and then only done once
        all_values = {}

        for card in self.cards:
            try:
                all_values[card.value] += 1
            except KeyError:
                all_values[card.value] = 1

        duplicated_values = sorted({k: v for k, v in all_values.items() if v > 1}.items(),
                                   key=itemgetter(1), reverse=True)

        # Check for flush
        #   - Check for royal flush
        #   - Check for straight flush
        all_suits = {}

        for card in self.cards:
            try:
                all_suits[card.suit_symbol] += 1
            except KeyError:
                all_suits[card.suit_symbol] = 1

        duplicated_suit = tuple({k: v for k, v in all_suits.items() if v > 4})

        if duplicated_suit:
            flush_cards = [c for c in self.cards if c.suit_symbol == duplicated_suit[0]]

            lcv, tcv = self.__check_for_straight(flush_cards)
            if tcv:
                if tcv == gconsts.ACE_HIGH_VALUE:
                    self.__quality = HandQuality(value=gconsts.ROYAL_FLUSH_QUALITY_VALUE,
                                                 suit=flush_cards[0].suit)
                    return
                else:
                    self.__quality = HandQuality(value=gconsts.STRAIGHT_FLUSH_QUALITY_VALUE, low_card_value=lcv,
                                                 top_card_value=tcv, suit=flush_cards[0].suit)
                    return
            else:
                if duplicated_values:
                    # Check for:
                    #   - Quads
                    #   - Full house
                    if self.__check_for_quads(duplicated_values):
                        return

                    if self.__check_for_full_house(duplicated_values):
                        return

                self.__quality = HandQuality(value=gconsts.FLUSH_QUALITY_VALUE,
                                             top_card_value=flush_cards[-1].value, suit=flush_cards[-1].suit)
                return
        else:
            if duplicated_values:
                # Check for:
                #   - Quads
                #   - Full house
                if self.__check_for_quads(duplicated_values):
                    return

                if self.__check_for_full_house(duplicated_values):
                    return
            lcv, tcv = self.__check_for_straight(self.cards)
            if tcv:
                self.__quality = HandQuality(value=gconsts.STRAIGHT_QUALITY_VALUE, top_card_value=tcv,
                                             low_card_value=lcv)
                return
            else:
                if duplicated_values:
                    # Check for:
                    #   - Trips
                    #   - Two pairs
                    #   - Pair
                    if self.__check_for_trips(duplicated_values):
                        return

                    if self.__check_for_two_pairs(duplicated_values):
                        return

                    # Must be a pair, so record this
                    self.__check_for_pair(duplicated_values)
                    return

                # Must be only high cards, only record the top five of these (only five cards in a valid hand)
                hcv = sorted([c.value for c in self.cards], reverse=True)
                self.__quality = HandQuality(value=gconsts.HIGH_CARD_QUALITY_VALUE,
                                             top_card_value=hcv[0], high_card_values=hcv[1:5])

    @staticmethod
    def __check_for_straight(cards):
        """
        Check to see if the supplied cards contain a straight and if they do then return the lowest and highest
        cards of that straight, note there is a special case of A,2,3,4,5 as ace is usually high but in the
        situation where there is no T,J,Q,K,A there could still be a low ace through 5 straight

        :param cards: list of cards to check for a straight

        :return tuple with first element the lowest card value in the straight and second element the highest
                card value in the straight, if no straight is found then return 0 as both elements
        """
        lcv = 0
        tcv = 0

        # Consolidate the card values to remove any duplicated values, for instance if 2,2,3,4,5,6,T is provided
        # then needs to only check 2,3,4,5,6,T (ie. remove the duplicated 2 value card) and sort them ascending
        card_values = sorted(list(set([c.value for c in cards])))

        if len(card_values) < 5:  # Not enough cards for a straight, must be at least 5 cards in a straight
            return lcv, tcv

        for i in range(len(card_values) - 4):
            if card_values[i + 4] == card_values[i] + 4:
                lcv = card_values[i]
                tcv = card_values[i + 4]

        if not lcv:  # Not a yet a straight but check for A,2,3,4,5
            if card_values[0] == 2:
                if card_values[3] == 5:
                    if card_values[-1] == gconsts.ACE_HIGH_VALUE:  # Yes this is a A,2,3,4,5 straight
                        lcv = gconsts.ACE_LOW_VALUE  # In this case ace is of value 1
                        tcv = card_values[3]

        return lcv, tcv

    def __check_for_quads(self, card_dups):
        """
        Check if the current hand has quads, if so then record this in the hand quality
        property and return True

        :param card_dups: list of identified card duplicates from which to check for quads

        :return True if quads, False otherwise
        """
        if card_dups[0][1] == 4:
            self.__quality = HandQuality(value=gconsts.QUADS_QUALITY_VALUE, top_card_value=card_dups[0][0])
            return True

        return False

    def __check_for_full_house(self, card_dups):
        """
        Check if the current hand is a full house, if so then record this in the hand quality property
        and return True

        :param card_dups: list of identified card duplicates from which to check for a full house

        :return True if is full house, False otherwise
        """
        # Get all trips card values
        trips= sorted([c[0] for c in card_dups if c[1] == 3], reverse=True)

        # Get all pair card values
        pair = sorted([c[0] for c in card_dups if c[1] == 2], reverse=True)

        # If there are at least 1 trips card value then potential full house
        if len(trips):
            # Highest trips card value must be the high card value of any full house
            tcv = trips[0]

            # If more than one trips then check against the highest pair card value (if present)
            if len(trips) > 1:
                if len(pair) and pair[0] > trips[1]:
                    lcv = pair[0]
                else:
                    lcv = trips[1]
            else:  # Check to see if there are any pairs, if so then there is a full house
                if len(pair):
                    lcv = pair[0]
                else:  # No pairs so not a full house
                    return False

            self.__quality = HandQuality(value=gconsts.FULL_HOUSE_QUALITY_VALUE, top_card_value=tcv,
                                         low_card_value=lcv)
            return True

        return False

    def __check_for_trips(self, card_dups):
        """
        Check if the current hand has trips, if so then record this in the hand quality
        property and return True

        :param card_dups: list of identified card duplicates from which to check for trips

        :return True if trips, False otherwise
        """
        if card_dups[0][1] == 3:
            self.__quality = HandQuality(value=gconsts.TRIPS_QUALITY_VALUE, top_card_value=card_dups[0][0])
            return True

        return False

    def __check_for_two_pairs(self, card_dups):
        """
        Check if the current hand has two pairs, if so then record this in the hand quality property,
        set the remaining high cards (in event of tied two pairs hands) and then return True

        :param card_dups: list of identified card duplicates from which to check for two pairs

        :return True if is two pairs, False otherwise
        """
        if card_dups[0][1] == 2 and len(card_dups) > 1:
            cdv = sorted([c[0] for c in card_dups], reverse=True)
            cv = set(c.value for c in self.cards)
            cv = cv.difference(set(cdv))
            cv = sorted(list(cv), reverse=True)
            self.__quality = HandQuality(value=gconsts.TWO_PAIRS_QUALITY_VALUE, high_card_values=cv[:1],
                                         top_card_value=cdv[0], low_card_value=cdv[1])
            return True

        return False

    def __check_for_pair(self, card_dups):
        """
        Check if the current hand is a pair, if so then record this in the hand quality property,
        set the remaining high cards (in event of tied pair hands) and then return True

        :param card_dups: list of identified card duplicates from which to check for a pair

        :return True if is a pair, False otherwise
        """
        if card_dups[0][1] == 2 and len(card_dups) == 1:
            cv = set(c.value for c in self.cards)
            cv = cv.difference(set([c[0] for c in card_dups]))
            cv = sorted(list(cv), reverse=True)
            self.__quality = HandQuality(value=gconsts.PAIR_QUALITY_VALUE, high_card_values=cv[:3],
                                         top_card_value=card_dups[0][0])
            return True

        return False

    def compare_hands(self, other_hand):
        """
        Check if this hand wins over a supplied hand, if so return 1 otherwise return -1 if the other
        hand wins and return 0 if the two hands tie

        :param other_hand: other hand to check against quality of this hand to determine if it wins,
                           loses or ties
        :return 1 if this hand wins over the other hand, otherwise -1 if the other hand wins or 0 in
                event of a tie
        """
        thv = self.quality.value if self.quality else -1
        ohv = other_hand.quality.value if other_hand.quality else -1

        if thv < 0 and ohv < 0:
            # Both hands are empty so assume a tie
            return gconsts.HAND_TIES

        if thv > ohv:
            # The quality of this hand is greater than the supplied other hand quality, so this hand
            # wins
            return gconsts.HAND_WINS

        if thv == ohv:
            # The quality of this hand and the supplied other hand quality are tied, so now check for
            # additional qualities of the hands
            if self.quality.top_card_value > other_hand.quality.top_card_value:
                # On second check this hand is of greater quality than other hand, so it wins
                return gconsts.HAND_WINS

            if self.quality.top_card_value < other_hand.quality.top_card_value:
                # On second check other hand is of greater quality than this hand, so it wins
                return gconsts.HAND_LOSE

            if self.quality.value_name == "TwoPairs":
                    if self.quality.top_card_value == other_hand.quality.top_card_value:
                        # If tied after second check then do a third check if checking two pairs
                        if self.quality.low_card_value > other_hand.quality.low_card_value:
                            return gconsts.HAND_WINS

                        if self.quality.low_card_value < other_hand.quality.low_card_value:
                            return gconsts.HAND_LOSE

            for i in range(len(self.quality.high_card_values)):
                # Check against high card values for each hand to try and break the tie
                if self.quality.high_card_values[i] > other_hand.quality.high_card_values[i]:
                    return gconsts.HAND_WINS

                if self.quality.high_card_values[i] < other_hand.quality.high_card_values[i]:
                    return gconsts.HAND_LOSE

            # Cannot break the tie so return 0 (to indicate a tie)
            return gconsts.HAND_TIES

        # Other hand definitely wins
        return gconsts.HAND_LOSE

    def __str__(self):
        """
        To string method

        :return string representation of this hand of cards instance
        """
        c = " ".join(map(str, self.cards))
        hc = " ".join(map(str, self.hole_cards))
        s = "({0}:{1}):[{2}]:[{3}]".format(self.size, self.max_size,
                                           hc if not hc == "" else "Empty hole",
                                           c if not c == "" else "No cards")

        return s
