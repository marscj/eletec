from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from django.utils.crypto import get_random_string

from app.user.models import User, Contract, Comment
from app.generic.models import Image

def random_string():
    return get_random_string(length=4)

class Order(models.Model):

    class Status(models.IntegerChoices):
        New = 0
        Confirm = 1
        Complete = 2
        Pending = 3
        Cancel = 4
        Delete = 5

    class Service(models.IntegerChoices):
        AC =  0 #'Air Conditioner',
        Electrical = 1
        Plumbing = 2
        Cleaning = 3 #'House Cleaning',

    # 订单状态
    status = models.IntegerField(blank=True, null=True, choices=Status.choices, default=Status.New)
    
    # 订单类型
    service = models.IntegerField(blank=True, null=True, choices=Service.choices, default=Service.AC)

    # 信息
    main_info = models.IntegerField(blank=True, null=True, default=0)

    # 副信息
    sub_info = models.IntegerField(blank=True, null=True, default=0)

    # 自定义信息
    other_info = models.CharField(blank=True, null=True, max_length=256)

    # 开始时间
    from_date = models.DateTimeField(blank=True, null=True)

    # 结束时间
    to_date = models.DateTimeField(blank=True, null=True)

    # 服务码
    code = models.CharField(blank=True, null=True, max_length=4, default=random_string)

    # 地址
    address = models.CharField(blank=True, null=True, max_length=128)

    # 坐标
    lat = models.FloatField(blank=True, null=True)

    # 坐标
    lng = models.FloatField(blank=True, null=True)

    # 创建时间
    create_at = models.DateTimeField(auto_now_add=True)

    # 修改时间
    change_at = models.DateTimeField(auto_now=True)

    # 评价
    comments = GenericRelation(Comment, related_query_name='order')

    # 评价
    images = GenericRelation(Image, related_query_name='order')

    # 合同
    contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, related_name='order', blank=True, null=True)

    # 客人
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='order', blank=True, null=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.orderID

    @property
    def orderID(self):
        return '%d-%s' % (100000 + self.id, self.create_at.strftime("%y%m%d"))