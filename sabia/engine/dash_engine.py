import abc
from typing import Any

from ..layout import Container, Row, Col
from ..dashboard import DashboardHeader, Dashboard
from .base import Engine, LayoutRenderer

import dash_bootstrap_components as dbc
import dash
from dash import html


class DashEngine(Engine):
    def __init__(self):
        self.layout_renderer = DashLayoutRenderer()

    def render(self, dashboard: Dashboard) -> dash.Dash:
        return self.layout_renderer.render_dashboard(dashboard)


class DashLayoutRenderer(LayoutRenderer):
    def render_dashboard_header(self, header: DashboardHeader) -> html.Div:
        return html.Div(
            [
                html.H1(header.title),
                html.H2(header.subtitle)
            ],
            className="dashboard-header"
        )
    
    def render_dashboard(self, dashboard: Dashboard) -> dash.Dash:
        rendered_dashboard = dash.Dash(dashboard.header.title, external_stylesheets=[dbc.themes.BOOTSTRAP])
            
        rendered_dashboard.layout = html.Div(
            [
                self.render_dashboard_header(dashboard.header),
                *[self.render_container(container) for container in dashboard.containers]
            ],
            className="dashboard-container"
        )
        return rendered_dashboard

    def render_container(self, container: Container) -> dbc.Container:
        children = []
        for child in container.children:
            children.append(self.render_row(child))
        
        kwargs = container.kwargs.copy()
        kwargs['children'] = children
        
        return dbc.Container(**kwargs)

    def render_row(self, row: Row) -> dbc.Row:
        children = []
        
        for child in row.children:
            children.append(self.render_col(child))
        
        kwargs = row.kwargs.copy()
        kwargs['children'] = children
        
        return dbc.Row(**kwargs)
    
    def render_col(self, col: Col) -> dbc.Col:
        return dbc.Col(**col.kwargs)

