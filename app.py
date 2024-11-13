import streamlit as st
from openai import OpenAI

@st.cache_data
def ask_answer(prompt):
    messages = [
        {"role": "user", "content": prompt}
    ]
    
    answer = ''
    
    if st.button("Generate"):
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = messages
        )
        answer = response.choices[0].message.content
    return answer

st.title("GPT-4O mini 사용")
st.write("API KEY")
Apikey = st.text_input('API KEY를 작성하세요', type="password")
st.session_state.Apikey
client = OpenAI(api_key=f"{Apikey}")

prompt = st.text_area("Prompt")
st.text(ask_answer(prompt))
