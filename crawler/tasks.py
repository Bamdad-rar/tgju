from stockCollector import tgju,db
from datetime import datetime
from stockCollector.models import Stock
from pytz import utc
'''
get_tgju_stock gets latest stock info and adds them to the database
this function is done at a 30 second interval using apscheduler
'''
def get_tgju_stock():
    t = utc.localize(datetime.now())
    if 9<=t.hour<17:
        data = tgju.get_info()
        d =Stock(name='dollar',price=int(data["dollar"].replace(',','')),time=t)
        e =Stock(name='euro',price=int(data["euro"].replace(',','')),time=t)
        db.session.add(d)
        db.session.add(e)
        db.session.commit()
    