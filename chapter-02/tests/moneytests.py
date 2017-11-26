"""金額テスト"""
import unittest as ut
from moneys import dollar

class MoneyTest(ut.TestCase):
    """Moneyクラスのテスト"""
    def test_multiplication(self):
        """テスト"""
        five = dollar.Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount, "5 * 2")
        product = five.times(3)
        self.assertEqual(15, product.amount, "5 * 3")
