# Sentence Similarity Model Evaluation using TOPSIS

##  Objective
The objective of this project is to evaluate and rank **pre-trained Sentence Similarity NLP models** using the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** multi-criteria decision-making method.

Instead of training models, this project compares existing Hugging Face models based on performance and efficiency metrics to determine the best overall model.

---

##  Models Evaluated
- all-MiniLM-L6-v2  
- all-mpnet-base-v2  
- paraphrase-MiniLM-L12-v2  
- distilbert-base-nli-stsb-mean-tokens  
- multi-qa-MiniLM-L6-cos-v1  

---

##  Evaluation Criteria

| Criterion | Type | Description |
|---------|------|------------|
| Accuracy (STS Score) | Benefit ↑ | Semantic Textual Similarity |
| Downloads | Benefit ↑ | Popularity / usage |
| Model Size (MB) | Cost ↓ | Storage requirement |
| Parameters (Millions) | Cost ↓ | Model complexity |

---

##  Methodology
1. Fetch model information from Hugging Face API  
2. Create decision matrix  
3. Normalize matrix  
4. Apply weights  
5. Determine ideal best & worst  
6. Compute distances  
7. Calculate TOPSIS score  
8. Rank models  
9. Visualize results  

---

##  Project Structure

```
sentence_similarity_topsis/
│
├── fetch_models.py
├── topsis.py
├── graph.py
├── data.csv
├── result.csv
├── requirements.txt
└── README.md
```

---

##  How to Run

### Install Dependencies
```
pip install -r requirements.txt
```

### Execute Files
```
python fetch_models.py
python topsis.py
python graph.py
```

---

##  Screenshots

### Data CSV Preview
<img width="808" height="194" alt="image" src="https://github.com/user-attachments/assets/82c393b4-1d2a-4ea1-8597-01b89687c9e7" />


---

### Result CSV Preview
<img width="946" height="185" alt="image" src="https://github.com/user-attachments/assets/56ea7ebe-6502-47ac-8f6f-71e8af249823" />


---

##  Graph Output
<img width="1487" height="896" alt="image" src="https://github.com/user-attachments/assets/a4611217-bcf6-40e5-8726-c1be86a9e730" />


---

##  Conclusion
The model with the **highest TOPSIS score** is considered the best overall sentence similarity model considering accuracy, efficiency, and popularity.

---

## Result

The model all-MiniLM-L6-v2 is the best overall model.

---

##  Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Hugging Face API  

---

##  Notes
- Some metrics such as parameter count or model size may be approximated.
- The project focuses on **comparative evaluation**, not model training.
