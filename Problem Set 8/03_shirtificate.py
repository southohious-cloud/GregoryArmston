from fpdf import FPDF

def main():
    name = input("Name: ")
    create_shirtificate(name)

def create_shirtificate(name):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 48)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C")

    pdf.image("shirtificate.png", x=10, y=70, w=pdf.w - 20)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)

    pdf.set_xy(0, 115)
    pdf.cell(pdf.w, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
