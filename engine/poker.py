"""
Author:     Chris Knowles
File:       poker.py
Version:    1.0.0
Notes:      Small poker game
"""
# Imports
from data_model.card import Card
from data_model.player import Player
from data_model.dealer import Dealer
from data_model.table import Table


def main():
    """
    Entry point for the main script thread

    :return nothing
    """
    finished = True

    dealer = Dealer(name="Ken")
    print("Dealer: {0}".format(dealer))
    print("Deck: {0}".format(dealer.deck))

    players = [Player(name="John", funds=10000, max_hand_size=5),
               Player(name="Alan", funds=10000, max_hand_size=5),
               Player(name="Emma", funds=10000, max_hand_size=5)]

    p = "\n\t".join(map(str, players))
    print("Players:\n\t{0}".format(p if not p == "" else "None"))

    table = Table(name="Main Event", dealer=dealer)
    print(table)

    for player in players:
        table.add_player(player)

    print(table)

    dealer.deal_to_players(count=5)

    print(table)

    print("Deck: {0}".format(dealer.deck))

    for p in table.players:
        p.hand.determine_quality()
        print("{0} has hand with quality: {1}".format(p.name, p.hand.quality))

    q01 = players[0].hand.compare_hands(players[1].hand)
    if q01 == 0:
        print("{0}:(quality={1}) ties with {2}:(quality={3})".format(players[0].name, players[0].hand.quality.value,
                                                                     players[1].name, players[1].hand.quality.value))
    elif q01 > 0:
        print("{0}:(quality={1}) beats {2}:(quality={3})".format(players[0].name, players[0].hand.quality.value,
                                                                 players[1].name, players[1].hand.quality.value))
    else:
        print("{0}:(quality={1}) loses to {2}:(quality={3})".format(players[0].name, players[0].hand.quality.value,
                                                                    players[1].name, players[1].hand.quality.value))

    q02 = players[0].hand.compare_hands(players[2].hand)
    if q02 == 0:
        print("{0}:(quality={1}) ties with {2}:(quality={3})".format(players[0].name, players[0].hand.quality.value,
                                                                     players[2].name, players[2].hand.quality.value))
    elif q02 > 0:
        print("{0}:(quality={1}) beats {2}:(quality={3})".format(players[0].name, players[0].hand.quality.value,
                                                                 players[2].name, players[2].hand.quality.value))
    else:
        print("{0}:(quality={1}) loses to {2}:(quality={3})".format(players[0].name, players[0].hand.quality.value,
                                                                    players[2].name, players[2].hand.quality.value))

    q12 = players[1].hand.compare_hands(players[2].hand)
    if q12 == 0:
        print("{0}:(quality={1}) ties with {2}:(quality={3})".format(players[1].name, players[1].hand.quality.value,
                                                                     players[2].name, players[2].hand.quality.value))
    elif q12 > 0:
        print("{0}:(quality={1}) beats {2}:(quality={3})".format(players[1].name, players[1].hand.quality.value,
                                                                 players[2].name, players[2].hand.quality.value))
    else:
        print("{0}:(quality={1}) loses to {2}:(quality={3})".format(players[1].name, players[1].hand.quality.value,
                                                                    players[2].name, players[2].hand.quality.value))

    while not finished:
        #  1. Dealer shuffles cards
        #  2. Players deposit ante to table
        #  3. BB and SB players deposit blinds to table
        #  4. Dealer deals 2 cards to each player starting with the BB players (one player after
        #     on the button player)
        #  5. Pre-flop betting until all players call or fold
        #  6. Dealer deals 3 flop cards to table
        #  7. Pre-turn betting until all players call or fold
        #  8. Dealer deals turn card to table
        #  9. Pre-river betting until all players call or fold
        # 10. Dealer deals river card to table
        # 11. Post-river betting until all players call or fold
        # 12. Determine winning player hand (or split pot if tied)
        # 13. Players have opportunity to leave table
        # 14. If more than one remaining player then goto 15. else goto 17.
        # 15. The button advances to next player
        # 16. Return to 1.
        # 17. Game is finished
        pass


# Invoke main() program entrance
if __name__ == "__main__":
    # Execute only if run as a script
    main()
