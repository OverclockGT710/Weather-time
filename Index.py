from App import app
from App import server
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from src.navbar import navbar
from src.Dataservice import get_data

df = get_data()

print(df.head())

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

app.layout = html.Div(children=[
    html.Div(navbar),
])

if __name__ == "__main__":
    app.run_server(debug=True)
