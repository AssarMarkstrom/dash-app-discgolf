from dash import Dash, dcc, html
from dash.dependencies import Input, Output

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.I("Search for a player"),
        html.Br(),
        dcc.Input(id="input1", type="text", placeholder="First name", debounce=True, style={'marginRight':'10px'}),
        dcc.Input(id="input2", type="text", placeholder="Last Name", debounce=True),
        html.Div(id="output"),
    ]
)


@app.callback(
    Output("output", "children"),
    Input("input1", "value"),
    Input("input2", "value"),
)
def update_output(input1, input2):
    return u'Input 1 {} and Input 2 {}'.format(input1, input2)


if __name__ == "__main__":
    app.run_server(debug=True)
