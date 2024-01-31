import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')
#initiate the chathistory
if 'messages' not in st.session_state:
    st.session_state.messages=[
        {
            "role":"assistant",
            "content":"Ask me anything"
        }
    ]
# Displying chathistory on restart.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# Process, display and store query and response.
def llm_function(Query):
    response = model.generate_content(Query)
    # Displaying users message and assistant response as well.
    with st.chat_message('user'):
        st.markdown(Query)
    with st.chat_message('assistant'):
        st.markdown(response.text)
    # Storing user message and query
    st.session_state.messages.append(
        {
            'role':'user',
            'content':Query
        }
    )
    st.session_state.messages.append(
        {
            'role':'assitant',
            'content':response.text
        }
    )
query = st.chat_input("hey hey what's up big boi")
if query:
    llm_function(query)