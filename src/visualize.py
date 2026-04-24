import matplotlib.pyplot as plt

def plot_scores(ranked):
    names = [r[0] for r in ranked]
    scores = [r[1] for r in ranked]

    plt.figure()
    plt.barh(names, scores)
    plt.xlabel("Similarity Score")
    plt.ylabel("Resumes")
    plt.title("Resume Ranking")

    # Highest score at top
    plt.gca().invert_yaxis()

    plt.tight_layout()

    # Save graph 
    plt.savefig("resume_ranking.png")
    print("Graph saved as resume_ranking.png")