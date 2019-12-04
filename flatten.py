import os
import img2pdf
import tkinter, tkinter.filedialog
from pdf2image import convert_from_path

directory = tkinter.filedialog.askdirectory() #select the output folder from redact.py
#directory = r"C:\Users\" #if you prefer to hardcode the file path. 

for file in os.scandir(directory):
    images= convert_from_path(file)
    #if this breaks, you forgot to add poppler's bin folder to your path environment variable 
    #you can also use this (below) but replace poppler_path with your poppler path 
    #images= convert_from_path(file,poppler_path='C:\\poppler-0.68.0\\bin')
    
    for image in images: #this is the dumbest loop I've ever written even though it works
        filename = file.name.replace(".pdf",".jpg") #create .jpg filename
        image.save(filename,"JPEG") #create jpg
        with open((file.name.replace("_flat","")),"wb") as f: #open new pdf
            f.write(img2pdf.convert(filename)) #convert jpg to pdf
        os.remove(filename) #remove jpg
