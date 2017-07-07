import time

from uuid import uuid4

bool_dict = {
    'true': True,
    'false': False,
}


def timestamp():
    return int(time.time())


def time_str(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(int(t) + 3600 * 8))


def short_uuid():
    seed = str(uuid4())
    short_seed = seed.split('-')[-1]
    return short_seed


def safe_list_get(l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default


def timestamp_today():
    import datetime
    start_dt = datetime.datetime.combine(datetime.date.today(), datetime.time.min).timetuple()
    start = int(time.mktime(start_dt))
    end_dt = datetime.datetime.combine(datetime.date.today(), datetime.time.max).timetuple()
    end = int(time.mktime(end_dt))
    return start, end
