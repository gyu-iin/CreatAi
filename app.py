import streamlit as st
from openai import OpenAI

st.title("GPT-4O mini 사용")
st.write("API KEY")
key = st.text_input('API KEY를 작성하세요', type="password")
client = OpenAI(api_key=f"{key}")

prompt = st.text_area("Prompt")

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
st.text(answer)
