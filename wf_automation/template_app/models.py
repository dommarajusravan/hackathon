# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class templates(models.Model):
    name = models.CharField(max_length=50)
    flavor = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    os = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"

    def __unicode__(self):
        return self.name
        return '%s %s %s %s' % (self.name, self.flavor, self.image, self.os)

class deployment(models.Model):
    status = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    template = models.ForeignKey(templates)

    class Meta:
        verbose_name = "Deployment"
        verbose_name_plural = "Deployments"

    def __unicode__(self):
        return '%s %s' % (self.status, self.name)
