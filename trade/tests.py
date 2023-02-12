from django.test import TestCase

from .views import compute_pnl, compute_total_buy_volume, compute_total_sell_volume
from .models import Trade

class test_pnl(TestCase):

    def test_compute_total_buy_volume(self):

        self.assertEqual(compute_total_buy_volume(),0)

        testBuyTrade = Trade(quantity=10,price=100,side='buy',strategy='test_STR')
        testBuyTrade.save()

        self.assertEqual(compute_total_buy_volume(),10)


        testSellTrade = Trade(quantity=10,price=100,side='sell',strategy='test_STR')
        testSellTrade.save()

        self.assertEqual(compute_total_buy_volume(),10)

        testBuyTrade = Trade(quantity=10,price=100,side='buy',strategy='test_STR2')
        testBuyTrade.save()

        self.assertEqual(compute_total_buy_volume(),20)


    def test_compute_total_sell_volume(self):

        self.assertEqual(compute_total_sell_volume(),0)

        testSellTrade = Trade(quantity=10,price=100,side='sell',strategy='test_STR')
        testSellTrade.save()

        self.assertEqual(compute_total_sell_volume(),10)


        testBuyTrade = Trade(quantity=10,price=100,side='buy',strategy='test_STR')
        testBuyTrade.save()

        self.assertEqual(compute_total_sell_volume(),10)

        testSellTrade = Trade(quantity=10,price=100,side='sell',strategy='test_STR2')
        testSellTrade.save()

        self.assertEqual(compute_total_sell_volume(),20)

    def test_compute_pnl(self):
        
        #inittaly no profit or loss
        self.assertEqual(compute_pnl('test_STR'),0)    

        #add one sell trade of 10 units price 100 Euro => profit 1000 Euro 
        testSellTrade = Trade(quantity=10,price=100,side='sell',strategy='test_STR')
        testSellTrade.save()

        self.assertEqual(compute_pnl('test_STR'),1000)

        #calculate profit for wrong stratigy name (does not exisit) => must return 0
        self.assertEqual(compute_pnl('test_STR1'),0)

        #add one buy trade of 10 units price 100 Euro => loss 1000 Euro and total 0 profit
        testBuyTrade = Trade(quantity=10,price=100,side='buy',strategy='test_STR')
        testBuyTrade.save()

        self.assertEqual(compute_pnl('test_STR'),0)
