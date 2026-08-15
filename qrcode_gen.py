import qrcode

data=input("enter text or URL").strip()
filename=input("enter filename").strip()

qr=qrcode.QRCode(box_size=10,border=4)
qr.add_data(data)
image=qr.make_image(fill_color='black',back_color='white')
image.save(filename)
print(f"QR CODE SAVED AS {filename}")