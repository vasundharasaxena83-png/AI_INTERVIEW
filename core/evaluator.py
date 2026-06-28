def evaluate_answer(answer: str):
    answer = answer.lower()

    scores = {
        "python": 0,
        "machine learning": 0,
        "projects": 0,
        "communication": 0,
        "leadership": 0
    }

    feedback = []

    # Python detection
    if "python" in answer:
        scores["python"] = 30

    # ML detection
    if "machine learning" in answer or "ml" in answer:
        scores["machine learning"] = 30

    # Project detection
    if "project" in answer:
        scores["projects"] = 25

    # Communication scoring (IMPORTANT FIX)
    word_count = len(answer.split())
    if word_count > 20:
        scores["communication"] = 15
    else:
        scores["communication"] = 5

    # Leadership scoring
    if "lead" in answer:
        scores["leadership"] = 20

    total = sum(scores.values())

    if total == 0:
        feedback.append("Try adding keywords like Python, ML, Projects")
    else:
        feedback.append("Good structured answer")

    return {
        "scores": scores,
        "total": total,
        "feedback": ", ".join(feedback)
    }