"""金額テスト"""
import unittest as ut
from moneys import dollar

class MoneyTest(ut.TestCase):
    """Moneyクラスのテスト"""
    def test_multiplication(self):
        """テスト"""
        five = dollar.Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amount, "amount expected 10")
