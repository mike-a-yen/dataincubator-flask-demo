from bokeh.plotting import figure, output_file, show

class TickerPlot(object):
    TOOLS="""hover,crosshair,pan,wheel_zoom,
    box_zoom,undo,reset,box_select,poly_select,
    lasso_select,"""
    
    def __init__(self,code,data,features,label=None):
        self.code = code
        self.dates = data['date']
        
        self.figure = figure(title='{code} Prices'.format(**{'code':code}),
                             x_axis_label='Date',
                             x_axis_type='datetime',
                             y_axis_label='Price',
                             tools=self.TOOLS)
        colors = {'open':'blue',
                  'adj_open':'green',
                  'close':'red',
                  'adj_close':'orange'}
        for feature in features:
            self.figure.line(self.dates,data[feature],
                             line_width=2,
                             line_color=colors[feature],
                             legend=feature)

        
            

