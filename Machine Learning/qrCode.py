import qrcode

qr = qrcode.make("Hello Prince")
qr.save("myQR.png")