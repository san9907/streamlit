import streamlit as st

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("채팅을 입력하세요")

if st.button("전송"):
    st.session_state.chat_history.append(user_input) 

for message in st.session_state.chat_history:
    st.write(message)