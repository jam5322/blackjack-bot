"""
Class representing a human player in blackjack.
"""

import player


class User(player.Player):

    def __init__(self):
        super().__init__()
        #probabl some more variable defining who the user is like name, stuff like that
        self.bank = 5000
        self.bet = 0 # zero means that there is no current bet

    def bet(self, bet):
        """
        Bets a certain amount of money during a round of blackjack.
        :param bet: integer number of money user wants to bet
        """
        if isinstance(bet, int):
            if bet > self.bank or bet < 1:
                #send error message
                pass
            elif bet % 50 != 0:
                #send message that bet must be a factor of 50
                pass
            else:
                #send message that user bet a certain amount
                self.bet = bet
        else:
            #send message that bet must be an integer
            pass

    def reset_bet(self):
        """
        Resets the users bet to no bet (zero)
        """
        self.bet = 0



