from collections import Counter

def analyze_resume(path: str) -> float:
    # Load and read resume text
    from docx import Document
    doc = Document(path)
    text = "\n".join([para.text for para in doc.paragraphs])
    
    keywords = ["Python", "Machine Learning", "API", "FastAPI", "Resume", "LLM"]  # Example set
    word_count = Counter(text.split())
    score = sum(word_count[k] for k in keywords if k in word_count)
    
    max_possible = len(keywords) * 3  # assume ideal frequency is 3 per keyword
    return round((score / max_possible) * 100, 2)
