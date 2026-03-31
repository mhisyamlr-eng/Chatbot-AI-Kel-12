import streamlit as st
from tmdb_api import search_movie, format_movie_info

st.title("🎥 Movie Info Chatbot")
st.caption("Ask me about any movie! Just type the title.")
# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
# Display the existing conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
# Handle new user input
if prompt := st.chat_input("Type a movie title..."):
    # Display and save the user's message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    # Call the API and generate a bot reply
    movie = search_movie(prompt)
    if movie:
        reply = format_movie_info(movie)
    else:
        reply = f"Sorry, I couldn't find anything for **'{prompt}'**. Try another title!"
    # Display and save the bot's reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
        