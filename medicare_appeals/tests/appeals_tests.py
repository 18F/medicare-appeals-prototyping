import pytest
from medicare_appeals.appeals import models
from medicare_appeals.tests import factories


@pytest.fixture(scope='function')
def build_an_appeal():
    """
    Build a single appeal
    """
    appeal = factories.AppealFactory()


@pytest.fixture(scope='function')
def build_two_appeals():
    """
    Build two appeals with the description 'test{n}'
    """
    appeal1 = factories.AppealFactory(description='test0')
    appeal2 = factories.AppealFactory(description='test1')


@pytest.mark.django_db
def test_appeal(build_an_appeal):
    """
    An appeal should be created
    """
    assert models.Appeal.objects.count() == 1


@pytest.mark.django_db
def test_two_appeals(build_two_appeals):
    """
    Two appeals should be created with description 'test{n}'
    """
    appeals = models.Appeal.objects.all()
    assert appeals.count() == 2

    for idx, appeal in enumerate(appeals):
        assert appeal.description == 'test{0}'.format(idx)
