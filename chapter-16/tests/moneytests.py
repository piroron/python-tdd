"""金額テスト"""
import unittest as ut
from moneys.money import Money
from moneys.bank import Bank
from moneys.total import Total

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

    def test_simple_addition(self):
        """同一単位の加算"""
        five = Money.dollar(5)
        total = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(10), reduced, "equal")

    def test_plus_returnsum(self):
        """合計を返す場合のテスト"""
        five = Money.dollar(5)
        result = five.plus(five)
        total: Total = result
        self.assertEqual(five, total.augend())
        self.assertEqual(five, total.addend())

    def test_reducesum(self):
        """合計のテスト"""
        total = Total(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        """Moneyのテスト"""
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result, "Money as expression")

    def test_reducemoney_diff_currency(self):
        """別の貨幣へ変換"""
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_identity_rate(self):
        """同一貨幣"""
        self.assertEqual(1, Bank().rate("USD", "USD"))

    def test_mixed_addition(self):
        """異なる通貨の加算"""
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(five_bucks.plus(ten_francs), "USD")
        self.assertEqual(Money.dollar(10), result)

    def test_totalplus_money(self):
        """合計の加算"""
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        total = Total(five_bucks, ten_francs).plus(five_bucks)
        result = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(15), result)

    def test_total_times(self):
        """moneyの倍"""
        five_bucks = Money.dollar(5)
        ten_francs = Money.franc(10)
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        total = Total(five_bucks, ten_francs).times(2)
        result = bank.reduce(total, "USD")
        self.assertEqual(Money.dollar(20), result)