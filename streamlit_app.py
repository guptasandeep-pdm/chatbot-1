import streamlit as st
import requests
import textwrap

# Your Colab URL (replace this with the actual ngrok URL)
colab_url = "http://127.0.0.1:5000"

# Streamlit UI setup
st.title("Chatbot for Ops Team")
st.write("Ask any question for Ops support!")

user_input = st.text_input("Your Question:")

if user_input:
    # Send request to Colab API
    response = requests.post(colab_url, json={"input": user_input})
    
    if response.status_code == 200:
        answer = response.json()["answer"]
        st.write("**Answer**:")
        st.write(answer)
    else:
        st.write("Error: Unable to get a response from the chatbot.")
