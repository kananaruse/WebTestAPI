# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32)
    comment = models.CharField(max_length=32)

    def __repr__(self):
        # 主キーとnameを表示させて見やすくする
        # ex) 1: Alice
        return "{}: {}".format(self.pk, self.user_id)

    __str__ = __repr__
