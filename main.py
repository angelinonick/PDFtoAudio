import pyttsx3, PyPDF2
from PIL import Image
from pytesseract import pytesseract
from pdf2image import convert_from_path

#sample1 will work without requiring conversion to image
pdf = 'sample1.pdf'

#sample2 will fail to fetch text from pdf and require conversion to image and text extraction
# pdf = 'sample2.pdf'

def pdftotext(pdf):
    pdfreader = PyPDF2.PdfFileReader(open(pdf, 'rb'))

    for page_num in range(pdfreader.numPages):
        text = pdfreader.getPage(page_num).extract_text()
        clean_text = text.strip().replace('\n', ' ')
        print(clean_text)

    return clean_text
    

def texttoaudio(text, pdf):
    speaker = pyttsx3.init()
    speaker.save_to_file(text, pdf+".mp3")
    speaker.runAndWait()

    speaker.stop()

def pdftoimagetotext(pdf):
    images = convert_from_path(pdf)
    imageNameList = []
    textList = []
    for i in range(len(images)):
    
        # Save pages as images in the pdf
        images[i].save('./tmp/page'+ str(i) +'.jpg', 'JPEG')
        imageNameList.append('./tmp/page'+ str(i) +'.jpg')


    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    pytesseract.tesseract_cmd = path_to_tesseract

    for individualImage in imageNameList:

        img = Image.open(individualImage)

        text = pytesseract.image_to_string(img)
        
        clean_text = text.rstrip().replace('\n', ' ')
        textList.append(clean_text)
        print(text)
    
    return textList

clean_text = pdftotext(pdf)

if len(clean_text) == 0:
    print("Couldn't fetch text. Attempting alternative method.")
    clean_text = pdftoimagetotext(pdf)
    if len(clean_text) == 0:
        print("Still can't fetch text.")
    if len(clean_text) != 0:
        texttoaudio(clean_text, pdf)

    
if len(clean_text) != 0:
    texttoaudio(clean_text, pdf)