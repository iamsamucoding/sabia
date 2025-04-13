class Chart:
    def __init__(self, title=None, data=None, chart_type='line',
                 x_axis=None, y_axis=None, options=None):
        self.title = title
        self.data = data or []
        self.chart_type = chart_type
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.options = options or {}

    def add_series(self, series):
        self.data.append(series)
        return self


class BarChart(Chart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, chart_type='bar', **kwargs)


class LineChart(Chart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, chart_type='line', **kwargs)


class PieChart(Chart):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, chart_type='pie', **kwargs)
