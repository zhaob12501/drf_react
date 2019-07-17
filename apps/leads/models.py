from django.db import models

# Create your models here.


class Lead(models.Model):
    name = models.CharField("领导名字", max_length=100, help_text="领导名字")
    email = models.EmailField("邮箱", help_text="邮箱")
    message = models.CharField("信息", max_length=300, help_text="信息")
    created_at = models.DateTimeField("创建时间", auto_now_add=True, help_text="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = "领导"
