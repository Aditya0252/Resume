from fastapi import FastAPI
from form_handler import get_form_data
from resume_builder import build_resume
from ats_analyzer import analyze_resume

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Resume Agent is up!"}

@app.post("/build-resume/")
def build_resume_api(option: int):
    form_data = get_form_data(option)
    resume_path = build_resume(form_data, option)
    ats_score = analyze_resume(resume_path)
    return {
        "resume_path": resume_path,
        "ats_score": ats_score
    }
