# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from colorful.fields import RGBColorField



class LightShow(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LightShowStep(models.Model):
    show = models.ForeignKey(LightShow)
    light = models.IntegerField(choices=settings.LED_CHOICES)
    color = RGBColorField(default="green")
    red = models.IntegerField(blank=True, null=True)
    green = models.IntegerField(blank=True, null=True)
    blue = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    def hex(self):
        return self.color

    class Meta:
        ordering = ['order', ]
        unique_together = ('show', 'light', 'order')

    def __str__(self):
        return '{}, LED {}, order {}, color ({},{},{})'.format(self.show, self.light, self.order, self.red, self.green, self.blue)

    
