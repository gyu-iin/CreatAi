import streamlit as st
from openai import OpenAI

st.title("GPT-4O사용")
st.write("API KEY")
key = st.text_input('API KEY를 작성하세요', type="password")
client = OpenAI(api_key=f"{key}")

messages = [
    {"role": "system", "content": "너는 질문에 대답하는 AI야."}
]


# query = st.text_input('무엇을 묻고싶나요?')
# messages.append({"role": "user", "content": query})
# response = client.chat.completions.create(
#   model = "gpt-4o-mini",
#   messages = messages
# )
# st.write(f"{response.choices[0].message.content}")
# st.write("")
# messages.append({"role": "assistant", "content": response.choices[0].message.content})

img = st.text_input('생성하고싶은 이미지를 입력하세요')
response = client.images.generate(
    model="dall-e-3",
    prompt=img)
image_url = response.data[0].url
st.markdown("![alt text](image_url)")
