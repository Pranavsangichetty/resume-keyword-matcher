from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract matched keywords
def get_matched_keywords(job_desc, resume):
    job_words = set(job_desc.split())
    resume_words = set(resume.split())

    matched = job_words.intersection(resume_words)

    return list(matched)[:10]


# Rank resumes
def rank_resumes(job_desc, resumes, names):
    documents = [job_desc] + resumes

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]

    ranked = sorted(
        zip(names, resumes, scores),
        key=lambda x: x[2],
        reverse=True
    )

    results = []
    for name, resume, score in ranked:
        keywords = get_matched_keywords(job_desc, resume)
        results.append((name, score, keywords))

    return results