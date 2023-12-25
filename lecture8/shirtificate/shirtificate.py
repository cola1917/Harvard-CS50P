from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("./shirtificate.png", 5, 40, 200)
        self.set_font("helvetica", "B", 50)
        self.ln(20)

def main():
    name = input("Name: ")
    shirt(name)

def shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=28, style='IU')
    pdf.set_text_color(212,242,231)
    pdf.cell(0, 200, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
