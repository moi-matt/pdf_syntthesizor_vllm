import requests
from pypdf import PdfReader
import tiktoken 
# Download the wanted document 
doc = requests.get("https://arxiv.org/pdf/2311.07071")
with open("to_summarize.pdf", 'wb') as f :
    f.write(doc.content)

# Read the pdf and extract text
reader = PdfReader("to_summarize.pdf")
print(f"Number of pages {len(reader.pages)}")

parts = []

def visitor_body(text, cm, tm, font_dict, font_size):
    y = tm[5]
    if 50 < y < 720 or y == 0:
        parts.append(text)

for page in reader.pages:
    page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

# Count the number of tokens the text is containing :

def count_number_of_token(text)->int:
    #get the encoding
    encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')
    text_encode = encoding.encode(text)
    print(text_encode[:10])
    number_of_token = len(text_encode)
    return number_of_token

n_token = count_number_of_token(text_body)
print(f'Number of token {n_token}')

#if "name"==__main__:
