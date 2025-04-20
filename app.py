import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

from sabia.layout import Container, Row, Col
from sabia.dashboard import Dashboard

from sabia.engine import EngineFactory

# 1. Generate Fake Data
np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_data = pd.DataFrame({
    'Month': months,
    'Revenue': np.random.randint(100, 500, 6),
    'Customers': np.random.randint(50, 200, 6),
    'Product': np.random.choice(['A', 'B', 'C'], 6)
})

# 2. Create Figures with Plotly Express
line_fig = px.line(
    sales_data, 
    x='Month', 
    y='Customers',
    title='Customer Trends'
).update_layout(margin=dict(t=30, b=10))

bar_fig = px.bar(
    sales_data,
    x='Month',
    y='Revenue',
    color='Product',
    title='Revenue by Product',
    barmode='stack'
).update_layout(margin=dict(t=30, b=10))


dashboard = Dashboard(title="Sales Dashboard", subtitle="Monthly Sales Overview")
dashboard.add_container(
    Container([
        # Row 1: Charts
        Row([
            Col([dcc.Graph(figure=line_fig)]),  # Auto width
            Col([dcc.Graph(figure=bar_fig)], width=6),   # Auto width
            Col([dcc.Graph(figure=bar_fig)]),   # Auto width
        ]),
    ]))
    

# dashboard.add_container(
#     Container([
#         # Row 2: KPIs
#         Row([
#             Col(dbc.Card([
#                 dbc.CardBody([
#                     html.H5("Total Revenue", className="card-title"),
#                     html.H2(f"${sales_data['Revenue'].sum():,}", className="card-text"),
#                     html.Span("↑8.5%", className="text-success ml-2")
#                 ])
#             ], color="primary", inverse=True)),
            
#             Col(dbc.Card([
#                 dbc.CardBody([
#                     html.H5("Avg Customers", className="card-title"),
#                     html.H2(f"{sales_data['Customers'].mean():.0f}", className="card-text"),
#                     html.Span("↓2.1%", className="text-danger ml-2")
#                 ])
#             ], color="secondary", inverse=True))
#         ]),
        
#         # Row 3: Table
#         Row([
#             Col(dbc.Card([
#                 dbc.CardHeader("Sales Data"),
#                 dbc.Table.from_dataframe(
#                     sales_data,
#                     striped=True,
#                     bordered=True,
#                     hover=True
#                 )
#             ]))
#         ])
#     ])
# )

dash_engine = EngineFactory.create_engine('dash')
app = dash_engine.render(dashboard)

if __name__ == '__main__':
    app.run(port=8050, debug=True)