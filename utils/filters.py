from datetime import timedelta, datetime
from django.conf import settings
from django.utils import timezone
import pytz


def get_local_start_time(time):
    local = pytz.timezone(settings.TIME_ZONE)
    try:
        local_time = local.localize(time)
    except ValueError:
        local_time = time
    delta = timedelta(hours=local_time.hour,
                      minutes=local_time.minute,
                      seconds=local_time.second,
                      microseconds=local_time.microsecond)
    local_time -= delta
    return local_time.astimezone(pytz.utc)


def get_local_time_today_start(time=None):
    return get_local_start_time(timezone.now())


def get_period_boundary(query_params, key):
    value = query_params.get(key, '')
    try:
        value = datetime.strptime(value, '%Y-%m-%d')
        value = value.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))
    except ValueError:
        value = get_local_time_today_start()
    return value


def datetime_filter(query_params, queryset):
    # Filter by sever local time
    time = query_params.get('time')
    if time is None:
        return queryset

    start = None
    end = None

    if time == 'period':
        start = get_period_boundary(query_params, 'from')
        end = get_period_boundary(query_params, 'to') + timedelta(days=1)
    elif time == 'days':
        start = get_local_time_today_start()
        days = int(query_params.get('days', 0))
        start -= timedelta(days=days)

    if start:
        queryset = queryset.filter(created_at__gte=start)

    if end:
        queryset = queryset.filter(created_at__lt=end)

    return queryset
