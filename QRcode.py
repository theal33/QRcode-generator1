import qrcode as qr

img =qr.make("https://www.example.com")

img.save("example.png")
