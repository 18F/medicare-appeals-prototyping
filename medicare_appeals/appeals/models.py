import uuid
from django.db import models
import medicare_appeals.appeals.choices as choices


class Appeal(models.Model):
    class Meta:
        db_table = 'appeal'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=60)
    category = models.CharField(max_length=2, choices=choices.APPEAL_CATEGORY)
    status = models.CharField(
        max_length=1,
        choices=choices.APPEAL_STATUS,
        default=choices.APPEAL_STATUS_DEFAULT)


class Appellant(models.Model):
    class Meta:
        db_table: 'appellant'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=60)


class Claim(models.Model):
    class Meta:
        db_table = 'claim'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=60)


class History(models.Model):
    class Meta:
        db_table = 'history'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=60)


class Level(models.Model):
    class Meta:
        db_table = 'level'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=60)


class Provider(models.Model):
    class Meta:
        db_table = 'provider'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=60)


class Status(models.Model):
    class Meta:
        db_table = 'status'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=60)
