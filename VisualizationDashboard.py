# Import libraries

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load dataset

df_ucf = pd.read_feather('UCF_Data_clean.ft')
df_ucf_electricity = df_ucf[df_ucf['meter'] == 0]
df_ucf_chiller = df_ucf[df_ucf['meter'] == 1]

# Create Dash app

app = dash.Dash()

# Define dropdown labels

dropdown_labels = df_ucf['building_id'].unique()

# Set up the app layout

app.layout = html.Div(children=[
    html.H1(children='UCF building meter reading'),
    dcc.Dropdown(id='building-dropdown',
                 options=[{'label': i, 'value': i}
                          for i in dropdown_labels],
                 value='Buildings'),
    dcc.Graph(id='consumption-graph')
])

# Set up callback function

@app.callback(
    Output(component_id='consumption-graph', component_property='figure'),
    Input(component_id='building-dropdown', component_property='value')
)
def update_graph(selected_building):
    filtered_building = df_ucf_electricity[df_ucf_electricity['building_id'] == selected_building]
    line_fig = px.line(filtered_building,
                       x='timestamp', y='meter_reading',
                       title=f'Meter readings in {selected_building}')
    return line_fig


# Run local server
if __name__ == '__main__':
    app.run_server(debug=True)