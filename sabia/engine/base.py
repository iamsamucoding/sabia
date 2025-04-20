from abc import ABC
from typing import Any
import pandas as pd

from ..layout import Container, Row, Col
from ..dashboard import DashboardHeader, Dashboard

class LayoutRenderer(ABC):
    def render_dashboard_header(self, header: DashboardHeader):
        pass

    def render_dashboard(self, dashboard: Dashboard):
        pass

    def render_container(self, container: Container):
        pass

    def render_col(self, col: Col):
        pass

    def render_row(self, row: Row):
        pass

class Engine(ABC):
    layout_renderer: LayoutRenderer
    
    def render(self, dashboard: Dashboard):
        pass