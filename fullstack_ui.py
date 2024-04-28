import streamlit as st
from service import upload_documents, ask_question
from user import User
from fastapi import UploadFile

async def main():
    st.title("Ücretsiz Türkçe RAG")
    
    st.write("Birkaç dosya yüklenebilir, her yükleme eskisini ezer. Dosya sayısına ve büyüklüğüne göre yükleme işlemi uzun sürebilir.")

    # Username input box
    username = st.text_input("Kullanıcı adı girin (sizi temsil edecek bir şey olması yeterli):")
    
    # API key input box
    api_key = st.text_input("Google API anahtarınızı ekleyin (boş bırakılırsa varsayılan anahtara istek atılacaktır, kendi anahtarınızı almanız önerilir. Anahtar alım videosu: [https://www.youtube.com/watch?v=brCkpzAD0gc]):", type="password")
    
    # Allow multiple file uploads
    files = st.file_uploader("Dosyalarınızı yükleyin", accept_multiple_files=True)
    
    if files:
        st.write("Yüklenen dosya sayısı:", len(files))
    
    # Convert file-like objects to UploadFile objects
    files = [UploadFile(filename=file.name, content=file.getvalue()) for file in files]
    
    # Display the names and sizes of the uploaded files
    for file in files:
        file_details = {"FileName": file.name, "FileSize": len(file.getvalue())}
        st.write(file_details)
    
    with st.spinner('Yükleniyor...'):
        user = User(username=username)  # Assuming username is defined elsewhere
        response, status_code = await upload_documents(user, files)
        if status_code == 200:
            st.success("Cevap: " + response)
        else:
            st.error("Hata:", response)
        
    question = st.text_area("Dokümanınıza sormak istediğiniz soruyu girin (sorunuz ne kadar detaylı olursa o kadar doğru bir cevap alırsınız): ")
    
    if st.button("Sor"):
        if not question:
            st.warning("Lütfen bir soru girin.")
        elif not username:
            st.warning("Lütfen kullanıcı ismi girin.")
        else:
            with st.spinner('Soru cevaplanıyor...'):
                user = User(username=username)
                response, status_code = ask_question(user, question, api_key)
                if status_code == 200:
                    st.success("Cevap: " + response)
                else:
                    st.error("Hata:", response)
            

if __name__ == "__main__":
    main()