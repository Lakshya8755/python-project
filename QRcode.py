import qrcode as qr
img = qr.make("xyz@gmail.com")
img.save("Email.png")