import nltk

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from src.data_loader import load_resumes, load_job_description
from src.preprocessing import clean_text
from src.matcher import rank_resumes
from src.visualize import plot_scores   

# Load data
names, resumes = load_resumes("data/resumes/")
job_desc = load_job_description("data/job_description.txt")

# Clean data
job_desc = clean_text(job_desc)
resumes = [clean_text(r) for r in resumes]

# Rank resumes
ranked = rank_resumes(job_desc, resumes, names)

# Show only top 10
ranked = ranked[:10]

# Output
print("\n" + "="*50)
print("🏆 RESUME RANKING RESULTS")
print("="*50)

for i, (name, score, keywords) in enumerate(ranked, 1):
    print(f"\nRank #{i}")
    print(f"Resume: {name}")
    print(f"Score : {score:.2f}")
    print(f"Matched Skills: {', '.join(keywords)}")

plot_scores(ranked)