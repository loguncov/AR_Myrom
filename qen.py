import qrcode
import os

# Список из 45 ссылок (пример, замените на свои)
urls = [
    "https://gzk.wildtourist.ru/ar/01/",
    "https://gzk.wildtourist.ru/ar/02/",
    "https://gzk.wildtourist.ru/ar/03/",
    "https://gzk.wildtourist.ru/ar/04/",
    "https://gzk.wildtourist.ru/ar/05/",
    "https://gzk.wildtourist.ru/ar/06/",
    "https://gzk.wildtourist.ru/ar/07/",
    "https://gzk.wildtourist.ru/ar/08/",
    "https://gzk.wildtourist.ru/ar/09/",
    "https://gzk.wildtourist.ru/ar/10/",
    "https://gzk.wildtourist.ru/ar/11/",
    "https://gzk.wildtourist.ru/ar/12/",
    "https://gzk.wildtourist.ru/ar/13/",
    "https://gzk.wildtourist.ru/ar/14/",
    "https://gzk.wildtourist.ru/ar/15/",
    "https://gzk.wildtourist.ru/ar/16/",
    "https://gzk.wildtourist.ru/ar/17/",
    "https://gzk.wildtourist.ru/ar/18/",
    "https://gzk.wildtourist.ru/ar/19/",
    "https://gzk.wildtourist.ru/ar/20/",
    "https://gzk.wildtourist.ru/ar/21/",
    "https://gzk.wildtourist.ru/ar/22/",
    "https://gzk.wildtourist.ru/ar/23/",
    "https://gzk.wildtourist.ru/ar/24/",
    "https://gzk.wildtourist.ru/ar/25/",
    "https://gzk.wildtourist.ru/ar/26/",
    "https://gzk.wildtourist.ru/ar/27/",
    "https://gzk.wildtourist.ru/ar/28/",
    "https://gzk.wildtourist.ru/ar/29/",
    "https://gzk.wildtourist.ru/ar/30/",
    "https://gzk.wildtourist.ru/ar/31/",
    "https://gzk.wildtourist.ru/ar/32/",
    "https://gzk.wildtourist.ru/ar/33/",
    "https://gzk.wildtourist.ru/ar/34/",
    "https://gzk.wildtourist.ru/ar/35/",
    "https://gzk.wildtourist.ru/ar/36/",
    "https://gzk.wildtourist.ru/ar/37/",
    "https://gzk.wildtourist.ru/ar/38/",
    "https://gzk.wildtourist.ru/ar/39/",
    "https://gzk.wildtourist.ru/ar/40/",
    "https://gzk.wildtourist.ru/ar/41/",
    "https://gzk.wildtourist.ru/ar/42/",
    "https://gzk.wildtourist.ru/ar/43/",
    "https://gzk.wildtourist.ru/ar/44/",
    "https://gzk.wildtourist.ru/ar/45/",
]
# Папка для сохранения QR-кодов

output_dir = "qr_codes"
os.makedirs(output_dir, exist_ok=True)

for i, url in enumerate(urls, 1):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(os.path.join(output_dir, f"{i}.png"))

print("QR-коды созданы в папке qr_codes")
