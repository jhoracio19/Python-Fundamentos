
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=16)
pdf.cell(200, 10, text="Hola mundo con fpdf2", ln=True, align="C")
pdf.output("test.pdf")
