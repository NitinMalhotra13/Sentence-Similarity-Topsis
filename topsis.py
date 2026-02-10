import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")
criteria = df.iloc[:, 1:].values

norm = criteria / np.sqrt((criteria**2).sum(axis=0))

weights = np.array([0.4, 0.2, 0.2, 0.2])
weighted = norm * weights

ideal_best = [max(weighted[:,0]), max(weighted[:,1]), min(weighted[:,2]), min(weighted[:,3])]
ideal_worst = [min(weighted[:,0]), min(weighted[:,1]), max(weighted[:,2]), max(weighted[:,3])]

D_plus = np.sqrt(((weighted - ideal_best)**2).sum(axis=1))
D_minus = np.sqrt(((weighted - ideal_worst)**2).sum(axis=1))

score = D_minus / (D_plus + D_minus)

df["TOPSIS Score"] = score
df["Rank"] = df["TOPSIS Score"].rank(ascending=False)

df.to_csv("result.csv", index=False)
print(df.sort_values("Rank"))