from utils.models import ModelBase
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Goods(ModelBase):
    """ 商品 """
    name = models.CharField(_("商品名称"), max_length=20, help_text=_("商品名称"))
    number = models.IntegerField(_("商品数量"), default=0, help_text=_("商品数量"))
    price = models.FloatField(_("商品价格"), default=0.0, help_text=_("商品价格"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tb_goods"
        ordering = ["-update_date", "-pk"]
        verbose_name = verbose_name_plural = "商品"
