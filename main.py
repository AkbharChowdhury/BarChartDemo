from collections import Counter

import pandas as pd
from matplotlib import pyplot as plt
import hvplot.pandas

def main():
    plt.style.use("fivethirtyeight")
    data = pd.read_csv('data.csv')
    lang_responses = data['LanguagesWorkedWith']

    language_counter = Counter()

    for response in lang_responses:
        language_counter.update(response.split(';'))

    languages_data:  dict[str, int] = {item[0]: item[1] for item in language_counter.most_common(15)}
    languages_data = dict(reversed(list(languages_data.items())))
    plt.barh(languages_data.keys(), languages_data.values())


    plt.title("Most Popular Languages")
    plt.ylabel("Programming Languages")
    plt.xlabel("Number of People Who Use")

    plt.tight_layout()

    plt.show()
def x():
    # data = {'x': ['A', 'B', 'C'], 'y1': [10, 15, 12], 'y2': [8, 9, 11]}
    # df = pd.DataFrame(data)
    # df.hvplot.bar(x='x', y=['y1', 'y2'], stacked=True)
    # hvplot.bar()


    data = {'x': ['A', 'B', 'C'], 'y1': [10, 15, 12], 'y2': [8, 9, 11]}
    df = pd.DataFrame(data)  # Create a grouped bar chart
    df.hvplot.bar(x='x', y=['y1', 'y2'], stacked=False)
    df.hv

if __name__ == '__main__':
    x()
    # main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
