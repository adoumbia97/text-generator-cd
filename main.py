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
    length: int

@app.get('/')
def root():
    return("<h1> Hello from DOUMBIA </h1>")

@app.post('/generate/')
def main(body: Body):
    text = read_url(body.text)
    summarised_text = predict(text)
    return summarised_text


if __name__ == "__main__":
    uvicorn.run(app,port=8080, host='0.0.0.0')
