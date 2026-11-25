import pyqrcode
import png
from pyqrcode import QRCode

path = "https://drive.google.com/file/d/1O_ANvi2erW2g8xHsYgMDc9QDeUivUD25/view?usp=sharing"

url = pyqrcode.create(path)
myqr = qrcode(url)
print("myqr.png", mtqr)