import uuid
from PIL import Image
import qrcode
ticket = Image.open('VÉ THẦY CÔ .png')
from QR import QR
for index in range(1201, 1341):
    ID = uuid.uuid5(uuid.NAMESPACE_DNS, str(index))
    qr = QR(ID)
    qr = qr.resize((334, 334))
    ticket.paste(qr, (1422, 388))
    ticket.save(f'QRCODES/THAY_CO/{index}.png')

