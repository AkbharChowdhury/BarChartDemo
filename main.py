import itertools
from collections import Counter
from itertools import chain

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def main():
    plt.style.use("fivethirtyeight")
    data = pd.read_csv('data.csv')
    languages = data['LanguagesWorkedWith']
    language_counter = Counter(list(chain.from_iterable([language.split(';') for language in languages])))
    languages_data: dict[str, int] = {item[0]: item[1] for item in language_counter.most_common(15)}
    languages_data = dict(reversed(list(languages_data.items())))
    plt.barh(languages_data.keys(), languages_data.values(), align='center')
    plt.title("Most Popular Languages")
    plt.ylabel("Programming Languages")
    plt.xlabel("Number of People Who Use")
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()




