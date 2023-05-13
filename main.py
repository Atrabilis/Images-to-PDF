import sys; sys.path.append('./Funciones')
import os
from Funciones.clear import clear
from Funciones.crear_pdf_a_partir_de_imagenes import crear_pdf_a_partir_de_imagenes
from Funciones.quitar_primera_pagina import quitar_primera_pagina
from Funciones.add_page_numbers import add_page_numbers
from Funciones.add_page_numbers import add_page_numbers
from Funciones.create_page_pdf import create_page_pdf
from move_last_page_to_second import move_last_page_to_second

clear() 
pdf = crear_pdf_a_partir_de_imagenes("./Imagenes", "imagenes")
quitar_primera_pagina("imagenes")
add_page_numbers("./imagenes.pdf")
move_last_page_to_second('./imagenes_numbered.pdf')
os.remove("./imagenes.pdf")


