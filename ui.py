import streamlit as st
import requests
import subprocess
import atexit
import os
import signal

def main():
    st.title("Free Multilingual RAG")

    tabs = ["Upload Document", "Ask Question"]
    active_tab = st.radio("Upload documents first, ask questions later:", tabs)
    
    if active_tab == "Upload Document":
        upload_document()
    elif active_tab == "Ask Question":
        ask_question()

def upload_document():
    st.write("Several files can be uploaded, each upload crushes the old one. Depending on the number and size of files, the upload process may take a long time.")

    username = st.text_input("Enter a username (just something that represents you):")
    uploaded_files = st.file_uploader("Upload your documents:", accept_multiple_files=True)

    if uploaded_files:
        st.write("Number of uploaded files:", len(uploaded_files))
        
        for uploaded_file in uploaded_files:
            file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
            st.write(file_details)
                
        files = [("files", (uploaded_file.name, uploaded_file, uploaded_file.type)) for uploaded_file in uploaded_files]
        
        payload = {'username': username}
        
        with st.spinner('Loading...'):
            response =  requests.post("http://localhost:8000/document-uploader/", files=files, data=payload)
        
        if response.status_code == 200:
            st.success(response.text)
        else:
            st.error("Error:", response.text)


def ask_question():
    username = st.text_input("Enter a username (just something that represents you):") 
    api_key = st.text_input("Add your Google API key. It is free. Key acquisition video: [https://www.youtube.com/watch?v=brCkpzAD0gc]: (If you do not trust you can download and use the app in your local too)", type="password")
    question = st.text_area("Enter the question you want to ask in your document (the more detailed your question, the more accurate an answer you will get): ")
    
    if st.button("Ask"):
        if not question:
            st.warning("Please enter a question.")
        elif not username:
            st.warning("Please enter a username.")
        else:
            payload = {'username': username, 'question': question, 'api_key': api_key}
            
            with st.spinner('Question is getting answered...'):
                response = requests.post("http://localhost:8000/question-answerer/", data=payload)
            
            if response.status_code == 200:
                st.success("Answer: " + response.text)
            else:
                print(response)
                st.error("Error:", response.text)

uvicorn_process = None

def run_fastapi():
    global uvicorn_process
    if uvicorn_process is None:
        uvicorn_process = subprocess.Popen(["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000"])
        print("FastAPI server has been started.")

def cleanup():
    global uvicorn_process
    if uvicorn_process:
        os.kill(uvicorn_process.pid, signal.SIGTERM)
        uvicorn_process.wait()
        print("FastAPI server has been closed.")

if __name__ == "__main__":
    run_fastapi()
    atexit.register(cleanup)
    main()