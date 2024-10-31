import random
import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):

    def test_random_credit_card_numbers(self):
        num_tests = 1005000
        for _ in range(num_tests):
            length = random.randint(14, 17)
            number = ''.join(random.choices('0123456789', k=length))
            try:
                credit_card_validator(number)
            except Exception as e:
                pass


if __name__ == "__main__":
    unittest.main()
