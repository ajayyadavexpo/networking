import PyPDF2
pdfFileObject = open('sample.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages
print("No of pages : ",count)

for i in range(count):
    page = pdfReader.getPage(i)
    print(page.extractText())