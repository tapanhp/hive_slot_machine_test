import random
from collections import namedtuple
from typing import Optional

# Define slot items in a simpler manner with namedtuple
SlotItem = namedtuple("RollItem", ["title", "short_sign", "winning_value"])


def get_slot_items():
    """
    Returns tuple of all items to fit into slots

    :return:tuple: Namedtuple objects of SlotItem
    """
    cherry = SlotItem("Cherry", "C", 10)
    lemon = SlotItem("Lemon", "L", 20)
    orange = SlotItem("Orange", "O", 30)
    watermelon = SlotItem("WaterMelon", "W", 40)
    return cherry, lemon, orange, watermelon,


def get_all_slot_items_response():
    """
    API facing method used for providing list of slot items to users
    :return:list: dict/json representation of SlotItem object
    """
    return [item._asdict() for item in get_slot_items()]


class SlotMachine:
    """The main machine class"""

    def __init__(self, no_of_slots):
        # initialise with machine
        self.slots = [Slot() for _ in range(no_of_slots)]

    def pull_lever(self):
        for slot in self.slots:
            current_choice = random.choice(get_slot_items())
            slot.fill_with_item(current_choice)

    def check_if_jackpot(self):
        return len(set(self.slots)) == 1

    def calculate_new_credits(self):
        return self.slots[0].item.winning_value

    def show_jackpot_value(self):
        for slot in self.slots:
            print(slot.item)


class Slot:
    """Box can contain roll items"""

    def __init__(self):
        # Rolls out empty box and attach with machine
        self.item = Optional[SlotItem]

    def fill_with_item(self, item: SlotItem):
        self.item = item

    def get_slot_worth(self):
        return self.item.winning_value

    def __eq__(self, other):
        return self.item == other.item

    def __hash__(self):
        return self.item.winning_value
