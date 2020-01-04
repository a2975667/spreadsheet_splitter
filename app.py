import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import argparse
import shutil




def get_filename_list(filename):
    f = open(filename, 'r')
    name_list = [n.rstrip() for n in f.readlines()]
    return name_list

def main(args, filename, folder):

    #create folder
    folder = str(folder.split('.')[0])
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)


    pdf = PdfFileReader(args.pdf, "rb")
    pdf_writer = PdfFileWriter()

    counter = 0
    page_count = 1
    filename_counter = 0
    for counter in range(pdf.getNumPages()+args.page_per_file):
        try:
            pdf_writer.addPage(pdf.getPage(counter))
        except:
            path = os.path.join(folder, filename[filename_counter] + '.pdf')
            filename_counter += 1
            f_out = open(path,"wb")
            pdf_writer.write(f_out)
            print("saving the a file.")
            return
            
        if page_count % (args.page_per_file) == 0:
            path = os.path.join(folder, filename[filename_counter] + '.pdf')
            filename_counter += 1
            f_out = open(path,"wb")
            pdf_writer.write(f_out)
            print("saving the a file.")
            pdf_writer = PdfFileWriter()
        page_count+=1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", help="pdf argument to split")
    parser.add_argument("csv", help="csv argument for lsit of filename")
    parser.add_argument("page_per_file", help="number of pages to split", type=int)
    
    args = parser.parse_args()
    filename = get_filename_list(args.csv)
    main(args, filename, args.csv)
    print(complete)
