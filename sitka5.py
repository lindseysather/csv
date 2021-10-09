import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file_dv = open("death_valley_2018_simple.csv", "r")
open_file_s = open("sitka_weather_2018_simple.csv", "r")

csv_file_dv = csv.reader(open_file_s,delimiter=',')
csv_file_s = csv.reader(open_file_dv,delimiter=',')

header_row_d = next(csv_file_dv)
header_row_s = next(csv_file_s)


highs_d = []
lows_d = []
dates_d = []

high_index = header_row_d.index('TMAX')
low_index = header_row_d.index('TMIN')
title_index = header_row_d.index('NAME')
date_index = header_row_d.index('DATE')

for rec in csv_file_dv:
    try:
        the_date = datetime.strptime(rec[date_index], '%Y-%m-%d')
        high = int(rec[high_index])
        low = int(rec[low_index])
        title_name_d = rec[title_index]
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs_d.append(high)
        lows_d.append(low)
        dates_d.append(the_date)



highs_s = []
lows_s = []
dates_s = []

high_index = header_row_s.index('TMAX')
low_index = header_row_s.index('TMIN')
title_index = header_row_s.index('NAME')
date_index = header_row_s.index('DATE')


for rec in csv_file_s:
    try:
        the_date = datetime.strptime(rec[date_index], '%Y-%m-%d')
        high = int(rec[high_index])
        low = int(rec[low_index])
        title_name_s = rec[title_index]
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs_s.append(high)
        lows_s.append(low)
        dates_s.append(the_date)

fig = plt.figure()

plt.subplot(2,1,1)
plt.plot(dates_s,highs_s,c='red', alpha=0.5)
plt.plot(dates_s,lows_s,c="blue", alpha=0.5)
plt.title(title_name_s)
plt.tick_params(axis="both",which="major",labelsize=12)
plt.fill_between(dates_s,highs_s,lows_s,facecolor='blue',alpha=0.1)

plt.subplot(2,1,2)
plt.plot(dates_d,highs_d,c='red', alpha=0.5)
plt.plot(dates_d,lows_d,c="blue", alpha=0.5)
plt.title(title_name_d)
plt.tick_params(axis="both",which="major",labelsize=12)
plt.fill_between(dates_d,highs_d,lows_d,facecolor='blue',alpha=0.1)

fig.autofmt_xdate()
plt.suptitle(f"Temperature comparison between {title_name_s} and {title_name_d}")

plt.show()