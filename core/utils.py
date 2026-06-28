def ats_score(resume_text: str):
    resume_text = resume_text.lower()

    skills = [
        "python",
        "machine learning",
        "deep learning",
        "sql",
        "nlp",
        "pandas",
        "tensorflow",
        "communication",
        "leadership",
        "problem solving",
        "teamwork",
        "project management",
        "data analysis",
        "data visualization",
    ]

    found = 0

    for skill in skills:
        if skill in resume_text:
            found += 1

    score = int((found / len(skills)) * 100)

    return score