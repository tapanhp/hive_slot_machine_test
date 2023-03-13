from random import choices
from collections import Counter


def should_roll_again(user_credits: int):
    """
    Decides whether Machine will re-roll before sending credits back to FE

    :param user_credits: Current user's credit
    :return: bool :
    """
    re_roll_choices = True, False

    if user_credits < 40:
        rolling_probability = 0.0, 1.0
    elif 40 < user_credits < 60:
        rolling_probability = 0.3, 0.7
    else:
        rolling_probability = 0.6, 0.4

    return choices(re_roll_choices, rolling_probability)[0]

# def check_rolling_probability():
#     with open("output.txt", "a") as outcome:
#         answers = [should_roll_again(75) for _ in range(1)]
#         outcome.write(f"{(int(answers[0]))}\n")


# check_rolling_probability()


# def check_thesis():
#     with open("output.txt", "r") as inco:
#         all_items = inco.readlines()
#         new_items = [int(item.replace("\n", "")) for item in all_items]
#         print(Counter(new_items))


# check_thesis()
