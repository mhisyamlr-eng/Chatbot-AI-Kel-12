import streamlit as st
from tmdb_api import search_movie, format_movie_info

st.set_page_config(page_title="Movie AI", page_icon="🎬")

st.title("🎥 Movie AI Chatbot")
st.caption("Your personal movie assistant 🍿")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! 👋 Tell me a movie title and I'll give you details + insights!"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
if prompt := st.chat_input("Type a movie title..."):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    # Search movie
    movie = search_movie(prompt)

    if movie:
        reply = format_movie_info(movie)
    else:
        reply = f"😢 I couldn't find **'{prompt}'**. Try another movie title!"

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)
