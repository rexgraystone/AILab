# 2. Write a Python program to implement and demonstrate the Candidate-Elimination algorithm to output a description of the set of all hypotheses consistent.

import pandas as pd

file = "EnjoySports.csv" #replace with CarSales.csv
df = pd.read_csv(f"Datasets/{file}", header = 0) 
dataset = df.values.tolist()

s = dataset[0][0:-1]
print(f"The initial value of specific hypothesis is {s}\n")

#initialize the general hypothesis
g = [['?' for i in range(len(s))] for j in range(len(s))]
print(f"The initial value of general hypothesis is {g}")

for row in dataset:
    if row[-1] == "Yes":
        for j in range(len(s)):
            if row[j] != s[j]:
                s[j] = '?'
                g[j][j] = '?'
    elif row[-1] == "No":
        for j in range(len(s)):
            if row[j] != s[j]:
                g[j][j] = s[j]
            else:
                g[j][j] = "?"
    print(f"Instance: {dataset.index(row)+1}")
    print(f"Specific boundary is: {s}")
    print(f"General boundary is: {g}")

print(f"Final specific hypothesis: {s}")
print(f"Final general hypothesis: {g}")