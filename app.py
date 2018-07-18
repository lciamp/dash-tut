# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Hello Dash'),

    html.Div(' Dash: A web application framework for Python'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4], 'y': [4, 1, 2, 6], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3, 4], 'y': [2, 4, 5, 2], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)