import datetime
import pytz
from statistics import mean
from django.db.models import Count, Max, Min, Q
from medicare_appeals.appeals import models
from medicare_appeals.appeals import schema


def format_overview_response(results=schema.dashboard()):
    output = []

    for level, racs in results.items():
        level_number = int(level.split()[1])
        for rac, counts in racs.items():
            sub_item = {}
            sub_item['level'] = level_number
            sub_item['denial_category'] = rac
            sub_item.update(counts)
            output.append(sub_item)

    return output


def get_receipt_dispositions(start=None, end=None, results=schema.dashboard()):
    appeal_status = models.Appeal.objects.values(
        'id', 'level__level_name','status__category', 'rac').order_by(
            'id','-status__created_at'
                )

    if start and end:
        try:
            s_year, s_month, s_day = start.split('-')
            e_year, e_month, e_day = end.split('-')
            start_date = datetime.datetime(int(s_year), int(s_month), int(s_day), tzinfo=pytz.UTC)
            end_date = datetime.datetime(int(e_year), int(e_month), int(e_day), tzinfo=pytz.UTC)

            appeal_status = appeal_status.filter(
                status__created_at__range=(
                    start_date,
                    end_date
                ))
        except Exception as e:
            print(f'{e}')
            pass

    for item in appeal_status:
        rac = 'rac'

        if item['rac'] == False:
            rac = 'non-rac'

        if item['status__category'] == 'Closed':
            results[item['level__level_name']][rac]['dispositions'] = results.get(
                item['level__level_name'], {}).get(rac).get('dispositions', 0) + 1
        else:
            results[item['level__level_name']][rac]['receipts'] = results.get(
                item['level__level_name'], {}).get(rac).get('receipts', 0) + 1

    return results


def get_work_in_progress(end=None, results=schema.dashboard()):
    appeal_status = models.Appeal.objects.values(
        'id', 'level__level_name','status__category', 'rac').order_by(
            'id','-status__created_at'
                ).distinct('id')
    if end:
        try:
            e_year, e_month, e_day = end.split('-')
            end_date = datetime.datetime(int(e_year), int(e_month), int(e_day), tzinfo=pytz.UTC)

            appeal_status = appeal_status.filter(status__created_at__lte=end_date)

        except Exception as e:
            print(f'{e}')
            pass

    for item in appeal_status:
        rac = 'rac'

        if item['rac'] == False:
            rac = 'non-rac'

        if item['status__category'] == 'Open':
            results[item['level__level_name']][rac]['work_in_progress'] = results.get(
                item['level__level_name'], {}).get(rac).get('work_in_progress', 0) + 1

    return results


def get_average_days(start=None, end=None, results=schema.dashboard()):
    total_days = schema.total_days()
    appeal_status = models.Appeal.objects.values(
        'id', 'level__level_name', 'rac').order_by(
            'id').annotate(
                closed_date=Max('status__created_at'),
                days=(Max('status__created_at') - Min('status__created_at')),
                status_count=Count('status__created_at')
            ).filter(status_count=2)

    if start and end:
        try:
            s_year, s_month, s_day = start.split('-')
            e_year, e_month, e_day = end.split('-')
            start_date = datetime.datetime(int(s_year), int(s_month), int(s_day), tzinfo=pytz.UTC)
            end_date = datetime.datetime(int(e_year), int(e_month), int(e_day), tzinfo=pytz.UTC)

            appeal_status = appeal_status.filter(
                closed_date__range=(
                    start_date,
                    end_date
                ))

        except Exception as e:
            print(f'{e}')
            pass

    for item in appeal_status:
        rac = 'rac'

        if item['rac'] == False:
            rac = 'non-rac'

            total_days.get(
                item['level__level_name']).get(rac).get('days').append(
                    item['days'].days)


    for level, racs in results.items():
        for rac, values in racs.items():
            if len(total_days[level][rac]['days']) == 0:
                results[level][rac]['days'] = int(0)
            else:
                extract_zeroes = list(filter(lambda a: a != 0, total_days[level][rac]['days']))
                results[level][rac]['days'] = int(mean(extract_zeroes))

    return results


def get_overturn_rates(start=None, end=None, results=schema.dashboard()):
    s_year, s_month, s_day = start.split('-')
    e_year, e_month, e_day = end.split('-')
    start_date = datetime.datetime(int(s_year), int(s_month), int(s_day), tzinfo=pytz.UTC)
    end_date = datetime.datetime(int(e_year), int(e_month), int(e_day), tzinfo=pytz.UTC)

    total_appeals = models.Appeal.objects.values('level__level_name','rac').filter(
            status__category='Closed',
            status__created_at__range=(start_date, end_date)).annotate(count=Count('id'))

    appeal_closed_actions = models.Appeal.objects.values(
        'level__level_name','rac', 'status__action').filter(
            status__category='Closed',
            status__action='Unfavorable',
            status__created_at__range=(start_date, end_date)).annotate(count=Count('id'))

    # for t in total_appeals:
    #     print(t)

    # for a in appeal_closed_actions:
    #     print(a)

def get_overview(start=None, end=None, results=schema.dashboard()):
    receipts_dispositions = get_receipt_dispositions(start, end, results)
    work_in_progress = get_work_in_progress(end, results)
    average_days = get_average_days(start, end, results)
    overturn = get_overturn_rates(start, end, results)
    output = format_overview_response(average_days)
    return output
