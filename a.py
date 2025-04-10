# # import matplotlib.pyplot as plt
# # import numpy as np
# # # Fixing random state for reproducibility
# # np.random.seed(19680801)
# #
# # # Example data
# # people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# # y_pos = np.arange(len(people))
# # performance = 3 + 10 * np.random.rand(len(people))
# # error = np.random.rand(len(people))
# #
# # fig, ax = plt.subplots()
# #
# # hbars = ax.barh(y_pos, performance, xerr=error, align='center')
# # ax.set_yticks(y_pos, labels=people)
# # ax.invert_yaxis()  # labels read top-to-bottom
# # ax.set_xlabel('Performance')
# # ax.set_title('How fast do you want to go today?')
# #
# # # Label with specially formatted floats
# # ax.bar_label(hbars, fmt='%.2f')
# # ax.set_xlim(right=15)  # adjust xlim to fit labels
# #
# # plt.show()
#
#
#
# from collections import Counter
# from itertools import chain
#
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
#
#
# def main():
#     plt.style.use("fivethirtyeight")
#     data = pd.read_csv('programming_lang_responses.csv')
#     languages = data['LanguagesWorkedWith']
#     # language_counter = Counter(list(chain.from_iterable(list((  language.split(';') for language in languages)))))
#     language_counter = Counter(list(chain.from_iterable(list((  language.split(';') for language in languages)))))
#     language_counter = Counter(list(chain.from_iterable( [ language.split(';') for language in languages    ]))))
#
#     languages_data: dict[str, int] = {item[0]: item[1] for item in language_counter.most_common(15)}
#     languages_data = dict(reversed(list(languages_data.items())))
#     plt.barh(languages_data.keys(), languages_data.values(), align='center')
#     plt.title("Most Popular Languages")
#     plt.ylabel("Programming Languages")
#     plt.xlabel("Number of People Who Use")
#     plt.tight_layout()
#     plt.show()
#
#
# if __name__ == '__main__':
#     main()
