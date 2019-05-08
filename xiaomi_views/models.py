from django.db import models

# Create your models here.
class PhoneKind(models.Model):

    name = models.CharField(max_length=255, verbose_name='手机类型')
    desc = models.CharField(max_length=255, verbose_name='类型简介')

    def __str__(self):
        return self.name


class PhoneDetail(models.Model):
    title = models.CharField(max_length=255, verbose_name='手机型号', unique=True)
                                                # unique=True 表示这个是唯一索引  不能重复
    desc = models.CharField(max_length=1000, verbose_name='手机简介', default='暂无简介')
    online_time = models.DateField(verbose_name='上市日期')
    price = models.IntegerField(null=True, default=None, blank=True)
    # upload to 表示把图片上传到哪里
    img = models.ImageField(upload_to='phone', null=True, default=None, blank=True)
                                                # 表示可以不传  默认为空

    kind = models.ManyToManyField(PhoneKind) # 多对多
    # kind = models.ForeignKey(MovieKind,default=None)  这个是一对多

    def __str__(self):
        return self.title
