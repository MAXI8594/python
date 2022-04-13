from PyPDF2 import PdfFileWriter, PdfFileReader

def seguridad_pdf(archivo,password):
    parser = PdfFileWriter()
    pdf = PdfFileReader(archivo)
    for page in range (pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f"encrypt_{archivo}","wb") as f:
        parser.write(f)
        f.close
    print(f"encrypted_{archivo} Created...")



if __name__ == "__main__" :
    archivo = "nuevo.pdf"
    password = "maxyy"
    seguridad_pdf(archivo,password)