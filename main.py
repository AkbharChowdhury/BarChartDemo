import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt


def main():
    plt.style.use("fivethirtyeight")

    data = pd.read_csv('data.csv')
    ids = data['Responder_id']
    lang_responses = data['LanguagesWorkedWith']

    language_counter = Counter()

    for response in lang_responses:
        language_counter.update(response.split(';'))

    languages = []
    popularity = []
    lang_data:  dict[str, int] = {item[0]: item[1] for item in language_counter.most_common(15)}

    for item in language_counter.most_common(15):

        languages.append(item[0])
        popularity.append(item[1])

    languages.reverse()
    popularity.reverse()
    res = dict(reversed(list(lang_data.items())))
    plt.barh(res.keys(), res.values())


    plt.title("Most Popular Languages")
    # plt.ylabel("Programming Languages")
    plt.xlabel("Number of People Who Use")

    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
