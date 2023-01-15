import requests
import json
import datetime
from datetime import datetime as dt
from requests.auth import HTTPBasicAuth
import calendar
from datetime import date

#Your Api Key is Ready!
#Your key: 9581e321-f16b-4136-99dc-ff899182d30f
#Expires on 15/01/2034


def get_data(start = datetime.datetime.now().date(), end = datetime.datetime.now().date(), coin='bitcoin'):
    start_date_object = date.fromisoformat(start)  
    end_date_object = date.fromisoformat(end) 
    from_time_milliseconds = round(calendar.timegm(start_date_object.timetuple())*1000-100000)
    end_time_milliseconds = round(calendar.timegm(end_date_object.timetuple())*1000)
    url = f'http://api.coincap.io/v2/assets/{coin}/history?interval=d1'
    opt = {'start': from_time_milliseconds, 'end': end_time_milliseconds }
    auth = HTTPBasicAuth('apikey', '9581e321-f16b-4136-99dc-ff899182d30f')
    api_response = requests.get(url, auth=auth, params=opt)
    # if api_response.status_code != 200:
    data = api_response.text
    parse_json = json.loads(data)
    # print(parse_json)
    time = []
    price = []
    try:
        if len(parse_json['data']) > 0:
            for i in range(len(parse_json['data'])):
                n = parse_json['data'][i]
                time.append(datetime.datetime.strptime(n['date'][:10], '%Y-%m-%d').date())
                price.append(round(float(n['priceUsd']), 2))
        res = {'time':time, 'price': price}
        return res
    except:
        return print("I can't read data. Mayby smth wrong with name of the coin")

    


# print(get_data(coin='bitcoin'))