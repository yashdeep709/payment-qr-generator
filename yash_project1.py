import qrcode
from PIL import Image
import urllib.parse

def generate_phonepe_qr(upi_id, amount=None, filename="phonepe_payment_qr.png"):
    

    upi_url = f"upi://pay?pa={upi_id}&pn=&cu=INR"

    if amount:
        upi_url += f"&am={amount}"

    qr = qrcode.QRCode(
        version=None,
        box_size=10,
        border=4
    )
    qr.add_data(upi_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"PhonePe QR Code generated and saved as {filename}")
    return img


upi_id = input("Enter your UPI ID (example: yourname@upi): ")
amount = input("Enter amount (leave blank for custom amount): ")

amount = amount if amount.strip() != "" else None

img = generate_phonepe_qr(upi_id, amount)
img.show()
