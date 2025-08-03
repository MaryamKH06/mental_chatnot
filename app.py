import streamlit as st
from openai import OpenAI
import os

# OpenAI istemcisi
client = OpenAI()

def get_response(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Sen kullanıcıya moral veren, motive edici ve kibar bir asistansın."},
            {"role": "user", "content": user_input}
        ],
        model="gpt-3.5-turbo"
    )
    return chat_completion.choices[0].message.content

st.set_page_config(page_title="Mini Mental Destek Botu 🧠", page_icon="💙")
st.title("🧠 Mini Mental Destek Chatbotu")
st.write("Duygularını paylaş, ben de seni motive edeyim.")

user_input = st.text_input("Bugün nasıl hissediyorsun?")

if user_input:
    with st.spinner("Yanıt hazırlanıyor..."):
        response = get_response(user_input)
        st.success("💬 Bot cevabı:")
        st.markdown(f"> {response}")
