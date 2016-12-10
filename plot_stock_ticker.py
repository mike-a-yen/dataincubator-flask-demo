from bokeh.plotting import figure, output_file, show

class TickerPlot(object):
    TOOLS="""hover,crosshair,pan,wheel_zoom,
    box_zoom,undo,reset,box_select,poly_select,
    lasso_select,"""
    
    def __init__(self,code,dates,prices):
        self.code = code
        self.figure = figure(title='{code} Prices'.format(**{'code':code}),
                             x_axis_label='Date',
                             x_axis_type='datetime',
                             y_axis_label='Price',
                             tools=self.TOOLS)

        self.figure.line(dates,prices,line_width=2)

        
            

