import qrcode

url = input("Enter the url :").strip()

#Add a location to save the png file
file_paht = ""

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_paht)

print("QR code was generated")



