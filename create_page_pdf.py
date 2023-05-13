from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def create_page_pdf(num, tmp):
    c = canvas.Canvas(tmp)
    for i in range(1, num + 1):
        c.drawString((210 // 2) * mm, (4) * mm, str(i))
        c.showPage()
    c.save()