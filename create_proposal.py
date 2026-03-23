from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.platypus import PageBreak
from datetime import datetime, timedelta

# Colors
PURPLE = colors.HexColor("#7C3AED")
DARK_BG = colors.HexColor("#1a1a2e")
LIGHT_PURPLE = colors.HexColor("#A78BFA")
GOLD = colors.HexColor("#D4AF37")
DARK_TEXT = colors.HexColor("#1F2937")
GRAY_TEXT = colors.HexColor("#6B7280")
LIGHT_BG = colors.HexColor("#F9FAFB")

output_path = "C:/Users/queen/Claude/Scent4Less/Scent4Less_Pricing_Proposal.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    rightMargin=50,
    leftMargin=50,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Title'],
    fontSize=28,
    textColor=PURPLE,
    spaceAfter=6,
    fontName='Helvetica-Bold',
    alignment=TA_LEFT,
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=12,
    textColor=GRAY_TEXT,
    spaceAfter=20,
    fontName='Helvetica',
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=PURPLE,
    spaceBefore=20,
    spaceAfter=10,
    fontName='Helvetica-Bold',
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=11,
    textColor=DARK_TEXT,
    spaceAfter=8,
    fontName='Helvetica',
    leading=16,
)

bold_body = ParagraphStyle(
    'BoldBody',
    parent=body_style,
    fontName='Helvetica-Bold',
)

small_style = ParagraphStyle(
    'SmallText',
    parent=styles['Normal'],
    fontSize=9,
    textColor=GRAY_TEXT,
    fontName='Helvetica',
    leading=13,
)

center_style = ParagraphStyle(
    'CenterText',
    parent=body_style,
    alignment=TA_CENTER,
)

right_style = ParagraphStyle(
    'RightText',
    parent=body_style,
    alignment=TA_RIGHT,
)

price_style = ParagraphStyle(
    'PriceText',
    parent=styles['Title'],
    fontSize=32,
    textColor=PURPLE,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold',
    spaceAfter=4,
)

story = []

# === HEADER ===
today = datetime.now()
valid_until = today + timedelta(days=30)

story.append(Paragraph("PRICING PROPOSAL", title_style))
story.append(Paragraph("Web Development Services", subtitle_style))

# Divider
story.append(HRFlowable(width="100%", thickness=2, color=PURPLE, spaceAfter=15))

# From / To section
header_data = [
    [
        Paragraph("<b>FROM</b>", ParagraphStyle('', parent=small_style, textColor=PURPLE, fontSize=9)),
        Paragraph("<b>TO</b>", ParagraphStyle('', parent=small_style, textColor=PURPLE, fontSize=9)),
        Paragraph("<b>DETAILS</b>", ParagraphStyle('', parent=small_style, textColor=PURPLE, fontSize=9)),
    ],
    [
        Paragraph("Chimudi Nwosu<br/>Web Developer<br/>Lagos, Nigeria<br/>chimunwosu@github", body_style),
        Paragraph("[Client Name]<br/>[Client Company]<br/>[Client Address]<br/>[Client Email]", body_style),
        Paragraph(f"Date: {today.strftime('%B %d, %Y')}<br/>Valid Until: {valid_until.strftime('%B %d, %Y')}<br/>Proposal #: SCT-001", body_style),
    ]
]

header_table = Table(header_data, colWidths=[170, 170, 170])
header_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ('LINEBELOW', (0, 0), (-1, 0), 0.5, LIGHT_PURPLE),
]))
story.append(header_table)
story.append(Spacer(1, 20))

# === PROJECT OVERVIEW ===
story.append(Paragraph("Project Overview", heading_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E5E7EB"), spaceAfter=10))

story.append(Paragraph(
    "Design and development of a premium, modern single-page website for <b>Scent4Less</b> "
    "-- a fragrance brand offering quality perfumes at affordable prices. The website will serve as "
    "the primary digital storefront, featuring product showcases, brand identity, and WhatsApp-based ordering.",
    body_style
))
story.append(Spacer(1, 10))

# === SCOPE & DELIVERABLES ===
story.append(Paragraph("Scope & Deliverables", heading_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E5E7EB"), spaceAfter=10))

deliverables = [
    ["#", "Deliverable", "Description"],
    ["1", "Custom UI/UX Design", "Premium dark-themed design with purple & gold accents, tailored to fragrance branding"],
    ["2", "Responsive Development", "Fully responsive website optimized for mobile, tablet, and desktop devices"],
    ["3", "Product Showcase", "Interactive product cards with pricing, images, and WhatsApp order buttons"],
    ["4", "Services Section", "Scent Consultation, Easy WhatsApp Orders, and Gift Packaging sections"],
    ["5", "Image Gallery", "Curated photo gallery showcasing products and brand lifestyle"],
    ["6", "WhatsApp Integration", "Floating 'Chat to Order' button and direct WhatsApp links for easy ordering"],
    ["7", "Scroll Animations", "Smooth fade-in and slide animations for a premium user experience"],
    ["8", "SEO Basics", "Meta tags, page titles, and structured content for search engine visibility"],
    ["9", "Deployment", "Live deployment on Netlify with SSL certificate and custom domain support"],
    ["10", "Source Code", "Full source code delivered via GitHub repository"],
]

# Convert to Paragraphs for wrapping
del_data = []
for i, row in enumerate(deliverables):
    if i == 0:
        del_data.append([
            Paragraph(f"<b>{row[0]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white, alignment=TA_CENTER)),
            Paragraph(f"<b>{row[1]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white)),
            Paragraph(f"<b>{row[2]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white)),
        ])
    else:
        del_data.append([
            Paragraph(row[0], ParagraphStyle('', parent=body_style, alignment=TA_CENTER, fontSize=10)),
            Paragraph(f"<b>{row[1]}</b>", ParagraphStyle('', parent=body_style, fontSize=10)),
            Paragraph(row[2], ParagraphStyle('', parent=body_style, fontSize=10)),
        ])

del_table = Table(del_data, colWidths=[30, 140, 330])
del_table.setStyle(TableStyle([
    # Header
    ('BACKGROUND', (0, 0), (-1, 0), PURPLE),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    # Alternating rows
    ('BACKGROUND', (0, 1), (-1, 1), LIGHT_BG),
    ('BACKGROUND', (0, 3), (-1, 3), LIGHT_BG),
    ('BACKGROUND', (0, 5), (-1, 5), LIGHT_BG),
    ('BACKGROUND', (0, 7), (-1, 7), LIGHT_BG),
    ('BACKGROUND', (0, 9), (-1, 9), LIGHT_BG),
    # Grid
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ('ROUNDEDCORNERS', [4, 4, 4, 4]),
]))
story.append(del_table)
story.append(Spacer(1, 15))

# === PRICING ===
story.append(Paragraph("Investment", heading_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E5E7EB"), spaceAfter=10))

pricing_data = [
    ["Item", "Amount"],
    ["Website Design & Development", "N200,000"],
    ["WhatsApp Integration & Animations", "N25,000"],
    ["Deployment & GitHub Setup", "N15,000"],
    ["SEO & Optimization", "N10,000"],
    ["", ""],
    ["TOTAL", "N250,000"],
]

price_table_data = []
for i, row in enumerate(pricing_data):
    if i == 0:
        price_table_data.append([
            Paragraph(f"<b>{row[0]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white)),
            Paragraph(f"<b>{row[1]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white, alignment=TA_RIGHT)),
        ])
    elif i == len(pricing_data) - 1:
        price_table_data.append([
            Paragraph(f"<b>{row[0]}</b>", ParagraphStyle('', parent=body_style, fontSize=14, fontName='Helvetica-Bold')),
            Paragraph(f"<b>{row[1]}</b>", ParagraphStyle('', parent=body_style, fontSize=14, fontName='Helvetica-Bold', textColor=PURPLE, alignment=TA_RIGHT)),
        ])
    elif i == len(pricing_data) - 2:
        price_table_data.append([Paragraph("", body_style), Paragraph("", body_style)])
    else:
        price_table_data.append([
            Paragraph(row[0], body_style),
            Paragraph(row[1], ParagraphStyle('', parent=body_style, alignment=TA_RIGHT)),
        ])

price_table = Table(price_table_data, colWidths=[350, 150])
price_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), PURPLE),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#F3F0FF")),
    ('LINEABOVE', (0, -1), (-1, -1), 2, PURPLE),
    ('GRID', (0, 0), (-1, -2), 0.5, colors.HexColor("#E5E7EB")),
    ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#E5E7EB")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
]))
story.append(price_table)
story.append(Spacer(1, 20))

# === TIMELINE ===
story.append(Paragraph("Project Timeline", heading_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E5E7EB"), spaceAfter=10))

timeline_data = [
    ["Phase", "Duration", "Details"],
    ["Discovery & Design", "3 - 4 Days", "Brand review, wireframing, and UI design mockup"],
    ["Development", "5 - 7 Days", "Frontend coding, animations, and responsive layout"],
    ["Integration & Testing", "2 - 3 Days", "WhatsApp setup, cross-browser & device testing"],
    ["Deployment & Handover", "1 - 2 Days", "Netlify deployment, GitHub repo, and client walkthrough"],
]

tl_data = []
for i, row in enumerate(timeline_data):
    if i == 0:
        tl_data.append([
            Paragraph(f"<b>{row[0]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white)),
            Paragraph(f"<b>{row[1]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white, alignment=TA_CENTER)),
            Paragraph(f"<b>{row[2]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white)),
        ])
    else:
        tl_data.append([
            Paragraph(f"<b>{row[0]}</b>", ParagraphStyle('', parent=body_style, fontSize=10)),
            Paragraph(row[1], ParagraphStyle('', parent=body_style, fontSize=10, alignment=TA_CENTER, textColor=PURPLE, fontName='Helvetica-Bold')),
            Paragraph(row[2], ParagraphStyle('', parent=body_style, fontSize=10)),
        ])

tl_table = Table(tl_data, colWidths=[140, 100, 260])
tl_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), PURPLE),
    ('BACKGROUND', (0, 1), (-1, 1), LIGHT_BG),
    ('BACKGROUND', (0, 3), (-1, 3), LIGHT_BG),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
]))
story.append(tl_table)

story.append(Spacer(1, 8))
story.append(Paragraph(
    "<b>Estimated Total Duration:</b> 11 - 16 business days from project kickoff.",
    ParagraphStyle('', parent=body_style, textColor=PURPLE, fontSize=11)
))
story.append(Spacer(1, 10))

# === PAYMENT TERMS ===
story.append(Paragraph("Payment Terms", heading_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E5E7EB"), spaceAfter=10))

payment_data = [
    ["Milestone", "Percentage", "Amount", "When"],
    ["Deposit", "50%", "N125,000", "Before project starts"],
    ["Final Payment", "50%", "N125,000", "Upon delivery & approval"],
]

pay_data = []
for i, row in enumerate(payment_data):
    if i == 0:
        pay_data.append([
            Paragraph(f"<b>{row[0]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white)),
            Paragraph(f"<b>{row[1]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white, alignment=TA_CENTER)),
            Paragraph(f"<b>{row[2]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white, alignment=TA_RIGHT)),
            Paragraph(f"<b>{row[3]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white)),
        ])
    else:
        pay_data.append([
            Paragraph(f"<b>{row[0]}</b>", body_style),
            Paragraph(row[1], ParagraphStyle('', parent=body_style, alignment=TA_CENTER, textColor=PURPLE, fontName='Helvetica-Bold')),
            Paragraph(row[2], ParagraphStyle('', parent=body_style, alignment=TA_RIGHT, fontName='Helvetica-Bold')),
            Paragraph(row[3], ParagraphStyle('', parent=body_style, fontSize=10)),
        ])

pay_table = Table(pay_data, colWidths=[120, 80, 120, 180])
pay_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), PURPLE),
    ('BACKGROUND', (0, 1), (-1, 1), LIGHT_BG),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
]))
story.append(pay_table)
story.append(Spacer(1, 15))

# Payment methods
story.append(Paragraph("<b>Accepted Payment Methods:</b>", body_style))
story.append(Paragraph("Bank Transfer | Opay | PalmPay", ParagraphStyle('', parent=body_style, textColor=PURPLE, fontName='Helvetica-Bold')))
story.append(Spacer(1, 15))

# === OPTIONAL ADD-ONS ===
story.append(Paragraph("Optional Add-ons", heading_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E5E7EB"), spaceAfter=10))

addon_data = [
    ["Add-on Service", "Price"],
    ["Full E-commerce (Cart + Paystack/Flutterwave)", "N100,000 - N300,000"],
    ["Custom Domain Purchase & Setup", "N10,000 - N20,000"],
    ["Advanced SEO Optimization", "N30,000 - N50,000"],
    ["Monthly Maintenance & Updates", "N15,000 - N30,000/month"],
    ["Professional Copywriting", "N20,000 - N40,000"],
    ["Logo Design / Brand Identity", "N30,000 - N60,000"],
]

addon_table_data = []
for i, row in enumerate(addon_data):
    if i == 0:
        addon_table_data.append([
            Paragraph(f"<b>{row[0]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white)),
            Paragraph(f"<b>{row[1]}</b>", ParagraphStyle('', parent=small_style, textColor=colors.white, alignment=TA_RIGHT)),
        ])
    else:
        addon_table_data.append([
            Paragraph(row[0], body_style),
            Paragraph(row[1], ParagraphStyle('', parent=body_style, alignment=TA_RIGHT, textColor=GRAY_TEXT)),
        ])

addon_table = Table(addon_table_data, colWidths=[320, 180])
addon_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), PURPLE),
    ('BACKGROUND', (0, 1), (-1, 1), LIGHT_BG),
    ('BACKGROUND', (0, 3), (-1, 3), LIGHT_BG),
    ('BACKGROUND', (0, 5), (-1, 5), LIGHT_BG),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E5E7EB")),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
]))
story.append(addon_table)
story.append(Spacer(1, 20))

# === TERMS & CONDITIONS ===
story.append(Paragraph("Terms & Conditions", heading_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E5E7EB"), spaceAfter=10))

terms = [
    "This proposal is valid for 30 days from the date of issue.",
    "The project timeline begins upon receipt of the initial deposit.",
    "Up to 2 rounds of revisions are included. Additional revisions will be billed separately.",
    "All intellectual property and source code will be transferred to the client upon final payment.",
    "The developer reserves the right to showcase the project in their portfolio unless otherwise agreed.",
    "Hosting fees (if applicable) are separate and the client's responsibility after handover.",
]

for i, term in enumerate(terms):
    story.append(Paragraph(
        f"<b>{i+1}.</b> {term}",
        ParagraphStyle('', parent=body_style, fontSize=10, leftIndent=15, spaceAfter=4)
    ))

story.append(Spacer(1, 25))

# === ACCEPTANCE ===
story.append(Paragraph("Acceptance", heading_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E5E7EB"), spaceAfter=10))

story.append(Paragraph(
    "By signing below, you confirm acceptance of this proposal and agree to the terms outlined above.",
    body_style
))
story.append(Spacer(1, 25))

sig_data = [
    [
        Paragraph("<b>Client Signature</b>", ParagraphStyle('', parent=small_style, textColor=PURPLE)),
        Paragraph("", body_style),
        Paragraph("<b>Developer Signature</b>", ParagraphStyle('', parent=small_style, textColor=PURPLE)),
    ],
    [
        Paragraph("_________________________", body_style),
        Paragraph("", body_style),
        Paragraph("_________________________", body_style),
    ],
    [
        Paragraph("Name:", small_style),
        Paragraph("", body_style),
        Paragraph("Chimudi Nwosu", small_style),
    ],
    [
        Paragraph("Date:", small_style),
        Paragraph("", body_style),
        Paragraph(f"Date: {today.strftime('%B %d, %Y')}", small_style),
    ],
]

sig_table = Table(sig_data, colWidths=[200, 100, 200])
sig_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'BOTTOM'),
    ('TOPPADDING', (0, 0), (-1, -1), 4),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
]))
story.append(sig_table)
story.append(Spacer(1, 30))

# Footer
story.append(HRFlowable(width="100%", thickness=1, color=PURPLE, spaceAfter=8))
story.append(Paragraph(
    "Thank you for considering this proposal. Looking forward to working with you!",
    ParagraphStyle('', parent=body_style, alignment=TA_CENTER, textColor=PURPLE, fontName='Helvetica-BoldOblique', fontSize=12)
))
story.append(Paragraph(
    "Chimudi Nwosu | Web Developer | Lagos, Nigeria",
    ParagraphStyle('', parent=small_style, alignment=TA_CENTER, spaceAfter=4)
))

# Build
doc.build(story)
print(f"Proposal created: {output_path}")
