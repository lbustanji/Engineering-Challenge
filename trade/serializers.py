from rest_framework import serializers
from trade.models import Trade,PnlData

class TradeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'

class PnlDataSerializer (serializers.ModelSerializer):
    class Meta:
        model = PnlData
        fields = ['strategy','value','unit','capture_time']