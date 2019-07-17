import xadmin
from xadmin import views
from .models import Lead


class BaseSetting:
    """ xadmin 的基础信息配置 """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    """ xadmin 通用信息配置 """
    site_title = "Leads Xadmin"
    site_footer = "zhao12501@163.com"


class LeadAdmin:
    """
    list_display: 后台展示的字段
    search_fields: 后台可搜索的字段
    list_filter: 后台过滤器可使用的字段
    """

    list_display = ("name", "email", "message")
    search_fields = ("name", "email", "message")
    list_filter = ("name", "email", "message", "created_at")


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

xadmin.site.register(Lead, LeadAdmin)
