class Table:
    def __init__(self, data=None, columns=None, title=None,
                 striped=False, bordered=False, hover=False):
        self.data = data or []
        self.columns = columns or []
        self.title = title
        self.striped = striped
        self.bordered = bordered
        self.hover = hover

    def add_row(self, row):
        self.data.append(row)
        return self

    def set_columns(self, columns):
        self.columns = columns
        return self
