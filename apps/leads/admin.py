import xadmin
from .models import Lead

# Register your models here.


class LeadAdmin:
    """
    list_display: 后台展示的字段
    search_fields: 后台可搜索的字段
    list_filter: 后台过滤器可使用的字段
    """

    list_display = ("name", "email", "message")
    search_fields = ("name", "email", "message")
    list_filter = ("name", "email", "message", "created_at")


xadmin.site.register(Lead, LeadAdmin)
