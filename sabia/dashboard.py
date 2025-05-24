from typing import List
from typing import Optional, Any, Dict

import dash_bootstrap_components as dbc
from dash import html
import dash

from .layout import Container

class DashboardHeader:
    def __init__(self, title: str, subtitle: str = "", kargs: Dict = None):
        self.title = title
        self.subtitle = subtitle
        self.kargs = kargs or {}

class ItauPrismaHeader(DashboardHeader):
    def __init__(self, title, subtitle = "", last_update: str = None):
        super().__init__(title, subtitle)

        self.last_update = last_update or ""
        self.logo_path = './assets/img/itau_logo.png'



class Dashboard:
    def __init__(self, title: str,
                 subtitle: str = "",
                 header: Optional[DashboardHeader] = None):
        self.header = header or DashboardHeader(title, subtitle)
        self.containers: List[Container] = []
    
    def add_container(self, container: Container):
        """Add a container to the dashboard"""
        self.containers.append(container)
    
    def render(self, engine: str = "dash"):
        """Render the dashboard using the specified engine"""
        if engine == "dash":
            dashboard = dash.Dash(self.header.title, external_stylesheets=[dbc.themes.BOOTSTRAP])
            
            dashboard.layout = html.Div(
                [
                    self.header.render(engine),
                    *[container.render(engine) for container in self.containers]
                ],
                className="dashboard-container"
            )
            return dashboard
        else:
            raise ValueError(f"Unsupported engine: {engine}")
    