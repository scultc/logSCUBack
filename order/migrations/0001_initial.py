# Generated by Django 2.1.7 on 2019-12-18 09:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('orderid', models.AutoField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('expireDateTime', models.DateTimeField(verbose_name='过期时间')),
                ('order_status', models.IntegerField(choices=[(0, 'uncompleted'), (1, 'completing'), (2, 'uncommented'), (3, 'completed'), (4, 'canceled'), (5, 'expired')], default=0, verbose_name='订单状态')),
                ('kuaidi', models.CharField(max_length=256, verbose_name='快递商')),
                ('money', models.DecimalField(decimal_places=4, default=0, max_digits=50, verbose_name='酬劳')),
                ('pos', models.CharField(default='快递街', max_length=256, verbose_name='地点')),
                ('received_pos', models.CharField(max_length=256, verbose_name='收货地址')),
                ('campus', models.CharField(max_length=256, verbose_name='校区')),
                ('goods_weight', models.DecimalField(decimal_places=4, default=0, max_digits=50, verbose_name='物品重量')),
                ('hidden_info', models.TextField(blank=True, null=True, verbose_name='隐藏的信息')),
                ('goods_introduction', models.CharField(blank=True, max_length=256, null=True, verbose_name='商品简介')),
                ('goods_category', models.CharField(blank=True, max_length=256, null=True, verbose_name='商品种类')),
                ('goods_img', models.CharField(default='/static/account/img/bob.jpg', max_length=2000, verbose_name='图片url')),
                ('free_lancer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lancer_orders', to='account.user', verbose_name='接单人')),
                ('order_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner_orders', to='account.user', verbose_name='订单主人')),
            ],
        ),
    ]
