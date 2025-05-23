import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Support Chatbot", page_icon="💬")

st.title("💬 AI-Powered Human Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful human support assistant."}
    ]

for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask me anything about your issue...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages,
                temperature=0.6,
            )
            bot_reply = response.choices[0].message.content
            st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
