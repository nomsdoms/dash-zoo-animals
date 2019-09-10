import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Pick variables
tabtitle='zoo'
myheading = 'Coolest Zoo Animals'
myfavoritecolor='#C62B0A' # More colors are here: https://htmlcolorcodes.com/
x_list=['lions', 'pandas', 'snakes']
y_list=[60, 39, 1]
mytitle='Coolest Animals at the Zoo'
githublink='https://github.com/nomsdoms/dash-zoo-animals'

########### Set up the chart
mydata = [go.Bar(x=x_list,
                y=y_list,
                marker=dict(color=myfavoritecolor))]
mylayout = go.Layout(
    title = mytitle,
    xaxis = dict(title = 'Animals'),
    yaxis = dict(title = 'Votes'))
myfigure = go.Figure(data=mydata, layout=mylayout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Display the chart
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(id='figure-1', figure=myfigure),
    html.A('Code on Github', href=githublink)])

########### Execute your code
if __name__ == '__main__':
    app.run_server()
