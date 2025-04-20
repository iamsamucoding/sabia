import abc
from typing import Any

from ..layout import Container, Row, Col
from ..dashboard import DashboardHeader, Dashboard
from .base import Engine, LayoutRenderer

import dash_bootstrap_components as dbc
import dash
from dash import html

# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/

def process_margin_classes(
    top: int,
    bottom: int,
    left: int,
    right: int
) -> str:
        """Generate Bootstrap margin classes from individual margin parameters."""
        classes = []
        
        if top is not None:
            classes.append(f"mt-{top}")
        if bottom is not None:
            classes.append(f"mb-{bottom}")
        if left is not None:
            classes.append(f"ms-{left}")
        if right is not None:
            classes.append(f"me-{right}")
            
        return " " + " ".join(classes) if classes else ""



class DashEngine(Engine):
    def __init__(self):
        self.layout_renderer = DashLayoutRenderer()

    def render(self, dashboard: Dashboard) -> dash.Dash:
        return self.layout_renderer.render_dashboard(dashboard)


class DashLayoutRenderer(LayoutRenderer):
    def render_dashboard_header(self, header: DashboardHeader) -> html.Div:
        return dbc.Container(
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

    def render_container(self, container_in: Container) -> dbc.Container:
        container = container_in.copy()
        
        children = []
        for child in container.children:
            children.append(self.render_row(child))
        
        class_name = container.class_name

        class_name += process_margin_classes(
            container.margin.top,
            container.margin.bottom,
            container.margin.left,
            container.margin.right
        )

        return dbc.Container(children=children,
                             class_name=class_name.strip(),
                             fluid=container.fluid, **container.kwargs)

    def render_row(self, row_in: Row) -> dbc.Row:
        row = row_in.copy()
        
        children = []
        
        for child in row.children:
            children.append(self.render_col(child))
        
        return dbc.Row(children=children, class_name=row.class_name, **row.kwargs)
    
    def render_col(self, col_in: Col) -> dbc.Col:
        col = col_in.copy()

        return dbc.Col(children=col.children,
                       class_name=col.class_name,
                       style=col.style,
                       width=col.width,
                       **col.kwargs)

