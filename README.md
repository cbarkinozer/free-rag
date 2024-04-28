# free-rag
With the emergence of Large Language Models, RAG (Retrieval Augmented Generation) has become a popular usage area.  
I think that this method, which directly demonstrates the benefits of Productive Artificial Intelligence, should be a method that has already been resolved in our country and is   known to everyone.  
Therefore, I will write open source how to make a basic RAG structure from scratch.  
I plan to make this project as a free program that will run in your locale, so that the created embeddings will be stored on your computer and you can use them for your personal use.  

# To Run on Your Device
After downloading Python and pip, you need to download all dependencies by doing "pip install -r requirements.txt".  
Then, when you say "streamlit run ui.py", the application will open in your default internet browser.  

(Preferably) If you create an .env file and add your api key into it, this will be used by default if you do not provide any value: "GOOGLE_API_KEY=****"  
You can (preferably) change the embedder value in user.py to the name of another embedding model in Huggingface.  
(Preferably) From the log.txt file, you can see which parts of the documents you sent to your requests and what kind of response was formed from these parts.  
(Preferably) You can modify the ui.py file to make changes to the frontend.  
(Preferably) You can only stand up the fastapi backend service and connect your own frontend. To do this, just run the app.py file.  
(Preferably) To add different file extensions, you need to add your own file processing code to the relevant section in service.py.  
(Preferably) To change the LLM used, the relevant part of the code must be changed.  

## Used technologies  
Frontend: Streamlit  
Backend: Fastapi  
Large Language Model (LLM): Gemini (free)  
Embedding Model (Embedding): sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 (471MB)  


## Features  
Supported formats: PDF, TXT, DOCX  
Supported languages: The Embedder model supports 50 languages, while Gemini supports 40+ languages.  
The questions asked and other values are logged to be stored locally for the purpose of detecting errors.  
The Major Language Models used are made free of charge and upon API request.  
The placement models used are free of charge and are made with Turkish-speaking placement models.  
In the first version, many documents are uploaded together, and in the new upload, the previous upload is crushed.  