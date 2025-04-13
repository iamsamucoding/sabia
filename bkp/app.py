from vizlib import Dashboard, Container, Row, Col
from vizlib.components.charts import BarChart, LineChart
from vizlib.components.tables import Table
from vizlib.translators.dash_translator import DashTranslator

# Create a dashboard
dashboard = Dashboard(title="Sales Dashboard")

cont = Container()
cont.add_child(
    Row(cols=[
        Col(span=6).add_child(BarChart(title="Monthly Sales").add_series({'x': ['Jan', 'Feb', 'Mar'], 'y': [100, 200, 150], 'name': 'Product A'})),
        Col(span=6).add_child(LineChart(title="Monthly Sales").add_series({'x': ['Jan', 'Feb', 'Mar'], 'y': [100, 200, 150], 'name': 'Product A'}))
    ])
)
print(len(cont.children))
print(len(cont.children[0].cols))

# Add the container to the dashboard
dashboard.add_container(cont)
# Set the theme
dashboard.set_theme("dark")
# Translate to Dash app
app = DashTranslator.translate_dashboard(dashboard)
# Run the app
if __name__ == "__main__":
    app.run(debug=True)


# # Add a row with two Cols
# row = Row()
# col1 = Col(span=6)
# col2 = Col(span=6)

# # Create a bar chart
# chart = BarChart(title="Monthly Sales")
# chart.add_series({'x': ['Jan', 'Feb', 'Mar'], 'y': [
#                  100, 200, 150], 'name': 'Product A'})

# # Create a table
# table = Table(Cols=["Month", "Sales"])
# table.add_row(["January", 100])
# table.add_row(["February", 200])

# # Add components to Cols
# col1.add_child(chart)
# col2.add_child(table)

# # Add Cols to row and row to dashboard
# row.add_Col(col1).add_Col(col2)
# dashboard.container.add_child(row)

# # Translate to Dash app
# app = DashTranslator.translate_dashboard(dashboard)
# app.run(debug=True)
