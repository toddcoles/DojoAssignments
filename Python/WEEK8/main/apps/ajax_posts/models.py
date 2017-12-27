# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)