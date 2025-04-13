class Container:
    def __init__(self, fluid=False, class_name=None, style=None):
        self.fluid = fluid
        self.class_name = class_name
        self.style = style or {}
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return self


class Row:
    def __init__(self, class_name=None, style=None, justify=None, align=None):
        self.class_name = class_name
        self.style = style or {}
        self.justify = justify  # start, center, end, between, around
        self.align = align      # start, center, end
        self.columns = []

    def add_column(self, column):
        self.columns.append(column)
        return self


class Column:
    def __init__(self, span=12, sm=None, md=None, lg=None, xl=None,
                 offset=None, class_name=None, style=None):
        self.span = span
        self.sm = sm
        self.md = md
        self.lg = lg
        self.xl = xl
        self.offset = offset
        self.class_name = class_name
        self.style = style or {}
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        return self
