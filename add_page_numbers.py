from PyPDF4.pdf import PdfFileReader, PdfFileWriter
from create_page_pdf import create_page_pdf
import os
def add_page_numbers(pdf_path):
    """
    Add page numbers to a pdf, save the result as a new pdf
    @param pdf_path: path to pdf
    """
    tmp = "__tmp.pdf"

    writer = PdfFileWriter()
    with open(pdf_path, "rb") as f:
        reader = PdfFileReader(f, strict=False)
        n = reader.getNumPages()

        # create new PDF with page numbers
        create_page_pdf(n, tmp)

        with open(tmp, "rb") as ftmp:
            number_pdf = PdfFileReader(ftmp)
            # iterarte pages
            for p in range(n):
                page = reader.getPage(p)
                numberLayer = number_pdf.getPage(p)
                # merge number page with actual page
                page.mergeTranslatedPage(numberLayer, 250, 10, expand=False)
                writer.addPage(page)

            # write result
            if writer.getNumPages():
                newpath = pdf_path[:-4] + "_numbered.pdf"
                with open(newpath, "wb") as f:
                    writer.write(f)
        os.remove(tmp)