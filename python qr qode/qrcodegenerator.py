# 1.) install library qrcode = pip install qrcode
# 2.) install python 3.12 di microsoft store yg error di pip
# 3.) install library image = pip install image
# 4.) code . untuk membuka vscode lewat terminal

import qrcode # import library yg akan dipakai
import image
qr = qrcode.QRCode(
    version = 15, #untuk versi qr codenya
    box_size = 10, #untuk ukuran qr codenya
    border = 5 #ukuran putih2nya qr code
)

data = "https://www.youtube.com/watch?v=buvWBOZTfdc&pp=ygURbWluZCBvdmVyIG1hdHRlciA%3D" #link qr code 

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill= "black", back_color = "white") #setting warna qr code
img.save("link.png") #untuk build qr ke gambar png