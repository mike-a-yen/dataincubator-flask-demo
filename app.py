from flask import Flask, render_template, request, redirect
from data_wrangler import Wrangler
from plot_stock_ticker import TickerPlot

from bokeh.resources import CDN
from bokeh.embed import file_html

app = Flask(__name__)
w = Wrangler()

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    form = request.form
    code = form['code']
    print(code)
    options = form.getlist('features')
    print(options)
    return render_template('index.html')
    

@app.route('/stock_ticker',methods=['POST'])
def stock_ticker():
  
  code = request.form.get('code')
  features = request.form.getlist('features')
  print(request.form)
  print(code,features)
  data = w.get(code)[['date']+features]
  print(data)
  tp = TickerPlot(code,data,features)
  html = file_html(tp.figure, CDN, 'Stock Ticker')
  return render_template('stock_ticker.html',
                         plot=html,
                         code=code)
  
if __name__ == '__main__':
  import os
  port = int(os.environ.get('PORT',5000))
  app.run(host='0.0.0.0', port=port)
