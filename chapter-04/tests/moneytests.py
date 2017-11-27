"""金額テスト"""
import unittest as ut
from moneys.dollar import Dollar

class MoneyTest(ut.TestCase):
    """Moneyクラスのテスト"""
    def test_multiplication(self):
        """テスト"""
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2), "5 * 2")
        self.assertEqual(Dollar(15), five.times(3), "5 * 3")

    def test_equality(self):
        """同一性テスト"""
        self.assertTrue(Dollar(5) == Dollar(5), "$5 == $5")
        self.assertFalse(Dollar(5) == Dollar(6), "$5 != $6")
