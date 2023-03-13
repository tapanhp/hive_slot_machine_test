class HiveRollMachineException(Exception):
    """Base class for all top level exceptions"""


class CreditExhaustedError(HiveRollMachineException):
    """When users left with no credits, Stop the game"""
