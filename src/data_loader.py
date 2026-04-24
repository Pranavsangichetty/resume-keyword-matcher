import os
import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
    return text

def load_resumes(folder_path):
    resumes = []
    names = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            text = extract_text_from_pdf(path)

            resumes.append(text)
            names.append(file)

    return names, resumes

def load_job_description(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()