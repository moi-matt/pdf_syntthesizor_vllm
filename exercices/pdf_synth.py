import requests
from pypdf import PdfReader

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





#if "name"==__main__:
