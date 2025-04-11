from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
hobbies = {
    'coding': 46,
    'exercising': 54,
    'shopping': 30,
    'socialising': 25,
    'media consumption': 40,
    'reading': 28
}

slices = list(hobbies.values())
labels = [hobby.title() for hobby in hobbies.keys()]
longest_hobby = max(hobbies.items(), key=lambda x: x[1])
explode = [0 if i!=longest_hobby[1] else 0.1 for i in hobbies.values()]
plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})
plt.title('How I Spend My Free Time')
plt.tight_layout()
plt.show()
