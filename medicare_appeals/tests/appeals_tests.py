import pytest
from medicare_appeals.appeals.models import Appeal, Appellant, Claim, History, Level, Provider, Status


@pytest.mark.django_db
def test_appeals():
    a = Appeal()
    a.save()
    assert Appeal.objects.count() == 1


@pytest.mark.django_db
def test_appellants():
    a = Appellant()
    a.save()
    assert Appellant.objects.count() == 1


@pytest.mark.django_db
def test_claims():
    a = Claim()
    a.save()
    assert Claim.objects.count() == 1


@pytest.mark.django_db
def test_histories():
    a = History()
    a.save()
    assert History.objects.count() == 1


@pytest.mark.django_db
def test_levels():
    a = Level()
    a.save()
    assert Level.objects.count() == 1


@pytest.mark.django_db
def test_providers():
    a = Provider()
    a.save()
    assert Provider.objects.count() == 1


@pytest.mark.django_db
def test_statuses():
    a = Status()
    a.save()
    assert Status.objects.count() == 1
