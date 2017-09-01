import datetime
import os

t_date = datetime.datetime.now()
current_time = t_date.strftime("%H:%M:%S")

os.system('sed -e %s  > led_log5.txt' %current_time)
