import numpy as np
import pandas as pd

dies = 1
columns = ["Wrath"]

print("Type the number of dies (a singular int value, please):")
try:
    dies = int(input())
except ValueError:
    dies = 1

for die in range(2, dies+1):
    columns.append(f"Die {die}")

df = pd.DataFrame(columns=columns)

for throw in range(0, 100):
    for die in range(1, dies+1):
        df.loc[throw, columns[die-1]] = np.random.randint(1, 7)

print(df)

print("Type the Difficulty Number (a singular int value, please):")
try:
    dies = int(input())
except ValueError:
    dies = 1

