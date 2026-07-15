# Install library
!pip install -q google-generativeai

import google.generativeai as genai

# -------------------------------
# Paste your Gemini API Key here
# -------------------------------
API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_question():
    q = input("\nAsk your question: ")
    response = model.generate_content(q)
    print("\nAnswer:")
    print(response.text)

def generate_quiz():
    topic = input("\nEnter topic: ")
    prompt = f"""
    Generate 5 multiple choice questions on {topic}.
    Give four options and mention the correct answer at the end.
    """
    response = model.generate_content(prompt)
    print("\nQuiz:\n")
    print(response.text)

def summarize():
    text = input("\nPaste text to summarize:\n")
    prompt = f"Summarize this in simple points:\n{text}"
    response = model.generate_content(prompt)
    print("\nSummary:\n")
    print(response.text)

def roadmap():
    subject = input("\nEnter subject: ")
    prompt = f"Create a beginner to advanced learning roadmap for {subject}."
    response = model.generate_content(prompt)
    print("\nLearning Roadmap:\n")
    print(response.text)

while True:
    print("\n===== EduGenie =====")
    print("1. Ask Question")
    print("2. Generate Quiz")
    print("3. Summarize Text")
    print("4. Learning Roadmap")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        ask_question()
    elif choice == "2":
        generate_quiz()
    elif choice == "3":
        summarize()
    elif choice == "4":
        roadmap()
    elif choice == "5":
        print("Thank you for using EduGenie!")
        break
    else:
        print("Invalid Choice!")