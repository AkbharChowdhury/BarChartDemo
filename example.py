import hvplot.pandas
import pandas as pd
import numpy as np
from vega_datasets import data as vds


def line_plot():
    df_line = pd.DataFrame({
        # 'x':list(np.arran)
        'x': np.arange(0, 100, 10).tolist(),
        'y': np.random.rand(10)
    })
    print(df_line)
    df_line.hvplot(x='x',y='y', kind='line')

line_plot()
