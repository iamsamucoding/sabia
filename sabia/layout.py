from typing import List, Optional, Any
import dash_bootstrap_components as dbc
import math
import copy

GRID_NUM_COLS = 12
from dataclasses import dataclass

@dataclass
class Margin:
    top: int = None
    bottom: int = None
    left: int = None
    right: int = None


class Col:
    """
    Custom Column class that extends the Dash Bootstrap Components Column class.
    It allows for additional attributes to be set for the column layout.
    """
    def __init__(self, children=None, width=None, class_name=None,
                mt: int = None,
                mb: int = None,
                ml: int = None,
                mr: int = None,
                kwargs: dict = None):
        self.children = children or []
        self.children = children if isinstance(children, list) else [children]

        assert width is None or (width > 0 and width <= 12), \
            "Width must be None or a number between 1 and 12"

        self.width = width  # e.g., 'auto', '50%', etc.
        self.auto_width = (width is None)
        self.class_name = class_name
        
        assert mt is None or mt >= 0, \
            "Top margin must be None or a positive number"
        assert mb is None or mb >= 0, \
            "Bottom margin must be None or a positive number"
        assert ml is None or ml >= 0, \
            "Left margin must be None or a positive number"
        assert mr is None or mr >= 0, \
            "Right margin must be None or a positive number"
        
        self.mt = mt
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.margin = Margin(mt, mb, ml, mr)

        self.kwargs = copy.deepcopy(kwargs) or {}
    
    def copy(self):
        """Returns a copy of the column object"""
        return Col(children=self.children, width=self.width,
                   class_name=self.class_name,
                   mt=self.margin.top,
                   mb=self.margin.bottom,
                   ml=self.margin.left,
                   mr=self.margin.right,
                   kwargs=self.kwargs)

        
class Row:
    """Simplified Row wrapper that mimics dbc.Row parameters"""
    def __init__(self, 
                 children: List[Col] = None,
                 class_name: str = "",
                 mt: int = None,
                 mb: int = None,
                 ml: int = None,
                 mr: int = None,
                 kwargs: dict = None):
        self.children = children or []
        self.class_name = class_name

        assert mt is None or mt >= 0, \
            "Top margin must be None or a positive number"
        assert mb is None or mb >= 0, \
            "Bottom margin must be None or a positive number"
        assert ml is None or ml >= 0, \
            "Left margin must be None or a positive number"
        assert mr is None or mr >= 0, \
            "Right margin must be None or a positive number"
        
        self.mt = mt
        self.mb = mb
        self.ml = ml
        self.mr = mr
        self.margin = Margin(mt, mb, ml, mr)

        self.kwargs = copy.deepcopy(kwargs) or {}
        self._auto_col_width()

    def _auto_col_width(self):
        auto_col_index = []
        total_col_width = 0

        for i, child in enumerate(self.children):
            if child.width is None:
                auto_col_index.append(i)
            else:
                total_col_width += child.width
        
        remaining_width = GRID_NUM_COLS - total_col_width
        auto_col_width = int(math.ceil(remaining_width / len(auto_col_index))) if auto_col_index else 0
        ceil_remaining_width = auto_col_width * len(auto_col_index)
        # print()
        # print(f'Auto column width: {auto_col_width}, Remaining width: {remaining_width}, Total width: {total_col_width}')
        # print(f'ceil_remaining_width = {ceil_remaining_width}, remaining_width = {remaining_width}')
        
        for i in auto_col_index:
            self.children[i].width = auto_col_width
        
        # Adjust the widths of the auto columns to fit within the remaining width
        # This is to ensure that the total width of the columns does not exceed GRID_NUM_COLS
        # and to avoid any floating point issues.
        i = len(auto_col_index) - 1
        while ceil_remaining_width > remaining_width and i > 0:
            self.children[auto_col_index[i]].width -= 1
            ceil_remaining_width -= 1
            i -= 1
        
        # self.print_widths()
        # print()

    
    def print_widths(self):
        """Prints the widths of the columns in the row"""
        for i, child in enumerate(self.children):
            print(f"Column {i}: {child.width}")
        print(f"Total Width: {sum(child.width for child in self.children)}")
    
    def copy(self):
        """Returns a copy of the row object"""
        return Row(children=[child.copy() for child in self.children],
                   class_name=self.class_name,
                   mt=self.margin.top,
                         mb=self.margin.bottom,
                         ml=self.margin.left,
                         mr=self.margin.right,
                         kwargs=self.kwargs)

    def add_col(self, col: Col) -> 'Row':
        """Helper method to add columns directly to the row"""
        self.children.append(col)
        self._auto_col_width()
        return self


class Container:
    """Simplified Container wrapper that mimics dbc.Container parameters"""
    def __init__(self, 
                 children: List[Row] = None,
                 class_name: str = "",
                 fluid: bool = False,
                 mt: int = None,
                 mb: int = None,
                 ml: int = None,
                 mr: int = None,
                 kwargs: dict = None):
        self.children = children or []
        self.class_name = class_name
        self.fluid = fluid

        assert mt is None or mt >= 0, \
            "Top margin must be None or a positive number"
        assert mb is None or mb >= 0, \
            "Bottom margin must be None or a positive number"
        assert ml is None or ml >= 0, \
            "Left margin must be None or a positive number"
        assert mr is None or mr >= 0, \
            "Right margin must be None or a positive number"
        
        self.margin = Margin(mt, mb, ml, mr)
        self.kwargs = copy.deepcopy(kwargs) or {}

    def copy(self):
        """Returns a copy of the container object"""
        return Container(children=[child.copy() for child in self.children],
                         class_name=self.class_name, fluid=self.fluid,
                         mt=self.margin.top,
                         mb=self.margin.bottom,
                         ml=self.margin.left,
                         mr=self.margin.right,
                         kwargs=self.kwargs)
    
    def add_row(self, row: Row) -> 'Container':
        """Helper method to add rows directly to the container"""
        self.children.append(row)
        return self
    