"""
Main cli or app entry point
"""
from my_lib.predict import predict, read_url
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 


app=FastAPI()
class Body(BaseModel):
    text:str
    max_length:int

@app.get('/')
def root():
    return("<h1> Hello from DOUMBIA </h1>")

@app.post('/generate/')
def main(body: Body):
    text = read_url(body.text)
    max_length=body.max_length
    summarised_text = predict(text, max_length=max_length  )
    return summarised_text


if __name__ == "__main__":
    uvicorn.run(app,port=8080, host='0.0.0.0')
