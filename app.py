import streamlit as st
import subprocess

st.title("AI Interview Assistant (Local LLM - Ollama)")

role = st.text_input("Enter Job Role", "Data Analyst")
context = st.text_area("Paste Resume / JD (RAG)")

def ask_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout

if st.button("Generate Question"):
    prompt = f"""
    You are an interviewer.

    Based on this context:
    {context}

    Ask one interview question for {role}.
    """

    question = ask_ollama(prompt)
    st.session_state["question"] = question

    st.write("Question:")
    st.write(question)

if "question" in st.session_state:

    answer = st.text_area("Your Answer")

    if st.button("Evaluate Answer"):

        eval_prompt = f"""
        Question: {st.session_state['question']}
        Answer: {answer}

        Give feedback and ask a follow-up question.
        """

        feedback = ask_ollama(eval_prompt)

        st.write("Feedback:")
        st.write(feedback)
