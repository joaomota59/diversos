#pip install pdfplumber
import pdfplumber
pdf = pdfplumber.open('./Relação')
paginas = len(pdf.pages) #quantidade de paginas
text = ""
for i in range(paginas):
    page = pdf.pages[i]
    text += page.extract_text()
print(text)
