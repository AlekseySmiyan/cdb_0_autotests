def get_date(date):
    return date.split('T')[0]


def get_time(date):
    return date.split('T')[1]


def get_hour(date):
    return get_time(date).split(':')[0]


def get_minutes(date):
    return get_time(date).split(':')[1]

