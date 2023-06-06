"""
Author:     Chris Knowles
File:       gconsts.py
Version:    1.0.0
Notes:      global constants for small poker game
"""
# Global consts
VALUE_SYMBOLS = "A23456789TJQK"
VALUE_NAMES = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
               "Jack", "Queen", "King")
SUIT_SYMBOLS = "♠♥♣♦"
SUIT_NAMES = ("Spade", "Heart", "Club", "Diamond")
HAND_QUALITIES = ("High", "Pair", "TwoPairs", "Trips", "Straight", "Flush", "FullHouse",
                  "Quads", "StraightFlush", "RoyalFlush")
HIGH_CARD_QUALITY_VALUE = 0
PAIR_QUALITY_VALUE = 1
TWO_PAIRS_QUALITY_VALUE = 2
TRIPS_QUALITY_VALUE = 3
STRAIGHT_QUALITY_VALUE = 4
FLUSH_QUALITY_VALUE = 5
FULL_HOUSE_QUALITY_VALUE = 6
QUADS_QUALITY_VALUE = 7
STRAIGHT_FLUSH_QUALITY_VALUE = 8
ROYAL_FLUSH_QUALITY_VALUE = 9
ACE_LOW_VALUE = 1
ACE_HIGH_VALUE = 14
JOKER_NAMES = ("X", "Y", "Z")
HAND_WINS = 1
HAND_TIES = 0
HAND_LOSE = -1
