import streamlit as st
import tempfile

from src.data_loader import extract_text_from_pdf
from src.preprocessing import clean_text
from src.matcher import rank_resumes

# Page config
st.set_page_config(
    page_title="Resume Matcher",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🧠 Resume Keyword Matcher</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Match resumes with job descriptions using NLP</div>', unsafe_allow_html=True)

st.markdown("---")

# Layout (2 columns)
col1, col2 = st.columns(2)

# Left column → Job Description
with col1:
    st.subheader("📄 Job Description")
    job_file = st.file_uploader("Upload JD (.txt)", type=["txt"])

# Right column → Resumes
with col2:
    st.subheader("📂 Resumes")
    resume_files = st.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

st.markdown("---")

# Process button
if st.button("🚀 Analyze Resumes"):

    if not job_file or not resume_files:
        st.warning("⚠️ Please upload both Job Description and Resumes")
    else:
        with st.spinner("Processing resumes..."):

            # Read JD
            job_desc = job_file.read().decode("utf-8")
            job_desc_clean = clean_text(job_desc)

            resumes = []
            names = []

            for file in resume_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(file.read())
                    tmp_path = tmp.name

                text = extract_text_from_pdf(tmp_path)
                text_clean = clean_text(text)

                resumes.append(text_clean)
                names.append(file.name)

            # Rank resumes
            ranked = rank_resumes(job_desc_clean, resumes, names)

        st.success("✅ Analysis Complete!")

        st.markdown("## 🏆 Ranking Results")

        # Display results
        for i, (name, score, keywords) in enumerate(ranked, 1):
            with st.container():
                st.markdown(f"### Rank #{i} — {name}")

                colA, colB = st.columns([1, 3])

                with colA:
                    st.metric(label="Score", value=f"{score:.2f}")

                with colB:
                    st.progress(float(score))

                st.write(f"**Matched Skills:** {', '.join(keywords)}")

                st.markdown("---")

else:
    st.info("Upload files and click 'Analyze Resumes' to start.")