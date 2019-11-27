from django.db import models
from django.utils.crypto import get_random_string

from app.user.models import User

class Order(models.Model):

    STATUS_SHEET = (
        (1, 'New'),
        (2, 'Confirm'),
        (3, 'Complete'),
        (4, 'Pending'),
        (5, 'Cancel'),
        (6, 'Delete'),
    )

    # 订单状态
    status = models.IntegerField(blank=True, null=True, choices=STATUS_SHEET, default=1)
    
    # 订单类型
    cagetory = models.IntegerField(blank=True, null=True)

    # 信息
    main_info = models.TextField(blank=True, null=True)

    # 副信息
    sub_info = models.TextField(blank=True, null=True)

    # 自定义信息
    other_info = models.TextField(blank=True, null=True)

    # 开始时间
    from_date = models.DateTimeField(blank=True, null=True)

    # 结束时间
    to_date = models.DateTimeField(blank=True, null=True)

    # 地址
    addr = models.TextField(blank=True, null=True)

    # 图片
    image = models.ImageField(blank=True, null=True)

    # 服务码
    code = models.CharField(blank=True, null=True, default=get_random_string(length=4))

    # 评价
    eva_info = models.TextField(blank=True, null=True)

    # 评价等级
    eva_lv = models.IntegerField(blank=True, null=True)

    # 坐标
    lat = models.FloatField(blank=True, null=True)

    # 坐标
    lgt = models.FloatField(blank=True, null=True)

    # 创建时间
    create_at = models.DateTimeField(auto_now_add=True)

    # 修改时间
    change_at = models.DateTimeField(auto_now=True)

    # 客人
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='order', blank=True, null=True)







