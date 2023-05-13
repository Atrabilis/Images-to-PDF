import os
from fpdf import FPDF
from PIL import Image
from PyPDF4.pdf import PdfFileReader, PdfFileWriter
def crear_pdf_a_partir_de_imagenes(path, nombre):
    # Define la ruta de la carpeta que contiene las imágenes
    folder_path = path

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
    pdf.output(nombre +'.pdf', 'F')