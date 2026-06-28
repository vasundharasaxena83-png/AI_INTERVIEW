import random

QUESTIONS = [
    "Tell me about yourself.",
    "Explain a machine learning project you worked on.",
    "What are your strengths?",
    "Why should we hire you?",
    "Explain Python decorators.",
    "How does a machine learning model work?"
]
def get_question():
    return random.choice(QUESTIONS)