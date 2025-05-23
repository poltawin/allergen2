# core/utils/pdf_utils.py
from io import BytesIO
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.core.files.base import ContentFile
import os
from django.conf import settings

logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'logo.png')


def generate_spec_pdf(data):
    """
    Generate a fragrance specification PDF based on the provided data dictionary.
    Returns a ContentFile or BytesIO to be used in Django responses or file storage.
    """

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setLineWidth(0.15)
    pdf.setFont('Helvetica', 10)

    # === Unpack data ===
    tscode = data["tscode"]
    productname = data["productname"]
    date = data["date"]
    color = data["color"]
    sg = data["specific_gravity"]
    ri = data["refractive_index"]
    fp = f"{data['flash_point']} °C"
    shelflife = f"Approx. {data['shelf_life']} months at 20°C"
    supersede = data["supersede"]

    # === Filename (optional use) ===
    filename = f"{tscode}_Spec.pdf"

    # === Layout ===
    # pdf.drawString(60, 795, "Revision No.: 0000")
    # pdf.drawString(60, 782, "Revision Date: 00.00.00")
    # pdf.drawString(60, 769, f"Issue Date: {date}")
    # pdf.drawString(60, 756, f"Supersede: {supersede}")

    pdf.setFont('Helvetica',10)
    pdf.drawString(60,795,"Revision No.")
    pdf.drawString(60,782,"Revision Date")
    pdf.drawString(60,769,"Issue Date")
    pdf.drawString(60,756,"Supersede")
    pdf.drawString(135,795,":")
    pdf.drawString(135,782,":")
    pdf.drawString(135,769,":")
    pdf.drawString(135,756,":")
    pdf.drawString(150,795,"0000")
    pdf.drawString(150,782,"00.00.00")
    pdf.drawString(150,769,f"{date}")
    pdf.drawString(150,756,supersede)
    

    pdf.drawString(255, 650, "Mixture of permitted fragrance substances")
    pdf.drawString(255, 590, color)
    pdf.drawString(255, 560, "Characteristics")
    pdf.drawString(255, 470, sg)
    pdf.drawString(255, 440, ri)
    pdf.drawString(255, 410, fp)
    pdf.drawString(255, 375, "In a tightly closed container, protected from heat and light.")
    pdf.drawString(255, 340, shelflife)
    pdf.drawString(255, 305, "Inside-lacquered drums (25 and 200 Kg)")
    pdf.drawString(255, 270, "33 02")

    # Lines
    pdf.line(50,710,530,710)
    pdf.line(50,670,530,670)
    pdf.line(50,630,530,630)
    pdf.line(50,395,530,395)
    pdf.line(50,360,530,360)
    pdf.line(50,325,530,325)
    pdf.line(50,290,530,290)
    pdf.line(50,255,530,255)
    pdf.line(50,82,530,82)

    # Footer
    pdf.setFont('Helvetica',10)
    pdf.drawString(50, 55, "This is a computer printout and has therefore not been signed by hand.")
    pdf.setFont('Helvetica',8)
    pdf.drawString(75,30,"De Roma Fragrance & Chemicals Co., Ltd. 88/43 Moo 12, Srinakarin Rd, Bang Kaew, Bang Plee, Samutprakarn 10540")
    pdf.drawString(75,22,"Tel: 66 2 3482223-5")

    # Title
    pdf.setFont('Helvetica-Bold', 18)
    pdf.drawString(155, 720, "FRAGRANCE SPECIFICATION")

    # Section Titles
    pdf.setFont('Helvetica-Bold', 12)
    # pdf.drawString(55, 690, f"PRODUCT: {tscode} - {productname}")
    pdf.drawString(55, 650, "PRODUCT INFORMATION")
    pdf.drawString(55, 615, "PRODUCT CHARACTERISTIC:")
    pdf.drawString(55, 375, "STORAGE CONDITIONS")
    pdf.drawString(55, 340, "SHELF-LIFE")
    pdf.drawString(55, 305, "PACKAGING")
    pdf.drawString(55, 270, "Customs Tariff (HS code)")
    pdf.drawString(55, 235, "ADDITIONAL INFORMATION")
    pdf.drawString(55,690,"PRODUCT:")
    pdf.drawString(145,690,tscode)
    pdf.drawString(255,690,productname)

    # Appearance and physical section
    # pdf.setFont('Helvetica-Bold', 10)
    # pdf.drawString(55, 590, "Appearance")
    # pdf.drawString(55, 560, "Odour")
    # pdf.drawString(55, 500, "PHYSICAL PROPERTIES")
    # pdf.drawString(55, 470, "Specific Gravity @ 20°C")
    # pdf.drawString(55, 440, "Refractive Index @ 20°C")
    # pdf.drawString(55, 410, "Flash Point (Closed Cup)")

    pdf.setFont('Helvetica-Bold',10)
    pdf.drawString(55,590,"Appearance")
    pdf.drawString(55,560,"Odour")
    pdf.drawString(55,500,"PHYSICAL PROPERTIES")
    pdf.drawString(55,470,"Specific Gravity @ 20°C")
    pdf.drawString(55,440,"Refractive Index @ 20°C")
    pdf.drawString(55,410,"Flash Point (Closed Cup)")
    pdf.drawString(225,590,":")
    pdf.drawString(225,560,":")
    pdf.drawString(225,500,":")
    pdf.drawString(225,470,":")
    pdf.drawString(225,440,":")
    pdf.drawString(225,410,":")
    pdf.drawString(225,375,":")
    pdf.drawString(225,340,":")
    pdf.drawString(225,305,":")
    pdf.drawString(225,270,":")
    pdf.drawString(225,235,":")
    pdf.drawString(225,650,":")
    pdf.drawString(255,500,"(Provisional data only)")
    pdf.drawString(50,72,"Date:")
    pdf.drawString(85,72,f"{date}")


    pdf.setFont('Helvetica', 10)
    pdf.drawString(55, 530, "(Standard for comparison: Sample from previously accepted batch)")

    # Note
    pdf.setFont('Helvetica-Bold', 6)
    pdf.drawString(50, 120, "Note:")
    pdf.setFont('Helvetica',6)
    pdf.drawString(50,110,"The information and recommendations made herein are based on our own information and research; and whilst they are believed to be accurate, they should be taken as a guide")
    pdf.drawString(50,104,"only. However, nothing stated herein is to be taken as a warranty expressed or implied regarding the non infringement of any relevant patents, the accuracy of the information")
    pdf.drawString(50,98,"supplied or the use of our product or products. Purchasers should make their own tests and/or patents searches to determine the suitability, stability, shelf-life and/or compatibility")
    pdf.drawString(50,92,"and/or recommendations for their purposes.")
    pdf.drawString(50,86,"No responsibility is accepted for any product once it is incorporated and/or mixed and/or diluted with other ingredients.")



    # Optional logo (assuming static path or URL later configurable)
    pdf.drawInlineImage(logo_path, 440, 711, width=138, height=138)
    # pdf.drawInlineImage(logo_path, x=400, y=750, width=120, height=50)


    # Finalize
    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return ContentFile(buffer.read(), name=filename)


def generate_coa_pdf(data):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setLineWidth(0.15)
    pdf.setFont('Helvetica', 10)

    # Extract data
    tscode = data["tscode"]
    productname = data["productname"]
    batch = data["batch"]
    date = data["date"]
    odor = data["odor"]
    appearance = data["appearance"]
    sg = data["specific_gravity"]
    ri = data["refractive_index"]


    # Layout
    pdf.drawString(60, 795, f"Batch No.: {batch}")
    pdf.drawString(60, 780, f"Date: {date}")
    pdf.setFont('Helvetica-Bold', 14)
    pdf.drawString(180, 750, "CERTIFICATE OF ANALYSIS")

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(60, 710, f"Product: {tscode} - {productname}")

    pdf.setFont('Helvetica-Bold', 10)
    pdf.drawString(60, 670, "Appearance:")
    pdf.drawString(60, 640, "Odor:")
    pdf.drawString(60, 610, "Specific Gravity @ 20°C:")
    pdf.drawString(60, 580, "Refractive Index @ 20°C:")

    pdf.setFont('Helvetica', 10)
    pdf.drawString(200, 670, appearance)
    pdf.drawString(200, 640, odor)
    pdf.drawString(200, 610, sg)
    pdf.drawString(200, 580, ri)

    pdf.setFont('Helvetica', 6)
    pdf.drawString(50, 50, "This is a computer printout and has not been signed by hand.")
    pdf.drawString(50, 38, "De Roma Fragrance & Chemicals Co., Ltd. | Srinakarin Rd, Bang Plee, Samutprakarn")

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    filename = f"{tscode}_COA.pdf"
    return ContentFile(buffer.read(), name=filename)

     
def generate_msds_pdf(data):
    from reportlab.lib.pagesizes import A4

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setLineWidth(0.15)
    pdf.setFont('Helvetica', 10)

    tscode = data["tscode"]
    productname = data["productname"]
    date = data["date"]
    hazard = data["hazard"]
    precaution = data["precaution"]

    pdf.setFont('Helvetica-Bold', 16)
    pdf.drawString(170, 790, "MATERIAL SAFETY DATA SHEET")

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(60, 750, f"Product: {tscode} - {productname}")
    pdf.setFont('Helvetica', 10)
    pdf.drawString(60, 735, f"Date: {date}")

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(60, 690, "1. Hazards Identification")
    pdf.setFont('Helvetica', 10)
    pdf.drawString(80, 670, hazard)

    pdf.setFont('Helvetica-Bold', 12)
    pdf.drawString(60, 630, "2. Precautionary Measures")
    pdf.setFont('Helvetica', 10)
    pdf.drawString(80, 610, precaution)

    # Footer
    pdf.setFont('Helvetica', 6)
    pdf.drawString(50, 50, "This is a computer printout and has not been signed by hand.")
    pdf.drawString(50, 38, "De Roma Fragrance & Chemicals Co., Ltd. | Srinakarin Rd, Bang Plee, Samutprakarn")

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    filename = f"{tscode}_MSDS.pdf"
    return ContentFile(buffer.read(), name=filename)
