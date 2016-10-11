# coding: utf8
from __future__ import unicode_literals

from django.utils import timezone

from django.utils.translation import ugettext as _
from django.db import models
from xlsparse.models import Book
from django.contrib.auth.models import User


class CartItem(models.Model):
    count = models.CharField(max_length=30, default=1)
    product = models.ForeignKey(Book, verbose_name=_("Продукт"), null=True, blank=True)
    create_date = models.DateTimeField(verbose_name=_("Дата"), default=timezone.now)

    def __unicode__(self):
        return unicode(self.product) or u''

    class Meta:
        verbose_name_plural = _("Элементы корзины")
        verbose_name = _("Элемент корзины")


class Cart(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Пользователь"), related_name='cart')
    create_date = models.DateTimeField(verbose_name=_("Дата"), default=timezone.now)
    cart = models.ManyToManyField(CartItem, verbose_name=_("Корзина"))

    def __unicode__(self):
        return unicode(self.user) or u''

    class Meta:
        verbose_name_plural = _("Корзины")
        verbose_name = _("Корзину")








