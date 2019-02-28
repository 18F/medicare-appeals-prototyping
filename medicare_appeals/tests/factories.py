import factory
from decimal import Decimal
from random import randint, randrange, random
from medicare_appeals.appeals import choices, models
from . import helpers


class ClaimFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Claim

    description = factory.Faker('sentence', nb_words=10)
    original_claim_id = factory.Faker('ean13')
    claim_type = factory.Iterator(choices.APPEAL_SERVICE_CATEGORY)
    code = factory.Faker('ean13')
    service_place = factory.Iterator(choices.PLACE_OF_SERVICE)
    amount_billed = factory.LazyFunction(helpers.random_amount_billed)
    amount_paid = factory.LazyAttribute(lambda o: helpers.random_amount_paid(
        o.amount_billed))
    amount_controversy = factory.LazyAttribute(
        lambda o: helpers.calc_controversy(o.amount_billed, o.amount_paid))


class HollisticAppealFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.HollisticAppeal


class AppealFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Appeal

    description = factory.Faker('sentence', nb_words=10)
    original_appeal_id = factory.Faker('ean13')
    medicare_part = factory.Iterator(choices.MEDICARE_PART)
    requestor_type = factory.Iterator(choices.REQUESTOR_TYPE)
    service_category = factory.Iterator(choices.APPEAL_SERVICE_CATEGORY)


class AppealToClaimFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.AppealToClaim

    appeal = factory.SubFactory(AppealFactory)
    claim = factory.SubFactory(ClaimFactory)


class AppellantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Appellant

    description = factory.Faker('sentence', nb_words=10)
    appellant_type = factory.Iterator(choices.REQUESTOR_TYPE)
    medicare_beneficiary_id = factory.Faker('ean13')
    name = factory.Faker('name')


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Status

    description = factory.Faker('sentence', nb_words=10)
    status_type = factory.Iterator(choices.APPEAL_STATUS)
    action = factory.Iterator(choices.APPEAL_WORKFLOW_TYPE)
    is_current = factory.Faker('pybool')
    appeal = factory.SubFactory(AppealFactory)


class LevelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Level

    level_name = factory.Iterator(choices.APPEAL_LEVEL)
    description = factory.Faker('sentence', nb_words=10)
    reviewer_name = factory.Faker('name')
    reviewer_type = factory.LazyAttribute(lambda o: helpers.get_reviewer_type(
        o.level_name))
    location = factory.Faker('state')


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Provider

    description = factory.Faker('catch_phrase')
    provider_type = factory.Iterator(choices.PLACE_OF_SERVICE)
    national_provider_id = factory.Faker('ean13')
    name = factory.Faker('company')


def build_four_level_hollistic_appeal(max_appeals=10, **kwargs):
    total_appeals = helpers.evenify(randrange(4, max_appeals))
    claim_count = int((total_appeals - 2) / 2)
    is_open = kwargs.get('is_open', bool(randint(0, 1)))

    hollistic_appeal = HollisticAppealFactory()
    appellant = AppellantFactory()
    provider = ProviderFactory()
    claims = helpers.save_batch_fixtures(ClaimFactory, claim_count)
    appeals = helpers.save_batch_fixtures(
        AppealFactory,
        total_appeals,
        hollistic_appeal=hollistic_appeal,
        appellant=appellant,
        provider=provider)

    for idx, appeal in enumerate(appeals):
        if (idx == 0):
            lvl4 = LevelFactory(
                level_name='lvl4',
                appeal=appeal,
                hollistic_appeal=hollistic_appeal)
            status4 = helpers.get_appeal_statuses(StatusFactory, appeal,
                                                  is_open)
            for claim in claims:
                atc4 = AppealToClaimFactory(appeal=appeal, claim=claim)

        elif (idx == 1):
            lvl3 = LevelFactory(
                level_name='lvl3',
                appeal=appeal,
                hollistic_appeal=hollistic_appeal)
            status3 = helpers.get_appeal_statuses(StatusFactory, appeal,
                                                  is_open)
            for claim in claims:
                atc3 = AppealToClaimFactory(appeal=appeal, claim=claim)
        elif (idx > 1 and idx <= (claim_count)):
            lvl2 = LevelFactory(
                level_name='lvl2',
                appeal=appeal,
                hollistic_appeal=hollistic_appeal)
            status2 = helpers.get_appeal_statuses(StatusFactory, appeal,
                                                  is_open)
            atc2 = AppealToClaimFactory(appeal=appeal, claim=claims[idx - 2])
        else:
            lvl1 = LevelFactory(
                level_name='lvl1',
                appeal=appeal,
                hollistic_appeal=hollistic_appeal)
            status1 = helpers.get_appeal_statuses(StatusFactory, appeal,
                                                  is_open)
            atc1 = AppealToClaimFactory(
                appeal=appeal, claim=claims[idx - (claim_count + 2)])


def build_three_level_hollistic_appeal(max_appeals=10, **kwargs):
    total_appeals = helpers.evenify(randrange(3, max_appeals), oddify=True)
    claim_count = int((total_appeals - 1) / 2)
    is_open = kwargs.get('is_open', bool(randint(0, 1)))

    hollistic_appeal = HollisticAppealFactory()
    appellant = AppellantFactory()
    provider = ProviderFactory()
    claims = helpers.save_batch_fixtures(ClaimFactory, claim_count)
    appeals = helpers.save_batch_fixtures(
        AppealFactory,
        total_appeals,
        hollistic_appeal=hollistic_appeal,
        appellant=appellant,
        provider=provider)

    for idx, appeal in enumerate(appeals):
        if (idx == 0):
            lvl3 = LevelFactory(
                level_name='lvl3',
                appeal=appeal,
                hollistic_appeal=hollistic_appeal)
            status3 = helpers.get_appeal_statuses(StatusFactory, appeal,
                                                  is_open)
            for claim in claims:
                atc3 = AppealToClaimFactory(appeal=appeal, claim=claim)
        elif (idx > 0 and idx <= (claim_count)):
            lvl2 = LevelFactory(
                level_name='lvl2',
                appeal=appeal,
                hollistic_appeal=hollistic_appeal)
            status2 = helpers.get_appeal_statuses(StatusFactory, appeal,
                                                  is_open)
            atc2 = AppealToClaimFactory(appeal=appeal, claim=claims[idx - 1])
        else:
            lvl1 = LevelFactory(
                level_name='lvl1',
                appeal=appeal,
                hollistic_appeal=hollistic_appeal)
            status1 = helpers.get_appeal_statuses(StatusFactory, appeal,
                                                  is_open)
            atc1 = AppealToClaimFactory(
                appeal=appeal, claim=claims[idx - (claim_count + 1)])