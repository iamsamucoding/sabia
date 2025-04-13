import abc
from typing import Any

from .layout import Container, Row, Col
from .dashboard import DashboardHeader, Dashboard
import dash_bootstrap_components as dbc

import dash
from dash import html

class RenderEngineFactory:
    """
    Factory class to create rendering engines based on the specified engine type.
    """
    
    @staticmethod
    def create_engine(engine: str) -> 'RenderEngine':
        if engine == "dash":
            return DashRenderEngine()
        else:
            raise ValueError(f"Unsupported engine: {engine}")

class RenderEngine(abc.ABC):
    """
    Abstract base class for rendering components in different engines.
    """
    self.renders = {}
    
    
    def __init__(self, engine: str = "dash"):
        self.engine = engine
    
    @abc.abstractmethod
    def render_header(self, header: Any) -> Any:
        """
        Render the header using the specified engine.
        
        Args:
            header (Any): The header to render.
        
        Returns:
            Any: The rendered header.
        """
        pass
    
    @abc.abstractmethod
    def render_dashboard(self, dashboard: Any) -> Any:
        """
        Render the dashboard using the specified engine.
        
        Args:
            dashboard (Any): The dashboard to render.
        
        Returns:
            Any: The rendered dashboard.
        """
        pass

    @abc.abstractmethod
    def render_container(self, container: Any) -> Any:
        """
        Render the container using the specified engine.
        
        Args:
            container (Any): The container to render.
        
        Returns:
            Any: The rendered container.
        """
        pass

    @abc.abstractmethod
    def render_row(self, row: Any) -> Any:
        """
        Render the row using the specified engine.
        
        Args:
            row (Any): The row to render.
        
        Returns:
            Any: The rendered row.
        """
        pass

    @abc.abstractmethod
    def render_col(self, col: Any) -> Any:
        """
        Render the column using the specified engine.
        
        Args:
            col (Any): The column to render.
        
        Returns:
            Any: The rendered column.
        """
        pass

    @abc.abstractmethod
    def render_chart(self, chart: Any) -> Any:
        """
        Render the chart using the specified engine.
        
        Args:
            chart (Any): The chart to render.
        
        Returns:
            Any: The rendered chart.
        """
        pass
    
    @abc.abstractmethod
    def render_kpi(self, kpi: Any) -> Any:
        """
        Render the KPI using the specified engine.
        
        Args:
            kpi (Any): The KPI to render.
        
        Returns:
            Any: The rendered KPI.
        """
        pass

    @abc.abstractmethod
    def render_table(self, table: Any) -> Any:
        """
        Render the table using the specified engine.
        
        Args:
            table (Any): The table to render.
        
        Returns:
            Any: The rendered table.
        """
        pass

class DashRenderEngine(RenderEngine):
    """
    Dash-specific rendering engine.
    """

    def render_dashboard(self, dashboard: Dashboard) -> db.Container:
        dashboard_app = dash.Dash(dashboard.title, external_stylesheets=[dbc.themes.BOOTSTRAP])
        
        dashboard_app.layout = html.Div(
            [
                dashboard.header.render(engine="dash"),
                *[self.render_container(container) for container in dashboard.containers]
            ],
            className="dashboard-container"
        )
        
        return dashboard_app
    
    def render_container(self, container: Container) -> dbc.Container:
        children = []
        for child in container.children:
            children.append(self.render_row(child))
        
        kwargs = container.kwargs.copy()
        kwargs['children'] = children
        
        container = dbc.Container(**kwargs)

        return container
    
    def render_row(self, row: Row) -> dbc.Row:
        children = []
        
        for child in row.children:
            children.append(self.render_col(child))
        
        kwargs = row.kwargs.copy()
        kwargs['children'] = children
        
        row = dbc.Row(**kwargs)

        return row
    
    def render_col(self, col: Col) -> dbc.Col:
        return dbc.Col(**col.kwargs)
    
    def render_chart(self, chart: Any) -> Any:
        return chart.render(engine="dash")
    
    def render_kpi(self, kpi: Any) -> Any:
        return kpi.render(engine="dash")
    
    def render_table(self, table: Any) -> Any:
        return table.render(engine="dash")


class PlotlyHeaderRenderer:
    """
    Dash-specific header renderer.
    """
    
    def render(self, header: DashboardHeader) -> dbc.Container:
        return dbc.Container(
                [
                    html.H1(self.title, className="header-title"),
                    html.P(self.subtitle, className="header-subtitle")
                ],
                className="header-container"
            )

class PlotlyDashboardRenderer:
    """
    Dash-specific dashboard renderer.
    """
    
    def render(self, dashboard: Dashboard) -> dbc.Container:
        return dbc.Container(
            [
                PlotlyHeaderRenderer().render(dashboard.header),
                *[self.render_container(container) for container in dashboard.containers]
            ],
            className="dashboard-container"
        ) 