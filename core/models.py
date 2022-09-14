from django.db import models


class TimeStampModel(models.Model):
    dt_created = models.DateTimeField("생성시간", auto_now_add=True)
    dt_updated = models.DateTimeField("수정시간", auto_now=True)

    class Meta:
        abstract = True