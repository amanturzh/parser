# coding: utf-8
from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=300, verbose_name=_("Название"))
    usd = models.CharField(max_length=30, verbose_name=_("Доллар"))
    kgs = models.CharField(max_length=30, verbose_name=_("Сом"))

    def __unicode__(self):
        return unicode(self.title) or u''


class File(models.Model):
    xls = models.FileField(upload_to='xlx/')


    def __unicode__(self):
        return unicode(self.xls) or u''
