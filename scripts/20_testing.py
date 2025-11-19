"""Contents: Exceptions (Assert, Try/Except/Finally), Date/Time, Speed, Space, Logging."""

import calendar as cal
import cProfile
import sys
import time
from datetime import datetime as dt

# Extras:
# import logging          # structured logs
# import pytz             # timezone handling
# import unittest         # built-in testing
# import pytest           # pytest style
# from pprint import pprint      # debug print
# from time import perf_counter  # high-res timing


# =================================================================================================
def fact(x):
    """Test function."""
    if x > 0:  # ideally, x > 1
        return x * fact(x - 1)
    else:  # base case
        return 1


# Define a test class too.


# =================================================================================================
# Assert:
assert fact(5 < 3, "5 is not smaller!")  # assertion error

# -------------------------------------------------------------------------------------------------
# Try/Except: Catching Traceback Errors, used around dangerous fragments
try:  # if try works, except part is skipped
    ch = "a"
    print(int(ch))  # = error, can't cast
    pass

except ValueError:  # executed if try fails
    print("ValueError")
    ch_no = ord(ch)
    print(int(ch_no))  # = 97
    pass

except (TypeError, ZeroDivisionError):  # to handle multiple exceptions
    print("TypeError and ZeroDivisionError")
    pass
# except:  # to handle all other exceptions --> don't use it bare beacuse it also traps
# KeyboardInterrupt and SystemExit, making debugging and termination harder.


# -------------------------------------------------------------------------------------------------
# Date:
ticks = time.time()  # secs since epoch(Jan 1st 1970)
dt.fromtimestamp(ticks)  # calculate date from seconds

time.asctime(time.gmtime(ticks))  # = 'Thu Jul 21 19:19:01 2022, 24char readable format
time.ctime(ticks)  # = 'Thu Jul 21 19:19:01 2022', same thing in local time
time.localtime()  # returns tuple of everything:  tm_year=2022, tm_mon=7,
# tm_mday=21, tm_hour=20, tm_min=13, tm_sec=1, tm_wday=3, tm_yday=202, tm_isdst=0
# tm.tzset()                            # sets timezone for libs, dangerous
time.timezone
time.sleep(5)  # suspends the calling thread for n secs
[dt.min, dt.max]  # = 0001-01-01 9999-12-31, timer can work till 2038
dt(1997, 4, 1)  # = 1997-04-01, prints given Y/M/D in yyyy-mm-dd)
dt.today()  # get current date
dt.today().day  # = 22

date_local = dt.now()  # local dt object
tz_london = time.timezone("Europe/London")
dt_london = dt.now(tz_london)  # London dt object

# -------------------------------------------------------------------------------------------------
# Calendar
cal.calendar(2022, 2, 1, 6)  # syntax: (year, width, spacing, col seperators)
cal.month(2022, 9, 4, 1)  # syntax: (year, month, width, spacing)
cal.firstweekday()  # = 0, (Monday, by default) --> can setfirstweekday(n)
cal.isleap(2022)  # = False, year with short (29day) Feb
cal.leapdays(2022, 2030)  # = 2
cal.weekday(2022, 7, 21)  # = 3 (Thu)
cal.monthcalendar(2022, 9)  # = [[0, 0, 0, 1, 2, 3, 4], [5, 6, ...
cal.monthrange(2022, 9)  # = (3, 30), returns tuple

# -------------------------------------------------------------------------------------------------
# Time:
print(time())  # = 00:00:00
print(time(18, 6, 15))  # = 18:06:15, leading zeros  not permitted

dt1 = dt(2017, 11, 28, 23, 0, 0)  # = 2017-11-28 23:00:05, when printed
dt2 = dt(2022, 8, 22, 0, 30, 0)  # = 2017-11-28 23:00:05, //
delta_dt = dt2 - dt1  # becomes a timedelta object
print(delta_dt, type(delta_dt))  # = 1727 days, 1:30:00 <class 'datetime.timedelta'>
delta_dt.total_seconds()  # = 149218200.0

dt2f = dt2.strftime("%d/%m/%Y, %H:%M:%S")  # = '22/08/2022, 00:30:00', to str, order changed
dt2 = dt.strptime("22/08/2022", "%d/%m/%Y")  #  = create dt object from str
print(dt2)  # = 2022-08-22 00:00:00


# -------------------------------------------------------------------------------------------------
# Speed:
t1 = time.time()
fact(10)
t2 = time.time()
fact(30)
t3 = time.time()
te1 = t2 - t1  # time elapsed for first block
te2 = t3 - t2  #
print(f"te1 = {te1 * 1e6:.1f} usecs")  # te1 = 7 usecs
print(f"te2 = {te2 * 1e6:.1f} usecs")  # te2 = 12 usecs

cProfile.run("fact(30)")  # = 34 func calls (4 primitive calls) in 0.001 secs


# -------------------------------------------------------------------------------------------------
# Space:
sys.getsizeof({"I": 1, "V": 5})
