# Make sure you have the library installed with: pip install qrcode[pil]
import qrcode
from PIL import Image

data = "https://www.nike.com"
#data = "https://www.youtube.com/watch?v=GBIIQ0kP15E&pp=ygUOcmljayByb2xsIG1lbWU%3D"

# QRCode object is created
qr = qrcode.QRCode(
    version = 5, # Increase the size of the QR if the logo is large
    error_correction = qrcode.constants.ERROR_CORRECT_H, # Allows up to 30% of the QR code to be damaged and still readable
    box_size = 10,
    border = 2,
)

qr.add_data(data)
qr.make(fit = True)

# The image is created with customized colors
qr_img = qr.make_image(fill_color = "black", back_color = "white").convert("RGB")

# The logo is loaded
logo = Image.open("logo.png") # The logo always has to be .png, you can change the example image

logo_size = qr_img.size[0] // 4 # Shifts to 1/4 the size of the QR
logo = logo.resize((logo_size, logo_size), Image.LANCZOS) # Maintains quality by reducing the image, preventing it from being pixelated or blurred
pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2) # Calculate the position to center the logo

# The logo is pasted on the QR
qr_img.paste(logo, pos, mask = logo if logo.mode == "RGBA" else None) # Allows transparent parts of the logo not to cover the QR

qr_img.save("QR_Code_Logo.jpg")

qr_img.show()
