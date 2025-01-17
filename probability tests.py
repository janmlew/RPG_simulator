import numpy as np
import pandas as pd

dies = 1
difficulty = 0
throws = 100
successes: int = 0
columns = ["Wrath"]

print("Type in the number of dies (a singular int value, please):")
try:
    dies = int(input())
except ValueError:
    dies = 1
print(f"Number of dies is {dies}.")

for die in range(2, dies+1):
    columns.append(f"Die {die}")

df = pd.DataFrame(columns=columns)

for throw in range(0, throws):
    for die in range(1, dies+1):
        toss = np.random.randint(1, 7)
        df.loc[throw, columns[die-1]] = toss
        if toss == 6:
            successes += 2
        elif toss > 3:
            successes += 1
    df.loc[throw, "Successes"] = int(successes)
    successes: int = 0

print("Type in the Difficulty Number (a singular int value, please):")
try:
    difficulty = int(input())
except ValueError:
    difficulty = 0
print(f"DN is {difficulty}.")

for throw in range(0, throws):
    if df.loc[throw, "Successes"] - difficulty >= 0:
        df.loc[throw, "Result"] = 1
    else:
        df.loc[throw, "Result"] = 0

print(f"Probability of a success is approximately {int(sum(df['Result']))}%.")
