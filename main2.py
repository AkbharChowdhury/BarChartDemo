import hvplot.pandas as p
import numpy as np
import pandas as pd
from numpy import random

data = {
    'cat': [str(i) for i in range(5)],
    'val': [random.randint(100) for _ in range(5)]
}
print(data)
df = pd.DataFrame(data)
plot = df.hvplot.bar(x='cat', y='val', title='example', xlabel='tags', ylabel="values", height=400, width=600)
plot