# visualize_data.py

import plotly.graph_objs as go
import pandas as pd

# Sample data (replace this with your actual dataset)
data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-01-10'),
    'Temperature': [25, 28, 24, 26, 27, 29, 23, 25, 28, 30],
    'Humidity': [40, 45, 38, 42, 50, 55, 37, 39, 42, 48],
    'City': ['City A']*5 + ['City B']*5
}

df = pd.DataFrame(data)

# Create traces for temperature and humidity
trace_temperature = go.Scatter(x=df['Date'], y=df['Temperature'], mode='lines', name='Temperature', line=dict(color='red'))
trace_humidity = go.Scatter(x=df['Date'], y=df['Humidity'], mode='lines', name='Humidity', line=dict(color='blue'))

# Create layout
layout = go.Layout(
    title='Temperature and Humidity Trends Over Time',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Value'),
    legend=dict(title='City'),
    template='plotly_dark'
)

# Create figure
fig = go.Figure(data=[trace_temperature, trace_humidity], layout=layout)

# Save the visualization as an HTML file
fig.write_html('temperature_humidity_visualization.html')

# Show the visualization (opens in a new browser window)
fig.show()
