# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 07:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xlsparse', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u0440\u0437\u0438\u043d\u0443',
                'verbose_name_plural': '\u041a\u043e\u0440\u0437\u0438\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(default=1, max_length=30)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=12, max_length=30, verbose_name='\u0421\u0443\u043c\u043c\u0430')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xlsparse.Book', verbose_name='\u041f\u0440\u043e\u0434\u0443\u043a\u0442')),
            ],
            options={
                'verbose_name': '\u042d\u043b\u0435\u043c\u0435\u043d\u0442 \u043a\u043e\u0440\u0437\u0438\u043d\u044b',
                'verbose_name_plural': '\u042d\u043b\u0435\u043c\u0435\u043d\u0442\u044b \u043a\u043e\u0440\u0437\u0438\u043d\u044b',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='cart',
            field=models.ManyToManyField(to='cart.CartItem', verbose_name='\u041a\u043e\u0440\u0437\u0438\u043d\u0430'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c'),
        ),
    ]