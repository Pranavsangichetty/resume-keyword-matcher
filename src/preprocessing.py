import re
import nltk
from nltk.corpus import stopwords

# ✅ Ensure stopwords work in Streamlit Cloud
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


# Normalize important multi-word skills
def normalize_skills(text):
    text = text.lower()
    text = text.replace("power bi", "powerbi")
    text = text.replace("machine learning", "machinelearning")
    text = text.replace("data analysis", "dataanalysis")
    text = text.replace("data visualization", "datavisualization")
    return text


# Main cleaning function (IMPORTANT — this must exist)
def clean_text(text):
    text = normalize_skills(text)

    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    words = text.split()

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    return " ".join(words)