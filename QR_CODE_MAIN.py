import tkinter as tk
from tkinter import messagebox

import qrcode
def make_qr_code():
    """Dummy function to be replaced with actual QR code generation logic"""
    global link_address, qr_code_name
    if link_address.get() and qr_code_name.get():
        messagebox.showinfo("Success", f"Generating QR Code for:\n{link_address.get()}\nFile Name: {qr_code_name.get()}.png")
    else:
        messagebox.showwarning("Input Error", "Please fill in both fields.")
    # Create a QR code object with a larger size and higher error correction
    qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

    # Define the data to be encoded in the QR code
    data = link_address

    # Add the data to the QR code object
    qr.add_data(data)

    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code with a black fill color and white background
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save(f"{qr_code_name}.png")
# Create main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x250")
root.resizable(False, False)

# Large label prompting the user
label = tk.Label(root, text="Enter the link for QR Code:", font=("Arial", 14), pady=10)
label.pack()

# Entry field for link
link_address = tk.StringVar()
entry_link = tk.Entry(root, textvariable=link_address, font=("Arial", 12), width=40)
entry_link.pack(pady=5)

# Label for QR code name
label_name = tk.Label(root, text="Enter QR Code file name:", font=("Arial", 12))
label_name.pack()

# Entry field for QR code name
qr_code_name = tk.StringVar()
entry_name = tk.Entry(root, textvariable=qr_code_name, font=("Arial", 12), width=40)
entry_name.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", font=("Arial", 12), command=make_qr_code, bg="green", fg="white")
convert_button.pack(pady=15)

# Run the application
root.mainloop()
