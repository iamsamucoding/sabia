import pandas as pd

class LineChart:
    def __init__(self, data: pd.DataFrame, x: str, y: str, color: str = None, title: str = "", **kwargs):
        self.data = data
        self.x = x
        self.y = y
        self.color = color
        self.title = title
        self.kwargs = kwargs

    def render(self, engine: str = "dash"):
        """
        Renders the line chart using the specified engine.
        """
        if engine == "dash":
            import plotly.express as px
            fig = px.line(self.data, x=self.x, y=self.y, color=self.color, title=self.title, **self.kwargs)
            return fig
        else:
            raise ValueError(f"Unsupported engine: {engine}")
#         self.children = children or []