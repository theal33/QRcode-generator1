import qrcode as qr

img =qr.make("https://www.stemlab.com.ng")

img.save("stemlab.png")
