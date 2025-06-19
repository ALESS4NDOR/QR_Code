# Make sure you have the library installed with: pip install qrcode[pil]
import qrcode

data = "https://github.com/ALESS4NDOR"

# QRCode object is created
qr = qrcode.QRCode(
    version = 1, # Control QR size
    error_correction = qrcode.constants.ERROR_CORRECT_L, # Only 7% of the QR can be damaged before it becomes unreadable
    box_size = 10,
    border = 2,
)

qr.add_data(data)
qr.make(fit = True)

# The image is created with customized colors
img = qr.make_image(fill_color = "black", back_color = "white").convert("RGB")

img.save("QR_Code.jpg")

img.show()
