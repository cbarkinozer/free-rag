# free-rag
With the introduction of Large Language Models, RAG (Retrieval Augmented Generation) has become a prominent application field.   
I believe that this strategy, which explicitly displays the benefits of Productive Artificial Intelligence, should have already been addressed globally and be well recognized.   
As a result, I'll provide an open source example on how to build a basic RAG structure from start.   
I intend to make this project a free program, so it can be used for personal purposes.  
 

# To Run on Your Device
After downloading Python and pip, you need to download all dependencies by doing "pip install -r requirements.txt".  
Then, when you enter the command "streamlit run ui.py", the application will open in your default internet browser.  

(Optional) If you create an.env file and include your API key in it, it will be used by default if no value is specified: "GOOGLE_API_KEY=****"    
(Optional) In user.py, update the embedding value to the name of another embedding model in Huggingface.    
(Optional) The log.txt file shows which parts of the documents you supplied in answer to your requests, as well as what type of response was generated from them.    
(Optional) To alter the frontend, modify the ui.py file.    
(Optional) You can only start the fastapi backend service and connect to your own frontend. To run only backend, simply run the app.py file.   
(Optional) To add other file extensions, you must provide your own file processing code for that extension (_extract_text_from_document() method in service.py).  
(Optional) To change the LLM used, the relevant part of the code must be changed (ask_question() method in service.py).    

## Technologies  
Frontend: Streamlit   
Backend: Fastapi   
Large Language Model (LLM): Gemini (free)   
Embedding Model (Embedding): sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 (471MB)   


## Features  
Supported formats: PDF, TXT, DOCX   
Supported languages: The Embedding model supports 50 languages, while Gemini supports 40+ languages.   
The questions asked and other related variables are logged locally for the purpose of detecting errors.   
The Major Language Models used are made free of charge and upon API request.   
The embedding model that is used is a  multilanguage (including Turkish) and is free of charge.   
Multiple documents are uploaded together, and in a new upload, the previous upload is overriden.   