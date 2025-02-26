import qrcode

# Create a QR code object with a larger size and higher error correction
qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)
data = input("Enter the Google/OneDrive link to PDF: ")
qr_name = input("Enter QR code: ")
# Define the data to be encoded in the QR code
#data = "https://1drv.ms/b/c/79c303d76318eadb/EdvqGGPXA8MggHmh1gEAAAABDwhQLd6owmMuJqU8uF-61Q?e=Sg3ARa"

# Add the data to the QR code object
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code with a black fill color and white background
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save(f"{qr_name}.png")