# 🧠 Resume Keyword Matcher (Mini ATS)

## 📝 Project Overview

This project implements a **Resume Keyword Matching System (Mini ATS)** that ranks resumes based on their relevance to a given job description using **Natural Language Processing (NLP)** techniques.

The system processes raw resume data (PDF files), extracts text, converts it into numerical features, and computes similarity scores to identify the best-matching candidates.

It demonstrates an end-to-end pipeline including **data extraction, preprocessing, feature engineering, similarity computation, and visualization**.

---

# 📂 Repository Contents

| File Name            | Type          | Description                            |
| -------------------- | ------------- | -------------------------------------- |
| `main.py`            | Python Script | Entry point to run the entire pipeline |
| `data_loader.py`     | Module        | Extracts text from PDF resumes         |
| `preprocessing.py`   | Module        | Cleans and preprocesses text           |
| `matcher.py`         | Module        | Computes similarity and ranks resumes  |
| `visualize.py`       | Module        | Generates ranking visualization        |
| `data/`              | Folder        | Contains resumes and job description   |
| `requirements.txt`   | Dependencies  | Required Python libraries              |
| `README.md`          | Documentation | Project overview and usage             |
| `resume_ranking.png` | Output        | Saved visualization of results         |

---

# ⚙️ Tech Stack

| Component            | Tool / Library    | Purpose                              |
| -------------------- | ----------------- | ------------------------------------ |
| Programming Language | Python            | Core implementation                  |
| NLP Processing       | NLTK              | Text cleaning and stopword removal   |
| Feature Engineering  | TF-IDF            | Convert text into numerical features |
| Similarity Measure   | Cosine Similarity | Compare resumes with job description |
| Data Handling        | PyPDF2            | Extract text from PDF resumes        |
| Visualization        | Matplotlib        | Generate ranking graph               |

---

# 🏗️ Data Preparation & Feature Engineering

## 1️⃣ Data Extraction

* Extracted text from PDF resumes using PyPDF2
* Loaded job description from text file

## 2️⃣ Data Cleaning

* Converted text to lowercase
* Removed special characters and noise
* Removed stopwords using NLTK
* Normalized important phrases (e.g., *Power BI → powerbi*)

## 3️⃣ Feature Extraction

* Converted text into numerical vectors using

  * TF-IDF
* Captured importance of keywords across resumes

---

# 🤖 Matching & Ranking Logic

* Compared resumes with job description using

  * Cosine Similarity
* Generated similarity scores between 0 and 1
* Ranked resumes based on relevance
* Extracted matched keywords for interpretability

---

# 🚀 Application Features

## 🔹 Resume Ranking

* Automatically ranks resumes based on job description
* Displays similarity scores

## 🔹 Keyword Matching

* Shows overlapping skills between resume and job description
* Improves explainability of results

## 🔹 File-Based Processing

* Works directly with real PDF resumes
* Mimics real-world ATS systems

## 🔹 Visualization

* Generates a bar chart of resume rankings
* Saves output as image file

---

# 📊 Output & Insights

* Ranked list of resumes with scores
* Matched skills for each candidate
* Visualization saved as `resume_ranking.png`

👉 Helps identify **best-fit candidates quickly**

---

# ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

# 📊 Sample Output

```
🏆 RESUME RANKING RESULTS

Rank #1
Resume: R21.pdf
Score : 0.82
Matched Skills: powerbi, sql, python
```

---

# 💡 Use Cases

* Resume screening automation
* Candidate shortlisting
* HR analytics
* Job-candidate matching systems

---

# 🔗 Concepts Used

* Natural Language Processing
* TF-IDF Vectorization
* Cosine Similarity
* Text Preprocessing

---

# 💡 Future Enhancements

* Build web app using Streamlit
* Add skill weighting (important skills priority)
* Support DOCX resumes
* Improve keyword extraction with NLP models
* Deploy as API

---

# 🎯 Conclusion

This project demonstrates a **real-world NLP application** for automating resume screening. It showcases how text data can be transformed into actionable insights using similarity-based techniques.

It is a practical example of applying NLP for **recruitment automation and decision-making**.
