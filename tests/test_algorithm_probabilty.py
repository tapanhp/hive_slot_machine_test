import pytest

from slot_machine_algorithm import should_roll_again
from collections import Counter


@pytest.fixture
def get_n_rolling_results():
    def get_n_rolling_results(current_user_credits: int, n: int):
        return [should_roll_again(current_user_credits) for _ in range(n)]

    return get_n_rolling_results


class TestSlotMachineAlgo:
    def test_no_rolling_case(self):
        current_user_credits = 35
        assert should_roll_again(current_user_credits) is False

    def test_re_rolling_case_for_user_credit_between_40_60(self, get_n_rolling_results):
        current_user_credits = 46
        results = get_n_rolling_results(current_user_credits, 10000)
        counts = Counter(results)
        # 30% 70% split case - It mostly ends up near 28-32% range in general testing scenarios
        # Check other methods in slot_machine_algorithm file for more details
        assert counts[1] in range(2800, 3200)
        assert counts[0] in range(6800, 7200)

    def test_re_rolling_case_for_user_credit_above_60(self, get_n_rolling_results):
        current_user_credits = 65
        results = get_n_rolling_results(current_user_credits, 10000)
        counts = Counter(results)
        # 40% 60% split case - It mostly ends up near 58-62% + 3800-4200 range in general testing scenarios
        # Check other methods in slot_machine_algorithm file for more details
        assert counts[1] in range(5800, 6200)
        assert counts[0] in range(3800, 4200)
