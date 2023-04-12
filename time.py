import time
import random
from datetime import datetime, timedelta


now_tm = time.gmtime()

# print(
#     f"Evenimentul s-a intamplat in anul {now_tm.tm_year}, luna {now_tm.tm_mon}, ziua {now_tm.tm_mday}, ora {now_tm.tm_hour}:{now_tm.tm_min}.")

# print(time.strftime("%d %B %Y %H:%M", now_tm))

event_time = "12 April 2023 16:47"
ev_tm = time.strptime(event_time, "%d %B %Y %H:%M")

ev1 = "20-02-2023 10:11"
ev2 = "22-02-2023 12:45"

ev1_tm = time.strptime(ev1, "%d-%m-%Y %H:%M")
ev2_tm = time.strptime(ev2, "%d-%m-%Y %H:%M")

#time.sleep(10) # cate secunde sa stea codul in standby

# print(f"Cele doua evenimente s-au intamplat la o distanta de {ev2_tm.tm_year - ev1_tm.tm_year} ani, {ev2_tm.tm_mon - ev1_tm.tm_mon} luni, {ev2_tm.tm_mday - ev1_tm.tm_mday} zile, {ev2_tm.tm_hour - ev1_tm.tm_hour} ore, {ev2_tm.tm_min - ev1_tm.tm_min} minute")

# print(f"Intre cele doua evenimente a trecut {(ev2_tm.tm_year - ev1_tm.tm_year) * 525948 + (ev2_tm.tm_mon - ev1_tm.tm_mon) * 43829 + (ev2_tm.tm_mday - ev1_tm.tm_mday) * 1440 + (ev2_tm.tm_hour - ev1_tm.tm_hour) * 60 + (ev2_tm.tm_hour - ev1_tm.tm_hour)} minute.")

now = datetime.now()
# print(now.strftime("%A, %d-%m-%Y %H:%M"))


ev1 = datetime(1988, 6, 27)
print(ev1.strftime("%A"))
delta = now - ev1
print(delta.total_seconds())