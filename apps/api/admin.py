import xadmin
from . import models
# Register your models here.


class GoodsAdmin:
    """
    list_display: 后台展示的字段
    search_fields: 后台可搜索的字段
    list_filter: 后台过滤器可使用的字段
    """

    list_display = ("name", "number", "price", "update_date")
    search_fields = ("name", "number", "price", "update_date")
    list_filter = ("name", "number", "price", "create_date", "update_date")

xadmin.site.register(models.Goods, GoodsAdmin)
