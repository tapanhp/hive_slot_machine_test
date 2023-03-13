import random
from collections import namedtuple
from typing import Optional

from config import DEFAULT_USER_ACCOUNT_CREDITS, CREDIT_CUT_FOR_SINGLE_ROLL, MINIMUM_CREDIT_TO_PLAY
from exceptions import CreditExhaustedError


class CreditManager:
    """Manages credit after each iteration"""

    def __init__(self):
        self.credits = 0

    def set_initial_credit(self):
        """Set initial credits to user account"""
        # self.user.credit = SET FROM CONFIG
        self.credits = DEFAULT_USER_ACCOUNT_CREDITS

    def deduct_credit_for_roll(self,
                               no_of_rolls: int = 1,
                               default_credit_cut: int = CREDIT_CUT_FOR_SINGLE_ROLL):
        self.has_minimum_credit()

        total_credit_to_cut = -abs(no_of_rolls * default_credit_cut)
        self.change_credit_after_roll(total_credit_to_cut)

    def change_credit_after_roll(self, credit: int):
        self.credits += credit

    def has_minimum_credit(self):
        if self.credits < MINIMUM_CREDIT_TO_PLAY:
            raise CreditExhaustedError("No sufficient credit for playing the game")
        return True

    def cash_out(self):
        if self.credits > 0:
            data = {"credit_won": self.credits, "msg": f"Yayyy! you won {self.credits}"}
            self.credits = 0
        else:
            data = {"credit_won": 0, "msg": "You haven't won this time, Please try your luck next time"}
        return data


def retrieve_all_cash_for_session():
    """
    Here this method is outer interface to communicate with routes
    :return:dict: Credit cash out response
    """
    return CreditManager().cash_out()
