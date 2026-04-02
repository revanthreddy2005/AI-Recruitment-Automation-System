#  AI Recruitment Automation System

An AI-powered recruitment automation system that evaluates candidate-job fit using semantic understanding, skill matching, and explainable decision-making.

---

## 📌 Problem

Manual resume screening is:
- Time-consuming ⏳  
- Inconsistent ⚠️  
- Hard to scale 📉  

Recruiters often struggle to quickly identify the best candidates from large application pools.

---

## 💡 Solution

This project builds an **AI-driven evaluation system** that:

- Analyzes resumes and job descriptions  
- Computes semantic similarity using embeddings  
- Extracts and compares relevant skills  
- Generates **explainable hiring decisions**  

---

## ⚙️ Features

✅ Semantic Matching using Sentence Transformers  
✅ Skill Extraction & Comparison  
✅ Decision Engine (Shortlist / Review / Reject)  
✅ Explainable Output (matched & missing skills)  
✅ Confidence Scoring  
✅ FastAPI-based backend (real-world API simulation)  

---

## 🧠 How It Works

1. **Input**
   - Resume text
   - Job description

2. **Processing**
   - Convert text → embeddings  
   - Compute similarity score  
   - Extract skills from both inputs  
   - Compare matched vs missing skills  

3. **Output**
   - Match Score (0–100)
   - Decision (Shortlist / Review / Reject)
   - Matched Skills
   - Missing Skills
   - Explanation

---

## 🛠 Tech Stack

- Python 🐍  
- FastAPI ⚡  
- Sentence Transformers 🤖  
- Scikit-learn 📊  

---

## 📊 Sample Output

```json
{
  "score": 72.45,
  "decision": "Review",
  "matched_skills": ["Python", "Pandas"],
  "missing_skills": ["Machine Learning", "NLP"],
  "reason": "Matched 2 skills, missing 2 required skills"
}

## 📊 Sample Output
<img width="634" height="599" alt="image" src="https://github.com/user-attachments/assets/4d9a001a-fdb0-42f0-acfa-8ec45b434faa" />

<img width="388" height="245" alt="image" src="https://github.com/user-attachments/assets/10915dc6-2bd8-47e8-b007-52342e5e6d84" />


---

**##🚀 How to Run**
git clone https://github.com/your-username/AI-Recruitment-Automation-System.git
cd AI-Recruitment-Automation-System

2. **Install dependencies**
pip install fastapi uvicorn sentence-transformers scikit-learn

3. **Run the server**
uvicorn main:app --port 8001 --log-level debug

4. **Open in browser**
http://127.0.0.1:8001/docs

---

## 🧪 **Example Input**
```json
{
  "resume": "Python, Machine Learning, NLP",
  "job_desc": "Looking for a candidate with Python, ML, and NLP experience"
}

---

## 🎯 **Use Case**
-Automated resume screening
-Recruitment process optimization
-HR tech / ATS integration
-AI-based candidate ranking systems

---

🔮 **Future Improvements**
-LLM-based explanation generation
-Integration with recruitment platforms (e.g., Manatal API)
-Workflow automation using tools like n8n
-Candidate ranking across multiple applications
-Bias reduction and fairness evaluation

---

## 🙋‍♂️ Author
Bommala Revanth Reddy
AI & Data Science Enthusiast
