# PDFtoAudio
Just a really sloppy and quick way to convert PDFs into an audio file. There is a lot of refactoring and refinement to be made, this was literally something I threw together in 45 minutes and won't need ever again. Maybe I'll clean it later, not really sure if anyone will ever see or use this again though.

It will work with PDFs that have editable text, documents that have been converted into PDFs, and scanned images/PDFs that have issues with programatically reading text directly from the PDF. This work around for reading PDFs that have issues being read is done by converting the PDF into an image which is then run through a text recognition engine which then extracts the text, which then is converted to audio.

############
REQUIREMENTS
############


#PYTHON AND PACKAGES


    Python 3.10.0

    pdf2image   1.16.0

    Pillow      9.3.0

    PyPDF2      2.12.1

    pytesseract 0.3.10

    pyttsx3     2.90


#SOFTWARE 


    poppler-22.12.0

    tesseract-ocr-v5.3.0.20221214
