# -*- coding: utf-8 -*-
from django.db import models


class MyModel(models.Model):
    """Model example."""
    blah = models.TextField(max_length=45)
