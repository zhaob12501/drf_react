from .serializers import GoodsSerializers
from rest_framework import generics
from rest_framework.schemas import AutoSchema
from . import models
# Create your views here.


class GoodsListCreate(generics.ListCreateAPIView):
    """
    get:
        返回所有已存在的商品对象

    post:
        创建一个新的商品实例
    """
    queryset = models.Goods.objects.all()
    serializer_class = GoodsSerializers
    schema = AutoSchema()
