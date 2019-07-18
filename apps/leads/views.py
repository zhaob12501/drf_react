from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from rest_framework.schemas import AutoSchema
# import coreapi
# Create your views here.


class LeadListCreate(generics.ListCreateAPIView):
    """
    get:
        返回所有已存在的 Lead 对象的列表

    post:
        创建一个新的 Lead 实例
    """
    queryset = Lead.objects.filter(is_delete=False).all()
    serializer_class = LeadSerializer
    # 必须自定义 schema
    schema = AutoSchema()


class LeadUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.filter(is_delete=False).all()
    serializer_class = LeadSerializer
    schema = AutoSchema()
