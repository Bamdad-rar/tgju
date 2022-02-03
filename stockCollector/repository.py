from stockCollector.models import Stock

'''
functions to get appropriate data for api calls
'''

def get_current_usd():
    temp = Stock.query.filter_by(name='dollar').order_by(Stock.time.desc()).first()
    return {'price':temp.price,'time':temp.time}

def get_current_eur():
    temp = Stock.query.filter_by(name='euro').order_by(Stock.time.desc()).first()
    return {'price':temp.price,'time':temp.time}

def get_usd(pagination=None):
    return [{"price":item.price,"time":item.time} for item in Stock.query.filter_by(name='dollar').order_by(Stock.time.desc()).limit(pagination)]

def get_eur(pagination=None):
    return [{"price":item.price,"time":item.time} for item in Stock.query.filter_by(name='euro').order_by(Stock.time.desc()).limit(pagination)]

def get_usd_eur_ratio(pagination=None):
    d = [{"price":item.price,"time":item.time} for item in Stock.query.filter_by(name='dollar').order_by(Stock.time.desc()).limit(pagination)]
    e = [{"price":item.price,"time":item.time} for item in Stock.query.filter_by(name='euro').order_by(Stock.time.desc()).limit(pagination)]
    res = []
    for x,y in zip(d,e):
        try:
            ratio = round(x["price"]/y["price"],3)
        except:
            ratio = "N/A"
        res.append({'ratio':ratio,'time':x["time"]})
    return {'data':res}