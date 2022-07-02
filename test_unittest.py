import unittest
from parameterized import parameterized

from stack_class import Stack

class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        print(">>> setUp")

    def tearDown(self) -> None:
        print(">>> tearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print(">>> setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print(">>> tearDownClass")

    @parameterized.expand(
        [
            (1, "(((([{}]))))", "Сбалансированно"),
            (2, "[([])((([[[]]])))]{()}", "Сбалансированно"),
            (3, "{{[()]}}", "Сбалансированно"),
            (4, "}{}", "Несбалансированно"),
            (5, "{{[(])]}}", "Несбалансированно"),
            (6, "[[{())}]", "Несбалансированно"),
            (7, "[{]}", "Несбалансированно"),
            (8, "([[](({}))])([", "Несбалансированно"),
            (9, "(()[[]]){[()][]}[(())]", "Сбалансированно"),
            (10, "[]()(){}(())[]", "Сбалансированно"),
            (11, "[[[(({(())", "Несбалансированно"),
            (12, "{}", "Сбалансированно"),
            (13, "", "Последовательность пуста")
        ]
    )
    def test_check_balance(self, num, staples, result):
        print(f">>> stack # {num}")
        stack = Stack(staples)
        self.assertEqual(stack.check_balance(), result)