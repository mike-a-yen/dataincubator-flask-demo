import requests
import json
import pandas as pd
from datetime import datetime, timedelta

from keys import quandl_key


quandl_base = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?ticker={code}&date.gt={date}&qopts.columns=date,open&api_key={api_key}'

class Wrangler(object):
    def __init__(self,base=quandl_base,key=quandl_key):
        self.base = base
        self.key = key

    def get(self,code,timediff=timedelta(365)):
        date = self.date(timediff).strftime('%Y%m%d')
        meta = {'code':code,'date':date,'api_key':self.key}
        query_url = self.base.format(**meta)
        page = requests.get(query_url)
        data = json.loads(page.text)
        price_history = self.data_clean(data)
        return price_history

    def date(self,timediff):
        return datetime.now()-timediff
    
    def data_clean(self,data):
        df =  pd.DataFrame(data['datatable']['data'],
                           columns=['date','price'])
        df['date'] = df['date'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d'))
        return df
