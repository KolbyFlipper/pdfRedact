from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import tkinter, tkinter.filedialog
import os

def redact(orig_file, redacting_file):
    output   = PdfFileWriter()
    original = PdfFileReader(open(orig_file, "rb"))
    redactor  = PdfFileReader(open(redacting_file, "rb"))

    if original.getNumPages() != redactor.getNumPages():
        print ("PDF Inputs have different number of pages. Exiting.")
        return

    output_page = original.getPage(0)  #if you need multi-page redaction, this can be easily made into a for loop
    output_page.mergePage((redactor.getPage(0))) #merges the pages
    output.addPage(output_page)  #adds the merged page to output
    
    return output

def redact_files_in_directory(input_directory, output_directory, redacting_file):
    files = os.listdir(input_directory)
    length = len(files) #tracker for later visual output

    for i in range(length): 
        file = files[i]
        if (os.path.isfile(file)):
            print (file, "is not a file. Skipping.")
            continue
        elif (file.endswith('.pdf') == False):
            print (file, 'must be a .pdf. Skipping.')
            continue

        output = redact(os.path.join(input_directory, file), redacting_file) #output = PdfFileWriter
        output_file = os.path.join(output_directory, file).replace("\\","/") #fix path issue
        flat_output_file = output_file.replace(".pdf","_flat.pdf")

        with open(flat_output_file, 'wb') as f:
           output.write(f)
            
        #displays progress as filenum/total files in dir
        print ("(" + str(i) + " of " + str(length - 1) + "): ", file) 
        
def get_new_directory_path():
    print("Select input directory path first, output directory second")
    return tkinter.filedialog.askdirectory()

def get_new_file_path():
    print("Select redacting pdf")
    return tkinter.filedialog.askopenfilename()

if __name__ == '__main__':
    input_directory = get_new_directory_path() #first popup dialog   (folder)
    output_directory = get_new_directory_path() #second popup dialog (folder)
    redacting_file = get_new_file_path()        #third popup dialog  (file)

    if redacting_file.endswith('.pdf') == False:
        print ("redacting file must be a pdf file with extension '.pdf'")
    else:
        redact_files_in_directory(input_directory, output_directory, redacting_file)
