# Generated by Django 2.1.7 on 2019-12-18 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_star', models.IntegerField(blank=True, default=5, null=True, verbose_name='评分')),
                ('owner_text', models.TextField(blank=True, default='', null=True, verbose_name='评价内容')),
                ('lancer_star', models.IntegerField(blank=True, default=5, null=True, verbose_name='接单人评分')),
                ('lancer_text', models.TextField(blank=True, default='', null=True, verbose_name='评价内容')),
                ('owner_commented', models.BooleanField(default=False, verbose_name='发单人是否评价')),
                ('lancer_commented', models.BooleanField(default=False, verbose_name='接单人是否评价')),
                ('order', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order', verbose_name='发单人订单')),
            ],
            options={
                'verbose_name': '评价',
                'verbose_name_plural': '评价s',
            },
        ),
    ]
