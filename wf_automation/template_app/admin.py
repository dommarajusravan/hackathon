# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import templates, deployment


# Register your models here.

admin.site.register(templates)
admin.site.register(deployment)
