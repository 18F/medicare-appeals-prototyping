from random import randrange, random


def evenify(num, oddify=False):
    """
    Make sure an int is even... or false

    returns: type int
    """
    if oddify:
        remainder = 1
    else:
        remainder = 0

    if num % 2 == remainder:
        return num
    else:
        return num + 1


def get_reviewer_type(level):
    """
    Creates the type of reviewer based on the level

    returns: type string
    """
    if level == 'lvl1' or level == 'lvl2':
        return 'contractor'
    else:
        return 'federal employee'


def get_appeal_statuses(factory, appeal, is_open):
    """
    Create statuses for an appeal

    returns: type string
    """
    statuses = list()

    if is_open:
        status_count = randrange(2, 4)
    else:
        status_count = randrange(3, 5)

    for idx in range(0, status_count):
        if (idx == 0):
            status = factory(
                appeal=appeal, category='Received', action='Appeal Filed')
        elif idx > 0 and idx < (status_count - 1):
            status = factory(appeal=appeal, category='Open')
        else:
            if is_open:
                status = factory(appeal=appeal, category='Open')
            else:
                status = factory(
                    appeal=appeal, category='Closed', action='Decision')

        statuses.append(status)

    return statuses


def random_amount_billed():
    """
    Generates a random amount billed.

    returns: type float
    """
    return round(float(randrange(6000, 100000) / 100), 2)


def random_amount_paid(amount_billed):
    """
    Generates a random amount paid based on the amount_billed passed to the function

    returns: type float
    """
    return round(float(amount_billed) * random(), 2)


def calc_controversy(amount_billed, amount_paid):
    """
    Calculates the amount of money in controversy based on the amount_billed and amount_paid passed to the function

    returns: type float
    """
    return round(float(amount_billed) - float(amount_paid), 2)


def save_batch_fixtures(factory, count, **kwargs):
    """
    Build and save a factory batch

    returns: type list
    """
    fixtures = factory.build_batch(count, **kwargs)

    for fixture in fixtures:
        fixture.save()

    return fixtures
