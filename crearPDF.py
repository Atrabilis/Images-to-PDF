import os
import PyPDF2
from fpdf import FPDF
from PIL import Image
from PyPDF4.pdf import PdfFileReader, PdfFileWriter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

# Define la ruta de la carpeta que contiene las imágenes
folder_path = './Imagenes'

# Define el tamaño de las imágenes en el PDF
pdf_image_width = 190
pdf_image_height = 280

# Obtiene una lista de todas las imágenes en la carpeta
image_list = os.listdir(folder_path)

# Crea un nuevo objeto PDF
pdf = FPDF()

# Agrega una página en blanco al PDF
pdf.add_page()

# Agrega cada imagen a una página separada en el PDF
for image_name in image_list:
    # Carga la imagen y redimensiona para que se ajuste al PDF
    image_path = os.path.join(folder_path, image_name)
    image = Image.open(image_path)
    image.thumbnail((pdf_image_width, pdf_image_height))

    # Agrega una nueva página al PDF
    pdf.add_page()

    # Agrega la imagen a la página actual del PDF
    pdf.image(image_path, x=pdf.get_x(), y=pdf.get_y(), w=pdf_image_width, h=pdf_image_height)

# Guarda el PDF en un archivo
pdf.output('imagenes.pdf', 'F')


# Abre el archivo PDF
with open('imagenes.pdf', 'rb') as pdf_file:
    # Crea un objeto PyPDF2 PdfFileReader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Crea un objeto PyPDF2 PdfFileWriter
    pdf_writer = PyPDF2.PdfWriter()

    # Agrega todas las páginas del PDF original al objeto pdf_writer, excepto la primera página
    for page_num in range(1, len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # Guarda el archivo PDF sin la primera página
    with open('imagenes.pdf', 'wb') as output_file:
        pdf_writer.write(output_file)

def create_page_pdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1, num + 1):
        c.drawString((210 // 2) * mm, (4) * mm, str(i))
        c.showPage()
    c.save()


def add_page_numgers(pdf_path):
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
                page.mergePage(numberLayer)
                writer.addPage(page)

            # write result
            if writer.getNumPages():
                newpath = pdf_path[:-4] + "_numbered.pdf"
                with open(newpath, "wb") as f:
                    writer.write(f)
        os.remove(tmp)



def create_page_pdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1, num + 1):
        c.drawString((210 // 2) * mm, (4) * mm, str(i))
        c.showPage()
    c.save()


def add_page_numgers(pdf_path):
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
                page.mergeTranslatedPage(numberLayer, 270, 10, expand=False)
                writer.addPage(page)

            # write result
            if writer.getNumPages():
                newpath = pdf_path[:-4] + "_numbered.pdf"
                with open(newpath, "wb") as f:
                    writer.write(f)
        os.remove(tmp)


add_page_numgers("./imagenes.pdf")