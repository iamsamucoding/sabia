from vizlib import Dashboard, Container, Row, Column
from vizlib.components.charts import BarChart
from vizlib.components.tables import Table
from vizlib.translators.dash_translator import DashTranslator

# Create a dashboard
dashboard = Dashboard(title="Sales Dashboard", layout='fluid')

# Add a row with two columns
row = Row()
col1 = Column(span=6)
col2 = Column(span=6)

# Create a bar chart
chart = BarChart(title="Monthly Sales")
chart.add_series({'x': ['Jan', 'Feb', 'Mar'], 'y': [
                 100, 200, 150], 'name': 'Product A'})

# Create a table
table = Table(columns=["Month", "Sales"])
table.add_row(["January", 100])
table.add_row(["February", 200])

# Add components to columns
col1.add_child(chart)
col2.add_child(table)

# Add columns to row and row to dashboard
row.add_column(col1).add_column(col2)
dashboard.container.add_child(row)

# Translate to Dash app
app = DashTranslator.translate_dashboard(dashboard)
app.run(debug=True)
