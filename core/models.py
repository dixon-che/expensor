# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from datetime import datetime
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from . import DIRECTION_CHOICES


class Action(models.Model):
    name = models.CharField(max_length=128)


class Transaction(models.Model):
    direction = models.SmallIntegerField(choices=DIRECTION_CHOICES,
                                         db_index=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10,
                                 validators=[MinValueValidator(Decimal(0))])
    comment = models.TextField(blank=True, null=True)


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=10)
    position = models.CharField(max_length=256)
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(db_index=True, default=False)
    works_from = models.DateField(default=datetime.utcnow)


class Salary(models.Model):
    person = models.ForeignKey(Person)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(default=datetime.utcnow)
    active_from = models.DateField(default=datetime.utcnow)

    class Meta:
        get_latest_by = 'active_from'