#pip install pdfplumber
import pdfplumber
pdf = pdfplumber.open('./Relação.pdf')
page = pdf.pages[0]
text = page.extract_text()
print(text)
