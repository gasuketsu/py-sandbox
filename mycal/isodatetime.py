#!/usr/bin/env python3

import datetime


if __name__ == '__main__':
    now = datetime.datetime.now()
    print(now.replace(microsecond=0).isoformat())
