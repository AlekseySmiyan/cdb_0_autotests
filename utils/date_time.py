from datetime import datetime, timedelta
from pytz import timezone
import dateutil.parser


def create_date(**kwargs):
    """param:
    days, seconds, microseconds, milliseconds, minutes, hours, weeks"""
    now = datetime.now() + timedelta(**kwargs)
    time_zone = timezone('Europe/Kiev')
    local_date = time_zone.localize(now)
    just_time = local_date.strftime('%Y-%m-%dT%H:%M:%S')
    time_zone = local_date.strftime('%z')
    if len(time_zone) > 4:
        time_zone = time_zone[0:3] + ':' + time_zone[3:]
    return just_time + time_zone


def date_now_format(str_format):
    date = datetime.now()
    return date.strftime(str_format)


def adapt_date(date, str_format):
    parse_date = dateutil.parser.parse(date)
    date = parse_date.strftime(str_format)
    return date


