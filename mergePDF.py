# from glob import glob
# from pikepdf import Pdf

# new_pdf = Pdf.new() #create new pdf

# for file in glob("*.pdf"): #access each file and open it and add each page to new file 
#     old_pdf = Pdf.open(file)
#     new_pdf.pages.extend(old_pdf.pages)

# new_pdf.save("demo.pdf")

      #OR

import PyPDF2

path1 = "c:/Users/hp/Desktop/More/PYTHON/Resources/pdf1.pdf"
path2 = "c:/Users/hp/Desktop/More/PYTHON/Resources/pdf2.pdf"
pdffiles = [path1,path2]

merger = PyPDF2.PdfMerger()

for filename in pdffiles:
    pdfFile = open(filename, "rb")
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write('mergedpdf.pdf')    
