import streamlit as st
from openai import OpenAI

st.title("GPT-4O사용")
st.write("API KEY")
key = st.text_input("API KEY를 작성하세요", type="password")
client = OpenAI(api_key=f"{key}")

messages = [
    {"role": "system", "content": "너는 질문에 대답하는 AI야."}
]

while True:
  query = input("Enter your query: ")
  if query == "exit":
    break
  messages.append({"role": "user", "content": query})
  response = client.chat.completions.create(
      model = "gpt-4o-mini",
      messages = messages
  )
  print(response.choices[0].message.content)
  print("")
  messages.append({"role": "assistant", "content": response.choices[0].message.content})
