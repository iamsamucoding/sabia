from .layout import Container
from typing import List
from .layout import Row, Col


class Dashboard:
    def __init__(self, title=None, containers: List = None, theme: str = None):
        self.title = title
        self.containers = containers or []
        self.theme = theme

    def set_theme(self, theme):
        self.theme = theme
        return self

    def add_container(self, container):
        self.containers.append(container)
        return self
    