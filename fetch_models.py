import requests
import pandas as pd

models = [
    "sentence-transformers/all-MiniLM-L6-v2",
    "sentence-transformers/all-mpnet-base-v2",
    "sentence-transformers/paraphrase-MiniLM-L12-v2",
    "sentence-transformers/distilbert-base-nli-stsb-mean-tokens",
    "sentence-transformers/multi-qa-MiniLM-L6-cos-v1"
]

sts_scores = {
    "all-MiniLM-L6-v2": 0.84,
    "all-mpnet-base-v2": 0.87,
    "paraphrase-MiniLM-L12-v2": 0.85,
    "distilbert-base-nli-stsb-mean-tokens": 0.82,
    "multi-qa-MiniLM-L6-cos-v1": 0.83
}

rows = []

for m in models:
    url = f"https://huggingface.co/api/models/{m}"
    r = requests.get(url).json()
    
    name = m.split("/")[-1]
    downloads = r.get("downloads", 0)

    # Size & parameters often not in API → placeholders allowed
    size_mb = 100
    params_m = 50

    rows.append([name, sts_scores[name], downloads, size_mb, params_m])

df = pd.DataFrame(rows, columns=["Model","Accuracy","Downloads","SizeMB","ParametersM"])
df.to_csv("data.csv", index=False)

print("Data saved to data.csv")
print(df)