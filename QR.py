# generate qr code for any link

import qrcode as qr
img = qr.make("https://www.canva.com/")
img.save("Canva_web.png")


