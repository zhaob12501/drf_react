from rest_framework import serializers
from . import models


class GoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Goods
        fields = "__all__"
