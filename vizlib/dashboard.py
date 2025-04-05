from .layout import Container


class Dashboard:
    def __init__(self, title=None, layout='fluid'):
        self.title = title
        self.layout = layout
        self.container = Container(fluid=(layout == 'fluid'))
        self.theme = None

    def set_theme(self, theme):
        self.theme = theme
        return self

    def add_component(self, component, row_idx=None, col_idx=None):
        # Simplified version - would need more complex layout management
        if not self.container.children:
            self.container.add_child(Row())

        if row_idx is None:
            row = self.container.children[-1]
        else:
            row = self.container.children[row_idx]

        if col_idx is None:
            if not row.columns:
                row.add_column(Column())
            col = row.columns[-1]
        else:
            col = row.columns[col_idx]

        col.add_child(component)
        return self
