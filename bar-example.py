import hvplot.pandas
import pandas as pd
import numpy as np
from vega_datasets import data as vds
from numpy import random
from collections import Counter
from itertools import chain
from matplotlib import pyplot as plt

data = pd.read_csv("programming_lang_responses.csv")
languages = data['LanguagesWorkedWith']
language_counter = Counter(list(chain.from_iterable([language.split(';') for language in languages])))
languages_data: dict[str, int] = {item[0]: item[1] for item in language_counter.most_common(15)}
languages_data = dict(reversed(list(languages_data.items())))
df = pd.DataFrame({
        'tech-stack': list(languages_data.keys()),
        'popularity': list(languages_data.values())
    })
plot = df.hvplot.barh(x='tech-stack', y='popularity',
                      title='Most popular programming languages'.title(),
                      xlabel='Programming Languages'.title(), ylabel="Number of People Who Use",
                      height=400,
                      width=600)
plot