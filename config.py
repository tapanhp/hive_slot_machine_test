import os
from dotenv import load_dotenv
from utils import convert_to_integer

load_dotenv()

DEFAULT_USER_ACCOUNT_CREDITS = convert_to_integer(os.getenv("DEFAULT_USER_ACCOUNT_CREDITS"))
TOTAL_SLOTS_IN_MACHINE = convert_to_integer(os.getenv("TOTAL_SLOTS_IN_MACHINE"))
CREDIT_CUT_FOR_SINGLE_ROLL = convert_to_integer(os.getenv("CREDIT_CUT_FOR_SINGLE_ROLL"))
MINIMUM_CREDIT_TO_PLAY = convert_to_integer(os.getenv("MINIMUM_CREDIT_TO_PLAY"))
