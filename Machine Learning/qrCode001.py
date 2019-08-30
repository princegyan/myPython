import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)

link ="https://www.youtube.com/watch?v=uOevCU4rRtY"

qr.add_data(link)
qr.make(fit=True)
img=qr.make_image(fill="red", back_color="white")
img.save("No Reason to Fear (Cover) - Hle Ntombela Mthethwa & Joyful Way Inc.png")