# 🧠 AI Interview Simulator & ATS Analytics Dashboard

An advanced, interactive technical assessment simulator designed using **Streamlit**, built to emulate production-grade hiring workflows used by product companies. Candidates can run simulation queries, process multi-format resumes, evaluate logic performance metrics, and review optimized framework blueprints.

---

## 🚀 Core Features

*   **⚡ Cognitive Guardrail Overlay:** A fixed introductory welcome modal pop-up that isolates the environment and displays structured guidelines before exposing workspace metrics.
*   **📊 Multi-Skill Analytics:** Evaluation matrix mapped via a Plotly performance pie chart assessing Python, Machine Learning, Projects, Communication, and Leadership depths.
*   **📋 ATS Resume Matrix Tracking:** Integrated `.pdf` and `.docx` parser mapping essential keyword indicators (SQL, Deep Learning, NLP, Pandas, TensorFlow) on a side-by-side color-coded bar chart.
*   **🌟 Star Reference Template:** Dynamically slides open a perfect response blueprint utilizing the Context-Action-Result structural methodology.
*   **🎨 Cyberpunk Premium UI:** Implements custom CSS injection featuring linear-gradient animated backdrops, neon typography effects, and responsive widget grids.

---

## 📁 Project Structure

```text
AI_INTERVIEW_SIMULATOR/
│
├── app.py                      # Core Dashboard & UI Execution Matrix
├── requirements.txt            # System dependencies
│
└── core/
    ├── question_bank.py        # Question bank evaluation queries
    ├── evaluator.py            # Response parsing scoring logic
    └── utils.py                # ATS parsing & skill metrics matrix
