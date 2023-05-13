import os
import PyPDF4
from reportlab.pdfgen.canvas import Canvas

def crear_indice(nombre):
    # Obtener la ruta absoluta del archivo de origen
    file_path = os.path.abspath(nombre)

    # Abrir el PDF original y crear un objeto PdfFileReader
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF4.PdfFileReader(pdf_file)

    # Crear un objeto PdfFileWriter para el PDF final
    pdf_writer = PyPDF4.PdfFileWriter()

    # Iterar sobre cada página del PDF original
    for i in range(pdf_reader.numPages):
        # Agregar la página actual al objeto PdfFileWriter para el PDF final
        page = pdf_reader.getPage(i)
        pdf_writer.addPage(page)

    # Crear un objeto PdfFileWriter para el PDF del índice
    index_writer = PyPDF4.PdfFileWriter()

    # Crear un objeto Canvas para dibujar el índice
    canvas = Canvas("indice.pdf")

    # Agregar el título del índice
    canvas.drawString(50, 750, "Índice")

    # Iterar sobre cada página del PDF original
    for i in range(pdf_reader.numPages):
        # Agregar una entrada para esa página en el índice
        entrada = "{} - Página {}: {}".format(nombre, i+1, "Título de la página")
        x = 50
        y = 700 - i*20
        leading = 14  # Espacio entre líneas
        words = entrada.split()
        lines = []
        line = ''
        for word in words:
            if len(line + ' ' + word) <= 50:
                line = line + ' ' + word
            else:
                lines.append(line)
                line = word
        if line:
            lines.append(line)
        for line in lines:
            canvas.drawString(x, y, line)
            y -= leading

    # Guardar el PDF del índice
    canvas.save()
    index_file = open("indice.pdf", "rb")
    index_pdf = PyPDF4.PdfFileReader(index_file)

    # Agregar el PDF del índice al objeto PdfFileWriter para el PDF final
    for i in range(index_pdf.numPages):
        # Insertar el índice en la segunda página del archivo final
        if i == 1:
            pdf_writer.insertPage(1, index_pdf.getPage(i))
        else:
            pdf_writer.addPage(index_pdf.getPage(i))

    # Guardar el PDF final
    output_file = open('final.pdf', 'wb')
    pdf_writer.write(output_file)
    output_file.close()

    # Cerrar los archivos abiertos
    pdf_file.close()
    index_file.close()


