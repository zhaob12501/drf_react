from rest_framework import serializers
from . import models


class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Goods
        fields = ("pk", "name", "number", "price", "create_date", "update_date")
