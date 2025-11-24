import streamlit as st
from google import genai

# -----------------------------
#  CONFIG
# -----------------------------
st.set_page_config(page_title="Sindhi Dictionary", page_icon="📘")

st.title("📘 Sindhi To Sindhi Dictionary")
st.title("🧠 Created by Irshad Ali Siper")
st.write("Write any Sindhi word to get its meaning.")

# User enters API key
# api_key = st.text_input("Enter your Gemini API Key", type="password")
API_KEY = "AIzaSyDiK7rf9NB2hepBLeXLsmdQGujzkXPUpuY"

# Word input
word = st.text_input("Enter Sindhi word:",placeholder="هتي سنڌي لفظ لکو")

# Output area
if st.button("Get Meaning"):
    if not API_KEY:
        st.error("Please enter your Gemini API Key.")
    elif not word.strip():
        st.error("Please enter a Sindhi word.")
    else:
        try:
            client = genai.Client(api_key=API_KEY)

            prompt = f"""
            You are a Sindhi dictionary.  
            Provide the meaning of the Sindhi word **in Sindhi language only**.
            Word in words format like real dictionary not detail  if user ask other question like 
            general question say sorry I resolve just dictionary related queries.: {word}
            """

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            meaning = response.text

            st.success("Meaning:")
            st.write(meaning)

        except Exception as e:
            st.error(f"Error: {e}")
