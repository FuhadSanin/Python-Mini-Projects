import qrcode

print("Welcome to the QR code Generator!!")

text = input("Enter the url: ")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20
)

qr.add_data(text)
qr.make(fit=True)
img = qr.make_image()
file_name = input("Enter the file name: ")
img.save(f"{file_name}.png")
