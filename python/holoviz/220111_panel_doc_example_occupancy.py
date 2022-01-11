from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print()
print()
print(f"   Current file directory: {Path(__file__).parent.resolve()}")
print(f"Present working directory: {Path().resolve()}")
print()
print()

directory = Path(__file__).parent.resolve()
data_file = directory / "occupancy_data" / "datatest.txt"
data = pd.read_csv(data_file)
data["date"] = data.date.astype("datetime64[ns]")
data = data.set_index("date")

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas


def mpl_plot(avg, highlight):
    fig = Figure()
    # FigureCanvas(fig)  # not needed in mpl >= 3.1
    ax = fig.add_subplot()
    avg.plot(ax=ax)
    if len(highlight):
        highlight.plot(style="o", ax=ax)
    return fig


def find_outliers(variable="Temperature", window=30, sigma=10, view_fn=mpl_plot):
    avg = data[variable].rolling(window=window).mean()
    residual = data[variable] - avg
    std = residual.rolling(window=window).std()
    outliers = np.abs(residual) > std * sigma
    return view_fn(avg, avg[outliers])


import panel as pn
import panel.widgets as pnw

variable = pnw.RadioButtonGroup(
    name="variable", value="Temperature", options=list(data.columns)
)
window = pnw.IntSlider(name="window", value=10, start=1, end=60)

reactive_outliers = pn.bind(find_outliers, variable, window, 10)

widgets = pn.Column("<br>\n# Room occupancy", variable, window)
occupancy = pn.Row(reactive_outliers, widgets)

occupancy.servable()
