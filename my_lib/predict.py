
import urllib.request
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, T5ForConditionalGeneration



def predict(text, max_length=150):
    tokenizer=AutoTokenizer.from_pretrained("t5-small")
    summarizer = T5ForConditionalGeneration.from_pretrained("t5-small")
    input_token = tokenizer.encode(text, return_tensors="pt", max_length=700, truncation=True)
    summary_ids = summarizer.generate(input_token, max_length=max_length, num_beams=4, length_penalty=2.0, early_stopping=True)
    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return output


def read_file(path):
    with open(path, 'r', encoding="utf-8") as f:
        return f.read()



def read_url(url):
    text=''
    req=urllib.request.Request(
        url,data=None,
        headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecji) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    html=urllib.request.urlopen(req)
    parser=BeautifulSoup(html, 'html.parser')
    for paragraph in parser.find_all("p"):
        #print(paragraph.text)
        text+= paragraph.text
    return text

