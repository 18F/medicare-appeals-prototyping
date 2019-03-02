import uuid
from decimal import Decimal
from django.db import models
import medicare_appeals.appeals.choices as choices


class HollisticAppeal(models.Model):
    class Meta:
        db_table = 'hollistic_appeal'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Claim(models.Model):
    class Meta:
        db_table = 'claim'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250)
    original_claim_id = models.CharField(max_length=50)
    claim_type = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    service_place = models.CharField(max_length=50)
    amount_billed = models.DecimalField(
        max_digits=9, decimal_places=2, default=Decimal('0.00'))
    amount_paid = models.DecimalField(
        max_digits=9, decimal_places=2, default=Decimal('0.00'))
    amount_controversy = models.DecimalField(
        max_digits=9, decimal_places=2, default=Decimal('0.00'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Appeal(models.Model):
    class Meta:
        db_table = 'appeal'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250)
    original_appeal_id = models.CharField(max_length=50)
    medicare_part = models.CharField(
        max_length=50, choices=choices.MEDICARE_PART)
    requestor_type = models.CharField(
        max_length=50, choices=choices.REQUESTOR_TYPE)
    service_category = models.CharField(
        max_length=50, choices=choices.APPEAL_SERVICE_CATEGORY)
    claims = models.ManyToManyField(
        Claim,
        through='AppealToClaim',
        through_fields=('appeal', 'claim'),
    )
    hollistic_appeal = models.ForeignKey(
        'HollisticAppeal', on_delete=models.CASCADE, blank=True, null=True)
    provider = models.ForeignKey(
        'Provider', on_delete=models.CASCADE, blank=True, null=True)
    appellant = models.ForeignKey(
        'Appellant', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AppealToClaim(models.Model):
    class Meta:
        db_table = 'appeal_to_claim'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appeal = models.ForeignKey(Appeal, on_delete=models.CASCADE)
    claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Appellant(models.Model):
    class Meta:
        db_table = 'appellant'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250)
    appellant_type = models.CharField(max_length=60)
    medicare_beneficiary_id = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Level(models.Model):
    class Meta:
        db_table = 'level'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level_name = models.CharField(max_length=50, choices=choices.APPEAL_LEVEL)
    description = models.CharField(max_length=250)
    reviewer_name = models.CharField(max_length=60)
    reviewer_type = models.CharField(max_length=25)
    location = models.CharField(max_length=50)
    appeal = models.OneToOneField('Appeal', on_delete=models.CASCADE)
    hollistic_appeal = models.ForeignKey(
        'HollisticAppeal', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Provider(models.Model):
    class Meta:
        db_table = 'provider'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250)
    provider_type = models.CharField(max_length=60)
    national_provider_id = models.CharField(max_length=25)
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Status(models.Model):
    class Meta:
        db_table = 'status'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250)
    status_type = models.CharField(max_length=60)
    action = models.CharField(max_length=60)
    is_current = models.CharField(max_length=60)
    appeal = models.ForeignKey('Appeal', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
