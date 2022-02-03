from stockCollector import tgju,db
from datetime import datetime
from stockCollector.models import Stock

def get_tgju_stock():
    data = tgju.get_info()
    d =Stock(name='dollar',price=int(data["dollar"].replace(',','')),time=datetime.utcnow())
    e =Stock(name='euro',price=int(data["euro"].replace(',','')),time=datetime.utcnow())
    db.session.add(d)
    db.session.add(e)
    db.session.commit()
   

