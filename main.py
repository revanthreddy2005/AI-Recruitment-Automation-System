from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import traceback

# Initialize FastAPI app
app = FastAPI()

# Request model
class EvaluationRequest(BaseModel):
    resume: str
    job_desc: str

# Load model lazily
model = None


# ---------- CORE LOGIC ----------

def get_match_score(resume, job_desc):
    global model

    try:
        if model is None:
            print("Loading model for the first time...")
            model = SentenceTransformer('all-MiniLM-L6-v2')
            print("Model loaded successfully!")

        emb1 = model.encode(resume)
        emb2 = model.encode(job_desc)

        score = cosine_similarity([emb1], [emb2])[0][0]
        return round(score * 100, 2)

    except Exception as e:
        print("ERROR in scoring:", e)
        return 0


def decision(score):
    if score > 75:
        return "Shortlist"
    elif score > 50:
        return "Review"
    else:
        return "Reject"


# ---------- SKILL EXTRACTION ----------

def extract_skills(text):
    skills = [
        "Python", "Machine Learning", "NLP",
        "TensorFlow", "Deep Learning", "Data Science",
        "SQL", "Pandas", "NumPy"
    ]

    found = []
    for skill in skills:
        if skill.lower() in text.lower():
            found.append(skill)

    return found


# ---------- API ----------

@app.post("/evaluate")
def evaluate(data: EvaluationRequest):
    try:
        print("===== REQUEST RECEIVED =====")
        print("Incoming data:", data)

        resume = data.resume
        job_desc = data.job_desc

        print("Resume:", resume)
        print("Job Desc:", job_desc)

        if not resume or not job_desc:
            return {"error": "Missing resume or job_desc"}

        # Core scoring
        score = get_match_score(resume, job_desc)
        result = decision(score)

        # Skill extraction
        resume_skills = extract_skills(resume)
        job_skills = extract_skills(job_desc)

        matched = list(set(resume_skills) & set(job_skills))
        missing = list(set(job_skills) - set(resume_skills))

        # Reason generation
        if result == "Shortlist":
            reason = "Candidate matches most required skills"
        elif result == "Review":
            reason = "Candidate partially matches job requirements"
        else:
            reason = "Candidate lacks key required skills"

        print("Score:", score, "| Decision:", result)

        return {
            "score": float(score),
            "decision": result,
            "matched_skills": matched,
            "missing_skills": missing,
            "reason": reason
        }

    except Exception as e:
        error_msg = f"FULL ERROR: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)

        with open("error.log", "a") as f:
            f.write(error_msg + "\n\n")

        return {"error": str(e)}