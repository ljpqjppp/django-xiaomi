from django.db import models
from django.contrib.auth.models import AbstractUser
from xiaomi_views.models import PhoneDetail
from django.utils.timezone import now


class MyUsers(AbstractUser):
    pass


class UserPhoneComment(models.Model):
    user = models.ForeignKey(MyUsers, verbose_name='评论手机的用户')
    phone = models.ForeignKey(PhoneDetail, verbose_name='被评论的手机')
    context = models.TextField(verbose_name='评论内容', max_length=2000)
    time = models.DateTimeField(verbose_name='评论时间', default=now)

    class Meta:
        unique_together = ('user', 'phone')

    def __str__(self):
        return '{}评论{}电影'.format(self.user.username, self.phone.title)

