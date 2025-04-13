import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from ..layout import Container, Row, Col
from ..components.charts import Chart
from ..components.tables import Table
import dash

class DashTranslator:
    @staticmethod
    def translate_container(container):
        fluid = container.fluid
        children = [DashTranslator.translate_child(
            child) for child in container.children]
        return dbc.Container(fluid=fluid, children=children)

    @staticmethod
    def translate_row(row):
        justify_map = {
            'start': 'start',
            'center': 'center',
            'end': 'end',
            'between': 'between',
            'around': 'around'
        }
        align_map = {
            'start': 'start',
            'center': 'center',
            'end': 'end'
        }

        justify = justify_map.get(row.justify, 'start')
        align = align_map.get(row.align, 'start')

        return dbc.Row(
            children=[DashTranslator.translate_column(
                col) for col in row.cols],
            justify=justify,
            align=align
        )

    @staticmethod
    def translate_column(column):
        # Map span values to Bootstrap classes
        col_class = f"col-{column.span}"

        return dbc.Col(
            children=[DashTranslator.translate_child(
                child) for child in column.children],
            className=col_class
        )

    @staticmethod
    def translate_chart(chart):
        """Simple chart translation to Dash components"""
        if isinstance(chart, BarChart):
            return DashTranslator._translate_bar(chart)
        # elif isinstance(chart, LineChart):
        #     return DashTranslator._translate_line(chart)
        # elif isinstance(chart, PieChart):
        #     return DashTranslator._translate_pie(chart)
        # else:
        #     return dcc.Graph(figure={'data': chart.data, 'layout': {'title': chart.title}})
    
    @staticmethod
    def _translate_bar(chart):
        """Simple bar chart translation"""
        figure = {
            'data': [{
                'x': series['x'],
                'y': series['y'],
                'name': series.get('name', ''),
                'type': 'bar',
                'orientation': 'h' if chart.horizontal else 'v'
            } for series in chart.data],
            'layout': {
                'title': chart.title,
                'barmode': 'stack' if chart.stacked else 'group',
                'xaxis': chart.x_axis,
                'yaxis': chart.y_axis
            }
        }
        return dcc.Graph(figure=figure)
        

    @staticmethod
    def translate_table(table):
        return dbc.Table(
            children=[
                html.Thead(html.Tr([html.Th(col) for col in table.columns])),
                html.Tbody([
                    html.Tr([html.Td(item) for item in row]) for row in table.data
                ])
            ],
            striped=table.striped,
            bordered=table.bordered,
            hover=table.hover
        )

    @staticmethod
    def translate_child(child):
        if isinstance(child, Container):
            return DashTranslator.translate_container(child)
        elif isinstance(child, Row):
            return DashTranslator.translate_row(child)
        elif isinstance(child, Col):
            return DashTranslator.translate_column(child)
        elif isinstance(child, Chart):
            return DashTranslator.translate_chart(child)
        elif isinstance(child, Table):
            return DashTranslator.translate_table(child)
        elif isinstance(child, str):
            return html.P(child)
        else:
            return html.Div(str(child))

    @staticmethod
    def translate_dashboard(dashboard):
        app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

        app.layout = html.Div([
            html.H1(dashboard.title)
        ] + [DashTranslator.translate_container(container) for container in dashboard.containers])

        return app
