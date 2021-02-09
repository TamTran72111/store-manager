from datetime import timedelta
from django.conf import settings
from django.utils import timezone
import pytz


def get_local_time_today_start():
    local = pytz.timezone(settings.TIME_ZONE)
    local_time = local.localize(timezone.now())
    delta = timedelta(hours=local_time.hour,
                      minutes=local_time.minute,
                      seconds=local_time.second,
                      microseconds=local_time.microsecond)
    local_time -= delta
    return local_time.astimezone(pytz.utc)


def datetime_filter(queryset, query):
    # Filter by sever local time
    time = query.get('time')
    if time is None:
        return queryset

    today_start = get_local_time_today_start()
    if time == 'today':
        query.filter(created_at__gte=today_start)
    elif time == 'ago':

        return None
