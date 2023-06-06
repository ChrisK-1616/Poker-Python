"""
Author:     Chris Knowles
File:       dealer.py
Version:    1.0.0
Notes:      Dealer class utilised for dealing poker hands
"""
# Imports
import uuid
from data_model.deck import Deck
from engine.exceptions import InsufficientCardsError


# Classes
class Dealer:
    """
    Dealer class utilised for dealing poker hands - class variables:
        none
    """
    def __init__(self, name):
        """
        Initialiser - instance variables:
            __ident: unique identifier of this dealer, as random UUID from uuid package, property
                     with read only access
            __name: name of this instance, as string, property with read/write access
            __table: table dealer is working at
            __deck: deck of cards managed by this dealer

        :param name: name of this dealer
        """
        self.__ident = uuid.uuid4()
        self.__name = name
        self.__table = None
        self.__deck = Deck()
        self.deck.shuffle()

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
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        self.__table = value

    @property
    def deck(self):
        return self.__deck

    def deal_to_players(self, count=1):
        """
        Deal a number of cards (default 1 card) from the dealer's shuffled card deck
        into the hand of all players currently playing at the dealer's table
        Note: the cards are dealt one at a time by alternating each player for each
        dealt card in a round robin fashion, the first player to receive a card is
        the player after the player that is currently on the button and    then the
        rotation is continued until all players have received counts-worth of cards,
        this will only be possible if there are a suitable number of cards remaining
        in the dealer's    shuffled card deck, if the dealer's shuffled card deck does
        not have enough    cards then throw an InsufficientCardsError exception

        :param count: number of cards to deal into each player's hand

        :return nothing

        :exception InsufficientCardsError: thrown when there are not enough cards in dealer's
                                           shuffled card deck to satisfy the number of cards
                                           required to deal to each player
        """
        if self.deck.shuffled_cards_count < self.table.player_count * count:
            msg_str = "Not enough cards in dealer's shuffled deck: available={0} required={1}"
            msg = msg_str.format(self.deck.shuffled_cards_count, self.table.player_count * count)
            raise InsufficientCardsError(msg)

        for _ in range(count):
            for i in range (self.table.player_count):
                player_index = (self.table.on_the_button_player_index + i + 1) % self.table.player_count
                self.deal_to_player(player=self.table.get_player_by_index(player_index))

    def deal_to_player(self, player, count=1):
        """
        Deal a number of cards (default 1 card) into a supplied player's hand, this will
        only work if there are a suitably number of cards remaining in the dealer's
        shuffled card deck, if the dealer's shuffled card deck does not have enough    cards
        then throw an InsufficientCardsError exception

        :param player: player to receive card(s) into their hand
        :param count: number of cards to deal into the player's hand

        :return nothing

        :exception InsufficientCardsError: thrown when there are not enough cards in dealer's
                                           shuffled card deck to satisfy the number of cards
                                           required to deal to this player
        """
        if self.deck.shuffled_cards_count < count:
            msg_str = "Not enough cards in dealer's shuffled deck: available={0} required={1}"
            msg = msg_str.format(self.deck.shuffled_cards_count, count)
            raise InsufficientCardsError(msg)

        for _ in range(count):
            player.receive_card(self.deck.pop_shuffled_card())

    def deal_to_table(self, count=1):
        """
        Deal a number of cards (default 1 card) to the table the dealer is working at,
        this will only work if there are a suitably number of cards remaining in the
        dealer's shuffled card deck, if the dealer's shuffled card deck does not have
        enough cards then throw an InsufficientCardsError exception

        :param count: number of cards to deal to the dealer's table

        :return nothing

        :exception InsufficientCardsError: thrown when there are not enough cards in dealer's
                                           shuffled card deck to satisfy the number of cards
                                           required to deal to the dealer's table
        """
        if self.deck.shuffled_cards_count < count:
            msg_str = "Not enough cards in dealer's shuffled deck: available={0} required={1}"
            msg = msg_str.format(self.deck.shuffled_cards_count, count)
            raise InsufficientCardsError(msg)

    def __eq__(self, other):
        """
        Equal To method, check that this and other instance are same class and that the
        ident properties are equal

        :return True if this instance and other instance are equal
        """
        return self.__class__ == other.__class__ and self.ident == other.ident

    def __str__(self):
        """
        To string method

        :return string representation of this dealer instance
        """
        return "{0}:{1}:{2}".format(self.name, str(self.ident),
                                    self.table.name if self.table else "Not working")
