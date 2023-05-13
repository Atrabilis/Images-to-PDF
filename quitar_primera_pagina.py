import PyPDF2
def quitar_primera_pagina(nombre):
    # Abre el archivo PDF
    with open(nombre+'.pdf', 'rb') as pdf_file:
        # Crea un objeto PyPDF2 PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Crea un objeto PyPDF2 PdfFileWriter
        pdf_writer = PyPDF2.PdfWriter()

        # Agrega todas las páginas del PDF original al objeto pdf_writer, excepto la primera página
        for page_num in range(1, len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # Guarda el archivo PDF sin la primera página
        with open(nombre+'.pdf', 'wb') as output_file:
            pdf_writer.write(output_file)

    def create_page_pdf(num, tmp):
        c = canvas.Canvas(tmp)
        for i in range(1, num + 1):
            c.drawString((210 // 2) * mm, (4) * mm, str(i))
            c.showPage()
        c.save()
