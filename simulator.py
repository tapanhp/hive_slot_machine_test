from config import TOTAL_SLOTS_IN_MACHINE, CREDIT_CUT_FOR_SINGLE_ROLL
from exceptions import CreditExhaustedError
from slot_machine_algorithm import should_roll_again
from services.slot_machine_service import SlotMachine
from services.credit_service import CreditManager

from utils import separate_line

total_hands_played = 0
total_jackpots = 0
total_cheat_run = 0

total_received_credit_by_house = 0
total_spent_credit_by_house = 0
total_pre_credit_by_house = 0
total_saved_by_re_rolling = 0

total_won_credit_by_user = 0

slot_machine = SlotMachine(TOTAL_SLOTS_IN_MACHINE)

for user in range(1):

    credit_manager = CreditManager()
    credit_manager.set_initial_credit()
    print(f"Provided initial credit {credit_manager.credits} to user {user + 1}")
    total_pre_credit_by_house += credit_manager.credits

    while True:
        try:
            credit_manager.deduct_credit_for_roll()  # 1
            total_received_credit_by_house += CREDIT_CUT_FOR_SINGLE_ROLL

            print(f"User {user + 1} lost {CREDIT_CUT_FOR_SINGLE_ROLL}, Now credit {credit_manager.credits}")

            slot_machine.pull_lever()
            total_hands_played += 1

            if slot_machine.check_if_jackpot():
                won_credit = slot_machine.calculate_new_credits()

                if should_roll_again(credit_manager.credits):
                    total_cheat_run += 1
                    print(f"CHEAT for user with {credit_manager.credits} credit :: Re-rolling, saved {won_credit}")
                    total_saved_by_re_rolling += won_credit
                    # Pull lever should be called here
                    continue

                total_jackpots += 1
                total_won_credit_by_user += won_credit
                # slot_machine.show_jackpot_value()

                total_spent_credit_by_house += won_credit
                credit_manager.change_credit_after_roll(won_credit)

        except CreditExhaustedError:
            print(f"User {user + 1} has exhausted credit, continue with next")
            break

    print(f"Total user credits are {credit_manager.credits}")

separate_line()

print(f"Total Jackpots are {total_jackpots},\n"
      f"Cheat counts are {total_cheat_run} that saved {total_saved_by_re_rolling}")

separate_line()

print(f"Total hands played {total_hands_played} \n"
      f"Total won credit by house {total_received_credit_by_house}\n"
      f"Total Pre credit spent by house {total_pre_credit_by_house}\n"
      f"and lost {total_spent_credit_by_house}")

print(f"Total won credit by jackpots {total_won_credit_by_user}")
