from clear import clear
from crear_pdf_a_partir_de_imagenes import crear_pdf_a_partir_de_imagenes
from quitar_primera_pagina import quitar_primera_pagina
from add_page_numbers import add_page_numbers
from add_page_numbers import add_page_numbers
from create_page_pdf import create_page_pdf

clear()
crear_pdf_a_partir_de_imagenes("./Imagenes", "imagenes")
quitar_primera_pagina("imagenes")
add_page_numbers("./imagenes.pdf")
add_page_numbers("./imagenes.pdf")

