"""金額テスト"""
import unittest as ut
from moneys.money import Money

class MoneyTest(ut.TestCase):
    """Moneyクラスのテスト"""
    def test_multiplication(self):
        """金額を指定倍する"""
        five: Money = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2), "5 * 2")
        self.assertEqual(Money.dollar(15), five.times(3), "5 * 3")

    def test_equality(self):
        """同一性テスト"""
        self.assertTrue(Money.dollar(5) == Money.dollar(5), "$5 == $5")
        self.assertFalse(Money.dollar(5) == Money.dollar(6), "$5 != $6")
        self.assertFalse(Money.franc(5) == Money.dollar(5), "f5 != $5")

    def test_currency(self):
        """通貨単位のテスト"""
        self.assertEqual("USD", Money.dollar(1).currency(), "Dollar Unit")
        self.assertEqual("CHF", Money.franc(1).currency(), "Franc Unit")
