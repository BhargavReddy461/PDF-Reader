import pyttsx3
import PyPDF2
book = open('BhargavReddy_Dwarampudi_Resume_2021.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(book)
s = pyttsx3.init()
page = pdf.getPage(0)
text = page.extractText()
s.say(text)
s.runAndWait()
