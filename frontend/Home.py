import streamlit as st
from PIL import Image

# Carga la fuente Inter
st.markdown(
    """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap" rel="stylesheet">
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    font-size: 1.05rem;
    background-color: #0e1117;
    color: #f5f5f5;
    line-height: 1.7;
}

h1 { font-size: 2.9rem; font-weight: 800; color: #fff; margin-bottom: 0.5em; }
h2 { font-size: 2.1rem; font-weight: 700; color: #f0f0f0; }
h3 { font-size: 1.5rem; font-weight: 600; color: #dddddd; }

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}
.stTabs [data-baseweb="tab"] {
    background-color: #1f222a;
    border-radius: 10px 10px 0 0;
    padding: 0.6em 1.2em;
    font-weight: 600;
    font-size: 1.02rem;
    color: #c9c9c9;
}
.stTabs [data-baseweb="tab"][aria-selected="true"] {
    background-color: #313843;
    color: #ffffff;
    border-bottom: 2px solid #e74c3c;
}
.stButton>button, .stDownloadButton>button {
    background-color: #e74c3c;
    color: white;
    border-radius: 8px;
    padding: 0.6em 1.2em;
    font-weight: bold;
}
.stTextInput>div>div>input {
    background-color: #1f1f1f;
    color: white;
    border-radius: 8px;
    padding: 0.5em;
}
a {
    color: #f39c12;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}
</style>
""",
    unsafe_allow_html=True,
)


# -------------------------
# SIDEBAR - Información personal
# -------------------------
img = Image.open("frontend/assets/avatar_cyberpunk.png")
st.sidebar.image(img, use_container_width=True)

st.sidebar.markdown("## 👨‍💻 Miguel Barrios")
st.sidebar.markdown("**Machine Learning & MLOps Engineer**")

st.sidebar.markdown("### 🛠 Stack")
st.sidebar.markdown(
    """
- **Python, PyTorch, TensorFlow, OpenAI, NLP**  
- **Kafka, Snowflake, SQL, Elasticsearch**  
- **AWS, Azure, Kubernetes, Docker, GitLab CI/CD**  
- **Grafana, Prometheus**
"""
)

st.sidebar.markdown("### 🌍 Languages")
st.sidebar.markdown("**🇬🇧 English:** C1  \n**🇪🇸 Spanish:** Native")

st.sidebar.markdown("### 🔗 Links")
st.sidebar.markdown(
    """
- [GitHub](https://github.com/MiguelBarriosAl)  
- [LinkedIn](https://www.linkedin.com/in/miguel-barrios-alvarez)  
- [ILM Article](https://medium.com/@mbarriosa339/ilm-data-rollover-in-elasticsearch-abd7fbfbb7a2)  
- [Mapping Article](https://medium.com/@mbarriosa339/elasticsearch-nested-field-type-the-importance-of-defining-the-mapping-of-the-index-9ac8d01ba7a8)
"""
)

st.sidebar.markdown("### 🎓 Certifications")
st.sidebar.markdown(
    """
- AWS ML Specialty *(in progress)*  
- Kubernetes for MLOps – Udemy  
- Elasticsearch – Udemy
"""
)

# -------------------------
# MAIN PAGE - Contenido principal
# -------------------------
st.title("🚀 Welcome to my AI Portfolio")
st.markdown(
    "Hi! I'm Miguel, an MLOps and ML Engineer passionate about building intelligent, production-ready systems. Below you can explore my work and skills."
)

# Secciones con pestañas
tabs = st.tabs(["🤖 AI Assistant", "🧠 About Me", "📁 Projects", "📄 CV"])

with tabs[0]:
    st.header("Ask the AI Assistant")
    question = st.text_input(
        "Ask me something about my experience, skills, or projects:"
    )
    if st.button("Ask"):
        if question:
            from utils import ask_question

            response = ask_question(question)
            st.success(f"🤖 {response}")
        else:
            st.warning("Please enter a question to ask the assistant.")

with tabs[1]:
    st.header("🚀 About Me")
    st.markdown(
        """
I'm a **Machine Learning & Data Engineer** with a passion for delivering **AI-powered solutions** that create real business impact.

✅ Developed **Feature Stores** that reduced fraud detection retrieval time by 30%.  
✅ Built **scalable data pipelines** handling millions of transactions/day.  
✅ Designed **document classification systems** using LLMs (OpenAI).  
✅ Proficient in **cloud-native ML deployment** with Kubernetes, Docker and MLOps tools.

I combine technical depth with business-driven thinking to build solutions that scale, automate, and deliver value fast.
"""
    )

    st.markdown("### 🌐 Connect with me")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            "[![GitHub](https://img.shields.io/badge/GitHub-000?style=flat&logo=github&logoColor=white)](https://github.com/MiguelBarriosAl)"
        )
    with col2:
        st.markdown(
            "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/miguel-barrios-alvarez/)"
        )
    with col3:
        st.markdown(
            "[![Medium](https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/@mbarriosa339)"
        )


with tabs[2]:
    st.header("📁 Key Projects")

    st.markdown("### 🔹 MLOps Platform for Fraud Detection *(INTELYGENZ)*")
    st.markdown(
        """
- Designed a **Feature Store** to support real-time fraud detection — improved model retrieval times by **30%**.
- Built **ETL pipelines** handling millions of records/day, improving ingestion speed by **40%**.
- Developed an **LLM-based document classifier** for banking automation.
    """
    )

    st.markdown("### 🔹 AI Web Scraping & Classification *(ENTHEC SOLUTIONS)*")
    st.markdown(
        """
- Engineered a **high-performance Elasticsearch architecture** for strategy indexing and allocation.
- Integrated **BeautifulSoup + BERT** for automatic webpage categorization with high accuracy.
    """
    )

    st.markdown("### 🔹 Web App with AI Capabilities *(ATK)*")
    st.markdown(
        """
- Developed a web application allowing users to apply **AI algorithms** for text analysis.
    """
    )


with tabs[3]:
    st.header("Download CV")
    with open("data/dev/Miguel_Barrios.pdf", "rb") as f:
        st.download_button(
            label="📥 Download CV",
            data=f,
            file_name="Miguel_Barrios_CV.pdf",
            mime="application/pdf",
        )

st.sidebar.markdown("### 🌐 Connect with me")

col1, col2, col3 = st.sidebar.columns(3)
with col1:
    st.markdown(
        "[![GitHub](https://img.shields.io/badge/GitHub-000?style=flat&logo=github&logoColor=white)](https://github.com/MiguelBarriosAl)"
    )
with col2:
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/miguel-barrios-alvarez/)"
    )
with col3:
    st.markdown(
        "[![Medium](https://img.shields.io/badge/Medium-12100E?style=flat&logo=medium&logoColor=white)](https://medium.com/@mbarriosa339)"
    )
