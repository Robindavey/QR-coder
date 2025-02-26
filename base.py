
import qrcode

# Localhost URL pointing to the PDF file
pdf_url = "http://localhost:8000/CHECK-LIST-PETC_en-US 1.pdf"

# Generate QR code
qr = qrcode.make(pdf_url)
qr.save("qr_code.png")

print("QR Code generated! Scan it to access the local PDF.")
