from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from service import upload_documents, ask_question
from user import User

app = FastAPI()


@app.post("/document-uploader")
async def document_uploader(username: str = Form(...), files: list[UploadFile] = File(...)):
    user = User(username=username)
    response, status_code = await upload_documents(user, files)
    if status_code == 200:
        return {response}
    else:
        raise HTTPException(status_code=status_code, detail=response)

@app.post("/question-answerer")
async def question_answerer(username: str = Form(...), question: str = Form(...), api_key = File(None)):
    user = User(username=username)
    response, status_code = await ask_question(user, question, api_key)
    if status_code == 200:
        return {response}
    else:
        raise HTTPException(status_code=status_code, detail=response)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)