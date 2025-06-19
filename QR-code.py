import qrcode
from PIL import Image

data = input("QR code link: ")
filename  = input("Filename(default: qr_128x128): ")
qrsize = input("size for your qr code: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=1
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
img = img.resize((qrsize, qrsize), Image.NEAREST)

template = (filename or "qr_code") + ".png"
img.save(template)
print("Created your QR code as: ", template)
