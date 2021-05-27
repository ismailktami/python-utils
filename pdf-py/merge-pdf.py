from PyPDF2 import PdfFileMerger, PdfFileReader


def merge_pdfs():
    # Call the PdfFileMerger
    mergedObject = PdfFileMerger()

    # I had 116 files in the folder that had to be merged into a single document
    # Loop through all of them and append their pages
    for fileNumber in range(1, 6):
        mergedObject.append(PdfFileReader(
            'pdf' + str(fileNumber) + '.pdf', 'rb'))

    # Write all the files into a file which is named as shown below
    mergedObject.write("files-merged.pdf")


def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    print(info)
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title


if __name__ == '__main__':
    merge_pdfs()
