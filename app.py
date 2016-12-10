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
    

@app.route('/stock_ticker/<code>')
def stock_ticker(code):
  data = w.get(code)
  tp = TickerPlot(code,data['date'],data['price'])
  html = file_html(tp.figure, CDN, 'Stock Ticker')
  return render_template('stock_ticker.html',
                         plot=html)
  
if __name__ == '__main__':
  app.run(port=33507)
