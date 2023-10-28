import streamlit as st
from chatgpt import run  # I'm assuming chatgpt.run is your custom GPT-3 API function

def generate_prompt(role, history, is_init=False):
    base_prompt = f"""
    Now you are {role}.
    Theme is {theme}.
    Give me opinion with two sentences as {role}, following history.
    ###rule
    """
    if is_init:
        return base_prompt + "1. Opinion should be within 15 words."
    else:
        return base_prompt + f"""
        1. Absolutely return response for last conversation at 1st sentence. Then give your opinion.
        2. Follow the history.
        3. Opinion should be within 15 words.
        ###history
        {history}
        """

def generate_debate(roles, theme):
    history = []
    for idx, role in enumerate(roles):
        prompt = generate_prompt(role, history, is_init=(idx==0))
        response = run(role, prompt)
        history.append(response)
        avatar = ["🧑‍💻", "🤖", "👻"][idx]
        st.chat_message("ai", avatar=avatar).write(response)
    return history  # Return the history for use in summary generation


def generate_summary(history):
    prompt = f"""
    Based on the history, give me a lesson in Japanese.
    ###rule
    1. Lesson should be within 15 words.
    2. Answer should be in Japanese.
    ###history
    {history}
    """
    return run("You are a creative poemer", prompt)

# Streamlit UI
st.title('AI議論プラットフォーム')
st.header('テーマ選択')

# Get initial theme and roles\
theme = run("You are smart AI", "Give me just only theme within 5 words.\n Theme:")
roles = [run("You are smart AI", f"Give me just only one role within 2 words like lazy doctor, cold lawer \n Role:") for _ in range(3)]

st.header('議論')
st.write(f"選択されたテーマ: {theme}")
st.write(f"AIのロール: {', '.join(roles)}")

# Run the debate and get the history
history = generate_debate(roles, theme)

# Generate and display summary
st.header('名言生成')
st.write("議論から生まれた名言がこちらです。")
print(history)
summary = generate_summary(history)  # Pass the history to the summary function
st.write(summary)

st.button('再生成する')
