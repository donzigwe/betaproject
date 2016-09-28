import datetime
from datetime import timedelta, date
import random
def beta_id():
    date = str(datetime.datetime.now())[2:10]
    date = date.replace('-', '')
    randnum = str(random.random())[4:8]
    id_num = 'BIA' + date + randnum
    return id_num

print beta_id()