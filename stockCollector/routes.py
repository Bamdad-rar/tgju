from stockCollector import app
from stockCollector.repository import get_current_usd,get_current_eur,get_usd,get_eur,get_usd_eur_ratio
from flask import request
'''
could be seperated with blueprints but meh
- /current/usd
- /current/euro
- /history/usd 
- /history/euro 
- /history/ratio 
'''

@app.route('/current/usd',methods=['GET'])
def current_usd():
    return get_current_usd()

@app.route('/current/euro',methods=['GET'])
def current_euro():
    return get_current_eur()

@app.route('/history/usd',methods=['GET'])
def history_usd():
    if request.args.get("quantity"):
        data = get_usd(request.args.get("quantity"))
    else:
        data = get_usd()
    return {'data':data}

@app.route('/history/euro',methods=['GET'])
def history_euro():
    if request.args.get("quantity"):
        data = get_usd(request.args.get("quantity"))
    else:
        data =get_eur()
    return {'data':data}


@app.route('/history/ratio',methods=['GET'])
def history_ratio():
    if request.args.get("quantity"):
        data = get_usd_eur_ratio(request.args.get("quantity"))
    else:
        data =get_usd_eur_ratio()
    return {'data':data}

