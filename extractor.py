import os
import re
import pdfplumber
from datetime import datetime

INPUT_FOLDER = r"C:\Users\AdityaHiremath\Desktop\resume_agent_backend\resumes"
OUTPUT_FOLDER = "extracted_markdowns"

# Create output folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    """Extracts text from all pages of the PDF."""
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    return text

def extract_fields(text):
    """Extract fields like name, email, phone, etc., from the resume text."""
    # Extract Name (assuming the name is in the first few lines)
    name = re.findall(r"(?i)(?<=Name:)\s*[A-Za-z\s]+", text)
    
    # Extract Email
    email = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    
    # Extract Phone Number
    phone = re.findall(r"\+?\d[\d\s-]{8,}", text)
    
    # Extract Skills (simple example, you can improve this)
    skills = re.findall(r"(?i)(?<=Skills:)[^\n]+", text)
    
    # Extract LinkedIn Profile (if any)
    linkedin = re.findall(r"(https?://(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+)", text)

    # You can add more regular expressions for other fields like Education, Experience, etc.

    return {
        "name": name[0].strip() if name else "N/A",
        "email": email[0] if email else "N/A",
        "phone": phone[0] if phone else "N/A",
        "skills": skills[0].strip() if skills else "N/A",
        "linkedin": linkedin[0][0] if linkedin else "N/A"
    }

def convert_to_md(data, filename):
    """Converts the extracted data into Markdown format."""
    md_template = f"""# Resume: {data['name']}

**Email:** {data['email']}  
**Phone:** {data['phone']}  
**Skills:** {data['skills']}  
**LinkedIn:** {data['linkedin']}  

---
"""
    return md_template

def save_markdown(data, original_filename):
    """Saves the extracted data as a Markdown file."""
    md_content = convert_to_md(data, original_filename)
    md_path = os.path.join(OUTPUT_FOLDER, original_filename.replace(".pdf", ".md"))
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

def extract_and_convert_all(input_dir, output_dir):
    """Extracts data from all PDFs and converts to Markdown."""
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file)
            print(f"Processing {file}...")
            try:
                text = extract_text_from_pdf(pdf_path)
                data = extract_fields(text)
                save_markdown(data, file)
                print(f"[✓] Extracted: {file}")
            except Exception as e:
                print(f"[!] Error processing {file}: {e}")

if __name__ == "__main__":
    extract_and_convert_all(INPUT_FOLDER, OUTPUT_FOLDER)
