import streamlit as st
import plotly.express as px

from core.question_bank import get_question
from core.evaluator import evaluate_answer
from core.utils import ats_score

from pypdf import PdfReader
import docx

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Interview Simulator",
    layout="wide"
)

# ---------------- PREMIUM UI & CUSTOM STYLES ----------------
st.markdown("""
<style>

/* Animated Background */
.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e1b4b, #0b1220, #1f1147);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    color: white;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Title */
h1, h2, h3 {
    color: #ff4ecd;
    text-shadow: 0px 0px 10px #38bdf8;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #38bdf8, #ff4ecd);
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 15px #ff4ecd;
}

/* Text area */
textarea {
    background-color: rgba(30, 41, 59, 0.8) !important;
    color: white !important;
    border-radius: 10px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1220, #1e1b4b);
}

/* Metrics */
div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 10px;
}

/* Custom Styled Slide Expander Box */
.stExpander {
    background: rgba(30, 41, 59, 0.5) !important;
    border: 1px solid #38bdf8 !important;
    border-radius: 12px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- FUNCTIONS ----------------
def extract_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    return text


def extract_text(file, file_type):
    if file_type == "pdf":
        return extract_pdf(file)
    elif file_type == "docx":
        return extract_docx(file)
    return ""

# ---------------- SESSION STATES ----------------
if "question" not in st.session_state:
    st.session_state.question = get_question()

if "history" not in st.session_state:
    st.session_state.history = []

if "ats" not in st.session_state:
    st.session_state.ats = 0

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

# Controls whether the overlay rules modal slide panel is active
if "show_welcome_modal" not in st.session_state:
    st.session_state.show_welcome_modal = True
    
# ---------------- PRE-DASHBOARD WELCOME POP-UP ----------------
if st.session_state.show_welcome_modal:
    st.markdown("""
        <div style="
            position: fixed; 
            top: 15%; 
            left: 20%; 
            width: 60%; 
            background: linear-gradient(135deg, #0f172a, #1e1b4b); 
            border: 2px solid #ff4ecd; 
            border-radius: 20px; 
            padding: 35px; 
            z-index: 99999;
            box-shadow: 0px 0px 30px rgba(255, 78, 205, 0.6);
            color: white;
        ">
            <h1 style='color: #ff4ecd; text-shadow: 0px 0px 10px #38bdf8; margin-top: 0;'>📝 Simulation Rules & Guidelines</h1>
            <p style='font-size: 16px; line-height: 1.6;'>Welcome to the assessment interface. To optimize your technical positioning indicators, please follow these deployment guidelines:</p>
            <ul style='font-size: 15px; line-height: 1.8;'>
                <li>🚀 <strong style='color: #38bdf8;'>Keyword Targeting:</strong> Utilize specialized identifiers such as <code>Python</code>, <code>Machine Learning</code>, or framework terms directly in your technical logic responses.</li>
                <li>📝 <strong style='color: #38bdf8;'>STAR Framework:</strong> Structure descriptive answers clearly breaking down your <em>Situation, Task, Action, and Results</em>.</li>
                <li>⏳ <strong style='color: #38bdf8;'>Depth Optimization:</strong> Elaborate completely. Formulating detailed descriptions above 40 words targets higher communication score metrics.</li>
            </ul>
            <p style='font-size: 14px; color: #94a3b8; margin-top: 20px;'>You may upload your tracking resume for ATS parsing via the left navigation tree once initialized.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚀 Start Interview Simulation"):
        st.session_state.show_welcome_modal = False
        st.rerun()

# ---------------- MAIN APP SYSTEM (UNLOCKED AFTER POP-UP CLOSE) ----------------
else:
    # ---------------- HEADER ----------------
    st.title("🧠 AI Interview Simulator")
    st.markdown("### 🚀 AI Interview Practice Dashboard")

    # ---------------- SIDEBAR ----------------
    st.sidebar.title("📊 Dashboard")
    uploaded_file = st.sidebar.file_uploader(
        "📄 Upload Resume (PDF / DOCX)",
        type=["pdf", "docx"],
        key="resume_uploader_unique"
    )

    if uploaded_file is not None:
        file_type = uploaded_file.name.split(".")[-1]
        st.session_state.resume_text = extract_text(uploaded_file, file_type)
        st.session_state.ats = ats_score(st.session_state.resume_text)
        st.sidebar.success("Resume Uploaded Successfully!")
        st.sidebar.metric("📊 ATS Score", f"{st.session_state.ats}/100")

    st.sidebar.metric("🧠 Interviews Taken", len(st.session_state.history))

    # ---------------- TOP METRICS ----------------
    col1, col2 = st.columns(2)
    col1.metric("📌 Current Question", "Active")
    col2.metric("🧠 System Status", "AI Ready")

    # ---------------- RETRO SLIDE EXPANDER (FOR REVIEWING GUIDELINES) ----------------
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("💡 Re-open Simulation Guidelines & Hacks", expanded=False):
        st.markdown("""
        ### 🎯 Premium Simulation Rules
        * 🚀 **Keyword Targeting:** Include explicit terms like `Python`, `Machine Learning`, or specific framework toolsets to score higher.
        * 📝 **The STAR Method:** Structure your project responses by giving the *Situation, Task, Action, and Final Result*.
        * ⏳ **Answer Depth:** Keep your responses descriptive. Explaining technical logic behind your answers earns up to 40 additional metrics.
        """)

    # ---------------- QUESTION BLOCK ----------------
    st.subheader("🎯 Interview Question")
    st.info(st.session_state.question)

    if st.button("🔄 New Question"):
        st.session_state.question = get_question()
        st.rerun()

    # ---------------- ANSWER INPUT ----------------
    answer = st.text_area("✍️ Your Answer")

    # ---------------- SUBMIT LOGIC ----------------
    if st.button("Submit Answer"):
        if not answer.strip():
            st.warning("Please type an answer before submitting!")
        else:
            result = evaluate_answer(answer)
            scores = result["scores"]

            st.session_state.history.append(result)

            st.success(f"Score: {result['total']}/100")
            st.write("💡 Feedback:", result["feedback"])

            # Chart Columns Display Matrix
            chart_col1, chart_col2 = st.columns(2)

            # ---------------- PIE CHART ----------------
            with chart_col1:
                st.subheader("📊 Skill Breakdown")
                names = ["Python", "Machine Learning", "Projects", "Communication", "Leadership"]
                values = [
                    scores.get("python", 0),
                    scores.get("machine learning", 0),
                    scores.get("projects", 0),
                    scores.get("communication", 0),
                    scores.get("leadership", 0)
                ]

                fig_pie = px.pie(
                    names=names,
                    values=values,
                    title="Interview Performance Weights"
                )
                fig_pie.update_traces(marker=dict(colors=["#38bdf8", "#ff4ecd", "#6366f1", "#22d3ee", "#f59e0b"]))
                st.plotly_chart(fig_pie, use_container_width=True)

            # ---------------- ATS RESUME BAR CHART ----------------
            with chart_col2:
                st.subheader("📋 ATS Keyword Tracker")
                
                target_skills = ["python", "machine learning", "deep learning", "sql", "nlp", "pandas", "tensorflow"]
                text_lower = st.session_state.resume_text.lower()
                match_status = [100 if skill in text_lower else 0 for skill in target_skills]
                display_skills = [skill.upper() for skill in target_skills]

                fig_bar = px.bar(
                    x=display_skills,
                    y=match_status,
                    labels={'x': 'Core Domain Skills', 'y': 'Match Status (%)'},
                    title="Resume Skill Matrix Presence Mapping",
                    color=match_status,
                    color_continuous_scale=["#ef4444", "#22c55e"]
                )
                fig_bar.update_layout(showlegend=False, coloraxis_showscale=False)
                st.plotly_chart(fig_bar, use_container_width=True)

    # ---------------- INTERVIEW RUN HISTORY ----------------
    st.subheader("📜 Interview History")

    for i, h in enumerate(st.session_state.history[::-1]):
        st.markdown(f"**Attempt {i+1} → Score: {h['total']}/100**")
        st.write("💡 Feedback:", h["feedback"])
        st.markdown("---")