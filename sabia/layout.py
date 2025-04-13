from typing import List, Optional, Any
import dash_bootstrap_components as dbc


class Col:
    """
    Custom Column class that extends the Dash Bootstrap Components Column class.
    It allows for additional attributes to be set for the column layout.
    """
    def __init__(self, children=None, width=None, class_name=None, style=None, **kwargs):
        self.children = children or []
        self.children = children if isinstance(children, list) else [children]
        self.width = width  # e.g., 'auto', '50%', etc.
        self.class_name = class_name
        self.style = style or {}
        
        kwargs['children'] = self.children
        kwargs['className'] = class_name
        kwargs['style'] = style or {}
        kwargs['width'] = width
        self.kwargs = kwargs

    def render(self, engine: str = "dash"):
        """
        Renders the column using the specified engine.
        """
        if engine == "dash":
            return dbc.Col(**self.kwargs)
        else:
            raise ValueError(f"Unsupported engine: {engine}")

        
class Row:
    """Simplified Row wrapper that mimics dbc.Row parameters"""
    def __init__(self, 
                 children: List[Col] = None,
                 class_name: str = "",
                 **kwargs):
        self.children = children or []
        self.class_name = class_name

        kwargs['children'] = self.children
        kwargs['className'] = class_name
        self.kwargs = kwargs
    
    def add_col(self, *args, **kwargs) -> 'Row':
        """Helper method to add columns directly to the row"""
        self.children.append(Col(*args, **kwargs))
        return self
    
    def render(self, engine: str = "dash"):
        """
        Renders the row using the specified engine.
        """
        if engine == "dash":
            children = []
            for child in self.children:
                children.append(child.render(engine))
            
            kwargs = self.kwargs.copy()
            kwargs['children'] = children
            
            row = dbc.Row(**kwargs)

            return row
        else:
            raise ValueError(f"Unsupported engine: {engine}")

class Container:
    """Simplified Container wrapper that mimics dbc.Container parameters"""
    def __init__(self, 
                 children: List[Row] = None,
                 class_name: str = "",
                 fluid: bool = True,
                 **kwargs):
        self.children = children or []
        self.class_name = class_name
        self.fluid = fluid

        kwargs['children'] = self.children
        kwargs['className'] = class_name
        kwargs['fluid'] = fluid
        self.kwargs = kwargs
    
    def add_row(self, *args, **kwargs) -> 'Container':
        """Helper method to add rows directly to the container"""
        self.children.append(Row(*args, **kwargs))
        return self
    
    def render(self, engine: str = "dash"):
        """
        Renders the container using the specified engine.
        """
        if engine == "dash":
            children = []
            for child in self.children:
                children.append(child.render(engine))
            
            kwargs = self.kwargs.copy()
            kwargs['children'] = children
            
            container = dbc.Container(**kwargs)

            return container
        else:
            raise ValueError(f"Unsupported engine: {engine}")
