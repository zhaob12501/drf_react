import xadmin
from xadmin import views


class BaseSetting:
    """ xadmin 的基础信息配置 """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    """ xadmin 通用信息配置 """
    site_title = "Leads Xadmin"
    site_footer = "zhao12501@163.com"


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
