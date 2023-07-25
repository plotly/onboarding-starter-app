### This is a basic Dash App! ###


### IMPORTING DEPENDENCIES ###

# Comments are throughout to highlight what each part of the code does
# Feel free to make changes and see how you're changes affect the app

# First, importing the necssary dependencies. This app only uses open source packages.

import dash
import plotly
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State

# Dash Maintine Components is an open source library that has some really great Dash components!
# https://www.dash-mantine-components.com/
import dash_mantine_components as dmc
import pandas as pd

### READING IN DATA ###

# Here we are reading in the data.
# This dataset comes with Plotly Express and is small, so we can easily load it in from the start.
# Try loading in your own data here!
# You could query a database using your normal python packages to do so and then convert to a pandas dataframe
gap_data = px.data.gapminder()

# Here, grabbing the unique continent names from the dataset
# This will be used in a dropdown later in the app
# https://dash.plotly.com/dash-core-components/dropdown
continents = [x for x in gap_data["continent"].unique()]

# Initializing the app object:
app = dash.Dash(__name__)

# Exposing the server variable.
# This step is important for deployment. We refer to this variable in the Procfile
server = app.server

### APP LAYOUT ###

# Lines 46 to 61 establish the layout of the app, what it will look like when it renders
# Checkout this section of the documentation for more information:
# https://dash.plotly.com/layout
app.layout = html.Div(
    [
        dmc.Header(
            height=60,
            children=[dmc.Text("Life Expectancy of Countries per Continents")],
        ),
        dcc.Graph(id="life-ex-graph"),
        dcc.Dropdown(
            id="continent-select", options=continents, value=["Oceania"], multi=True
        ),
        # uncomment lines 57 to 59 and 88 to 92 of code to see what happens in the app!
        # html.H3("What is your favorite color?"),
        # dcc.Input(id="favorite_color_input"),
        # html.Div(id="user_fav_color"),
    ]
)

### CALLBACKS ###

# Here are the callbacks! This is where we can customize the interactivity of an application
# Essentially, a callback is a regular python function and the callback tells dash when it should be called
# via the Input and where the retun of that function should go via the Output


# This callback takes in the value the user selects in the dropdown, filters the data, and creates a graph!
@app.callback(
    Output(component_id="life-ex-graph", component_property="figure"),
    Input(component_id="continent-select", component_property="value"),
    prevent_inital_call=True,
)
def update_graph(continent):
    values = gap_data.continent.isin(continent)
    fig = px.line(
        gap_data[values],
        x="year",
        y="lifeExp",
        color="country",
        labels={"year": "Year", "lifeExp": "Life Expectancy"},
    )
    return fig


# @app.callback(
#     Output("user_fav_color", "children"), Input("favorite_color_input", "value")
# )
# def favorite_color(color):
#     return f"Your favorite color is {color}"


if __name__ == "__main__":
    app.run(debug=True)
