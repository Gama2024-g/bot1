import streamlit as st
from openai import OpenAI

st.balloons()
# Show title and description.
st.title("  💬 Bienvenido a mi primer app  ")
st.write(
   "Este es mi primer app con IA. "
   "Te comparto el link para que entres y te deleites [here](https://platform.openai.com/account/api-keys). "
   "Para aprender a realizar el tuyo puedes entrar al siguiente tutoria, ponte chingon [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)
openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("What is up?")
if prompt==None:
   st.stop()

with st.chat_message("user"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.

stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0.3,
    )
respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
   st.write(respuesta)
