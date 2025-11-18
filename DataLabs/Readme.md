
# 🎬 Snorkel IMDB Sentiment Lab  

This repository contains **three hands-on labs** built using the **IMDB Movie Review Sentiment Dataset** to teach how Snorkel can be used to create high-quality training data *without manually labeling thousands of samples.*

---

# 📁 Project Structure
```bash

snorkel-movie-review-lab/
│
├── 01_sentiment_labeling_tutorial.ipynb
├── 02_sentiment_augmentation_tutorial.ipynb
├── 03_sentiment_slicing_tutorial.ipynb
├── utils.py
└── data/
├── train.csv
├── test.csv
```


---

# 🎯 What You Will Learn

### ✅ **1. Labeling Functions (LFs)**  
How to build rule-based labeling functions to label IMDB movie reviews *programmatically* using:
- Keyword heuristics  
- Regex-based rules  
- Pattern-based sentiment clues  
- Snorkel `LabelModel` to combine noisy labels  
- End-to-end weak supervision pipeline

---

### ✅ **2. Data Augmentation (TFs)**  
Learn how to expand your dataset using **transformation functions**:
- Synonym replacement  
- Random word deletion  
- Negation insertion  
- Snorkel's updated `PandasTFApplier` with correct policy usage  
- Build a larger, more diverse dataset without manual effort

---

### ✅ **3. Data Slicing (Slices)**  
Teach the model to focus on important subgroups of data:
- Very short reviews  
- Very long reviews  
- ALL CAPS reviews  
- Create slice membership matrices  
- Train slice-aware vs baseline models  
- Compare performance improvement on hard slices

---

# 🧩 Dataset

This lab uses a **clean IMDB sentiment dataset** with two columns:

| text | label |
|------|--------|
| "This movie was amazing!" | 1 |
| "Terrible acting and slow." | 0 |

---

# 🔧 Utilities (`utils.py`)

This file includes helper functions used across notebooks:
- `clean_text()` – text cleaning for IMDB reviews  
- `load_datasets()` – load & combine CSVs automatically  
- `plot_label_counts()` – visualize label distribution  

This keeps all notebooks clean and beginner-friendly.

---

# 🚀 How to Run This Lab

### ### Option 1 — Google Colab (**Recommended**)

1. Open each notebook in Colab  
2. Upload the `data/` folder + `utils.py`  
3. Run the cells step-by-step

### Option 2 — Local Machine

```bash
pip install snorkel numpy pandas scikit-learn matplotlib
jupyter notebook

