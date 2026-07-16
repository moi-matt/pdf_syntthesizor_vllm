import requests

doc = requests.get("https://arxiv.org/pdf/2311.07071")

with open("to_summarize.pdf", 'wb') as f :
    f.write(doc.content)



#if "name"==__main__:
