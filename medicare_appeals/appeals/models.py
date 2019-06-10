import uuid
from decimal import Decimal
from django.db import models
import medicare_appeals.appeals.choices as choices


class HolisticAppeal(models.Model):
    class Meta:
        db_table = 'holistic_appeal'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Claim(models.Model):
    class Meta:
        db_table = 'claim'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250, null=True)
    original_claim_id = models.CharField(max_length=100)
    claim_type = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, null=True)
    service_place = models.CharField(
        max_length=100, choices=choices.PLACE_OF_SERVICE, null=True)
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
    description = models.CharField(max_length=250, null=True)
    original_appeal_id = models.CharField(max_length=50)
    medicare_part = models.CharField(
        max_length=100, choices=choices.MEDICARE_PART, null=True)
    requestor_type = models.CharField(
        max_length=100, choices=choices.REQUESTOR_TYPE, null=True)
    service_category = models.CharField(
        max_length=100, choices=choices.APPEAL_SERVICE_CATEGORY, null=True)
    rac = models.BooleanField(default=False)
    claims = models.ManyToManyField(
        Claim,
        through='AppealToClaim',
        through_fields=('appeal', 'claim'),
    )
    holistic_appeal = models.ForeignKey(
        'HolisticAppeal', on_delete=models.CASCADE, blank=True, null=True)
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
    description = models.CharField(max_length=250, null=True)
    appellant_type = models.CharField(
        max_length=100, choices=choices.REQUESTOR_TYPE, null=True)
    medicare_beneficiary_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Level(models.Model):
    class Meta:
        db_table = 'level'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    level_name = models.CharField(max_length=50, choices=choices.APPEAL_LEVEL)
    description = models.CharField(max_length=250, null=True)
    reviewer_name = models.CharField(max_length=100, null=True)
    reviewer_type = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    appeal = models.OneToOneField('Appeal', on_delete=models.CASCADE)
    holistic_appeal = models.ForeignKey(
        'HolisticAppeal', on_delete=models.CASCADE)
    appeal = models.ForeignKey(
        'Appeal', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Provider(models.Model):
    class Meta:
        db_table = 'provider'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250, null=True)
    provider_type = models.CharField(
        max_length=100, choices=choices.PROVIDER_TYPE, null=True)
    national_provider_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Status(models.Model):
    class Meta:
        db_table = 'status'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=250, null=True)
    category = models.CharField(max_length=100, null=True)
    action = models.CharField(max_length=100, null=True)
    appeal = models.ForeignKey('Appeal', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
