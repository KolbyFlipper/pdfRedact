from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import tkinter, tkinter.filedialog
import os

def redact(original_file_location, blocker_file_location):
    output   = PdfFileWriter()
    original = PdfFileReader(open(original_file_location, "rb"))
    blocker  = PdfFileReader(open(blocker_file_location, "rb"))

    if original.getNumPages() != blocker.getNumPages():
        print ("PDF Inputs have different number of pages. Exiting.")
        return

    output_page = original.getPage(0)  
    output_page.mergePage((blocker.getPage(0)))
    output.addPage(output_page)
    
    return output

def redact_files_in_directory(input_directory, output_directory, redacting_file):
    files = os.listdir(input_directory)
    length = len(files)

    for i in range(length):
        file = files[i]
        if (os.path.isfile(file)):
            print (file, "is not a file. Exiting.")
            continue
        elif (file.endswith('.pdf') == False):
            print (file, 'must be a .pdf. Exiting.')
            continue

        output = redact(os.path.join(input_directory, file), redacting_file) #output = PdfFileWriter
        output_file = os.path.join(output_directory, file).replace("\\","/") #fix path issue
        flat_output_file = output_file.replace(".pdf","_flat.pdf")
        
        #temp_output_ps = output_file.replace(".pdf","_temp.ps")

        with open(flat_output_file, 'wb') as f:
           output.write(f)
            
        print ("(" + str(i) + "/" + str(length - 1) + "): ", file)
        
def get_new_directory_path():
    print("Select input directory path first, output directory second")
    return tkinter.filedialog.askdirectory()

def get_new_file_path():
    print("Select redacting pdf")
    return tkinter.filedialog.askopenfilename()

if __name__ == '__main__':
    input_directory = get_new_directory_path()

    output_directory = get_new_directory_path()

    redacting_file = get_new_file_path()

    if redacting_file.endswith('.pdf') == False:
        print ("redacting file must be a pdf file with extension '.pdf'")
    else:
        redact_files_in_directory(input_directory, output_directory, redacting_file)