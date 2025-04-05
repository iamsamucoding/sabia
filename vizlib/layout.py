from typing import List

class Container:
    def __init__(self, 
                 children: list = None,
                 fluid: bool = False,
                 class_name: str = None,
                 style: dict = None):
        self.fluid = fluid
        self.class_name = class_name
        self.style = style or {}
        self.children = children or []

    def add_child(self, child):
        self.children.append(child)
        return self


class Row:
    def __init__(self,
                 cols: list = None,
                 class_name=None, style=None, justify=None, align=None):
        self.class_name = class_name
        self.style = style or {}
        self.justify = justify  # start, center, end, between, around
        self.align = align      # start, center, end
        self.columns = []

    def add_column(self, column):
        self.columns.append(column)
        return self
