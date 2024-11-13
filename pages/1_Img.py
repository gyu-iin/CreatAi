prompt = st.session_state.prompt
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    n=1,
    size="1024x1024"
)
image_url = response.data[0].url

if image_url:
    st.markdown(f"![{prompt}]({image_url})")
