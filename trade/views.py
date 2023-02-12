from django.shortcuts import render
from .models import Trade,PnlData
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TradeSerializer,PnlDataSerializer
from django.db.models import Sum,Q,F
from rest_framework import status
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

def compute_total_buy_volume() -> float:
    totalBuy = 0
    buyTrades = Trade.objects.filter(side='buy')

    if buyTrades:
        totalBuy = buyTrades.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    
    return totalBuy

def compute_total_sell_volume() -> float:
    totalSell = 0
    sellTrades = Trade.objects.filter(side='sell')
    
    if sellTrades:
        totalSell = sellTrades.aggregate(total_quantity=Sum('quantity'))['total_quantity']
    
    return totalSell

def compute_pnl(strategy_id: str) -> float:
    totalSell = 0
    totalBuy = 0

    sellTrades = Trade.objects.filter(strategy=strategy_id,side='sell')
    if sellTrades:
        totalSell=sellTrades.aggregate(total=Sum(F('price') * F('quantity')))['total']

    buyTrades = Trade.objects.filter(strategy=strategy_id,side='buy')
    if buyTrades:
        totalBuy = buyTrades.aggregate(total=Sum(F('price') * F('quantity')))['total']

    pnl = totalSell - totalBuy
    return pnl

@api_view(['GET'])
def Get_PNL(request,strategy_id):
   
    pnlAmount = compute_pnl(strategy_id=strategy_id)

    result = PnlData(value=pnlAmount,strategy=strategy_id,unit='euro')
    
    serializer = PnlDataSerializer(result)
    return Response(serializer.data,status=status.HTTP_200_OK)