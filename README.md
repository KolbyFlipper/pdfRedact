# pdfRedact
Takes in an input directory and a redaction PDF, outputs all redacted PDFs to selected output directory. Python 3.8.0

Requirements: 
PyPDF2  (pip install PyPDF2) 

tkinter (pip install tkinter)

os (should come with your python installation)

pdf2img (pip install pdf2img)

img2pdf (pip install img2pdf)

poppler for windows (https://blog.alivate.com.au/poppler-windows/)


There are quite possibly more requirements that you'll need, honestly I installed so many things over the course of writing this that I couldn't keep track. If you notice something, make an Issue and I'll update this.

You'll need to add PyPDF2 to your %PATH%, as well as poppler's bin folder.

Program flow: 
Create a redaction PDF. This PDF must have your redactions (I use black rectangles) and nothing else, with a transparent background. 
Instructions on how to do it on Linux: https://ask.libreoffice.org/en/question/182659/libreoffice-writer-page-transparency/ 
Instructions on how to do it on Windows (untested): https://helpx.adobe.com/acrobat/using/transparency-flattening-acrobat-pro.html
https://graphicdesign.stackexchange.com/questions/57316/make-pdf-background-transparent-in-adobe-acrobat-pro-xi *

Run the code (py redact.py); It will open a file dialogue. First select the input folder with unredacted PDFs. Next select your EMPTY output folder. 

Lastly, select your redaction PDF. This will fill the output folder with your input files visually merged with the redaction PDF. However, to properly redact the information there is one more step.

Run flatten.py. It will ask you to select a folder- select wherever you put the output from redact.py. It will then output all of the final PDFs after converting them to JPG and back. You will likely lose a small amount of resolution in the process. This removes the underlying information so that your redacted information can't be highlighted/copied. If flatten.py fails with a poppler error, follow the steps commented in the file.

*i have no idea how to create a transparent PDF in windows and have been thus unable to do it for free
