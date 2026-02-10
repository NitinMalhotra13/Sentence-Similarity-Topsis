import pandas as pd
import matplotlib.pyplot as plt
import textwrap

df = pd.read_csv("result.csv")

df["Model"] = df["Model"].apply(lambda x: "\n".join(textwrap.wrap(x, 12)))

plt.figure(figsize=(10,6))
plt.bar(df["Model"], df["TOPSIS Score"])

plt.title("TOPSIS Model Ranking")
plt.xlabel("Models")
plt.ylabel("Score")
plt.tight_layout()

plt.show()
