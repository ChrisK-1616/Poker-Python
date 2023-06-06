"""
Author:     Chris Knowles
File:       table.py
Version:    1.0.0
Notes:      Table class that holds the current set of active players and the current state of
            the poker game
"""
# Imports


# Classes
class Table:
    """
    Table class that pulls together current players, the dealer and the current poker round - class variables:
        none
    """
    def __init__(self, name, dealer=None, players=None):
        """
        Initialiser - instance variables:
            __name: name of this instance, as string, property with read only access
            __dealer: current dealer instance at this table, as Dealer class, property with read/write access
            __players: current list of player instances at this table, as list of Player class, property with
                       read only access, the order of the players in this array is important as it defines
                       the on the button sequence with the player at index 0 being the first player that is
                       on the button
            __on_the_button_player_index: player that is currently on the button, as integer index into the
                                          players array
            __current_player_index: player that is currently active, as integer index into the players array

        :param name: name of this table
        :param dealer: dealer at this table as Dealer class, defaults to None
        :param players: players at this table as list of Player class, defaults to empty list
        """
        self.__name = name

        self.__dealer = dealer
        if self.dealer:
            self.dealer.table = self

        self.__players = [] if not players else players
        for player in self.players:
            player.table = self

        self.__on_the_button_player_index = 0
        self.__current_player_index = 0

        # otb - sb - bb - utg - mp1 - mp2 - mp3 ... mpN - hj - co

    @property
    def name(self):
        return self.__name

    @property
    def dealer(self):
        return self.__dealer

    @dealer.setter
    def dealer(self, value):
        self.__dealer = value

    @property
    def players(self):
        return self.__players

    @property
    def on_the_button_player_index(self):
        return self.__on_the_button_player_index

    @property
    def current_player_index(self):
        return self.__current_player_index

    @property
    def player_count(self):
        return len(self.players)

    def get_player_by_index(self, index):
        """
        Returns the player held in the players array at the supplied index or returns
        None if the supplied index is out of range

        :param index: the index of the player instance to return from the players array

        :return player instance or None if out of range index supplied
        """
        # Check if players array is not empty and that the supplied index is in range of
        # the players array
        if self.players.count == 0 or index < 0 or index >= self.player_count:
            return None

        return self.players[index]

    def add_player(self, player):
        """
        Adds the supplied player onto this table, if the player is not duplicated by
        unique ident of player, if duplicated then player is not added

        :param player: player to add to this table

        :return nothing
        """
        # Check if player already in players, if so then abort
        if player in self.players:
            return

        self.__players.append(player)
        player.table = self

    def advance_button(self):
        """
        Calling this method advances the button to the player next in the players array
        with this cycling round once the last player in the array is currently on the
        button

        :return nothing
        """
        self.__on_the_button_player_index = (self.__on_the_button_player_index + 1) % self.player_count

    def __str__(self):
        """
        To string method

        :return string representation of this table instance
        """
        p = "\n\t".join(map(str, self.players))
        s = "{0}\nDealer: {1}\nPlayers:\n\t{2}".format(self.name,
                                                       self.dealer.name if self.dealer else "None",
                                                       p if not p == "" else "None")

        return s
