import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def encrypt(input_pdf, output_pdf, password):
    os.remove(output_pdf)
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
                       use_128bit=True)
    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    encrypt(input_pdf='./pdf-py/sample.pdf',
            output_pdf='./pdf-py/encrypted.pdf',
            password='ismail')
