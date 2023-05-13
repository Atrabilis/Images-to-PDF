import PyPDF4

def move_last_page_to_second(pdf_file_path):
    # Abrir el archivo PDF en modo de lectura y escritura
    with open(pdf_file_path, 'rb+') as pdf_file:
        # Crear un objeto de lectura de PDF
        pdf_reader = PyPDF4.PdfFileReader(pdf_file)
        
        # Obtener el número total de páginas del PDF
        num_pages = pdf_reader.getNumPages()
        
        # Obtener la página final del PDF
        last_page = pdf_reader.getPage(num_pages - 1)
        
        # Eliminar la última página del PDF
        pdf_writer = PyPDF4.PdfFileWriter()
        for i in range(num_pages - 1):
            pdf_writer.addPage(pdf_reader.getPage(i))
        
        # Insertar la página final en la segunda posición del PDF
        pdf_writer.insertPage(last_page, 1)
        
        # Guardar los cambios en el archivo PDF
        pdf_writer.write(pdf_file)