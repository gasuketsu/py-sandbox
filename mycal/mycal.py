#!/usr/bin/env python3

import datetime
import calendar
calendar.setfirstweekday(calendar.SUNDAY)


def print_calendar_header(year, month):
    weekdays = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    print('%d/%d' % (year, month))
    print(' '.join(weekdays))


def print_calendar_body(year, month):
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        datelist = []
        for date in week:
            datestr = '{0:>2}'.format(date) if date != 0 else '  '
            datelist.append(datestr)
        print(' '.join(datelist))


if __name__ == '__main__':
    buf = input()
    ym = list(map(int, buf.split('-')))

    print_calendar_header(ym[0], ym[1])
    print_calendar_body(ym[0], ym[1])
