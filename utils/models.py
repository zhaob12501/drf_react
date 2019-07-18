from django.db import models


class ModelBase(models.Model):
    """ 用于继承 """
    create_date = models.DateTimeField("创建时间", auto_now_add=True, help_text="创建时间")
    update_date = models.DateTimeField("更新时间", auto_now=True, help_text="更新时间")
    is_delete = models.BooleanField("逻辑删除", default=False, help_text="逻辑删除")

    class Meta:
        # 为抽象模型类, 用于其他模型来继承，数据库迁移时不会创建ModelBase表
        abstract = True
