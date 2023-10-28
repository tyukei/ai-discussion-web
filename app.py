import streamlit as st
from chatgpt import run

theme = ""
roles= list(list())
conservations = list(list())

def get_ai(num):
    prompt =f"""
    Now you are {roles[num]}.
    Theme is {theme}.
    Give me opinion with two sentences as {roles[num]}, following history.
    ###rule
    1. Absolutely return response for last conversation at 1st sentence. Then give your opinion.
    2. Follow the history.
    3. Opinion should be within 15 words.
    ###history
    {conservations}
    """
    return run(roles[num], prompt)
    
def get_ai_init(num):
    prompt =f"""
    Now you are {roles[num]}.
    Theme is {theme}.
    Give me opinion with two sentences as {roles[num]}, following history.
    ###rule
    1. Opinion should be within 15 words.
    """
    return run(roles[num], prompt)

def get_summary():
    prompt =f"""
    Based on the history, give me lesson in Japanese.
    ###rule
    1. Lesson should be within 15 words.
    2. Answer should be in Japanese.
    ###history
    {conservations}
    """
    return run("You are a creative poemer", prompt)

# UI for Topic Selection (You can replace this with AI-based logic)
st.title('AI議論プラットフォーム')
st.header('テーマ選択')

with st.spinner('AI is thinking...'):
    theme = run("You are smart AI", "Give me just only theme within 5words.\n Theme:")
    role1 = run("You are smart AI", "Give me just only one role within 2 words like lazy doctor, cold lawer \n Role:")
    roles.append(role1)
    role2 = run("You are smart AI", "Give me just only one role within 2 words like lazy doctor, cold lawer \n Role:")
    roles.append(role2)
    role3 = run("You are smart AI", "Give me just only one role within 2 words like lazy doctor, cold lawer \n Role:")
    roles.append(role3)

# UI for Debate
st.header('議論')
st.write(f"選択されたテーマ: {theme}")
st.write(f"AIのロール: {role1}, {role2}, {role3}")

# Placeholder for debate content
debate_placeholder = st.empty()

with st.spinner('AI is thinking...'):
    role1_says = get_ai_init(0)
    conservations.append(role1_says)
    st.chat_message("ai",avatar="🧑‍💻").write(role1_says)


with st.spinner('AI is thinking...'):
    role2_says = get_ai(1)
    conservations.append(role2_says)
    st.chat_message("ai",avatar="🤖").write(role2_says)


with st.spinner('AI is thinking...'):
    role3_says = get_ai(2)
    conservations.append(role3_says)
    st.chat_message("ai",avatar="👻").write(role3_says)




# UI for Generated Quote
st.header('名言生成')
st.write("議論から生まれた名言がこちらです。")
quote_placeholder = st.empty()


with st.spinner('AI is thinking...'):
    sample_quote = get_summary()
    st.write(sample_quote)

st.button('再生成する')
