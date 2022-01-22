#: A simple program which calculates the % of streak of 6 heads or tails in a 10,000 experiment.
#: Automate the boring stufff with Python

import random
result = []
streak = 0
num_of_streaks = 0

for experimentnumber in range(10000):
    # creating a list of 100 'heads' or 'tails' value.
    for i in range(100):
        result.append(random.randint(0, 1))

    # checking if there is a streak of 6 heads or tails in a row.
    for i in range(len(result)):
        if i == 0:
            pass
        elif result[i] == result[i - 1]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            num_of_streaks += 1
    result = []
print("Chance of streak: {} %.".format((num_of_streaks / 10000) * 100))
