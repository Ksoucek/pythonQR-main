import qrcode 
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H , box_size=20  ,border= 2)
qr.add_data('data')

qr_eyes_img = qr.make_image(
image_factory=StyledPilImage,
eye_drawer=RoundedModuleDrawer(radius_ratio=(1)),
color_mask=SolidFillColorMask(back_color=(255, 255, 255), front_color=(199 , 8 ,8 ))
)

qr_img = qr.make_image(
image_factory=StyledPilImage,
module_drawer=RoundedModuleDrawer(),
embeded_image_path='H_znak_05.png'
)

def style_eyes(img):
    img_size = img.size[0]
    box_size = img.box_size
    border_size = (img_size/box_size - 33 ) /2
    quiet_zone = box_size * border_size
    eye_size = 7 * box_size
    quiet_eye_size = eye_size + quiet_zone
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rectangle((quiet_zone, quiet_zone,quiet_eye_size,quiet_eye_size), fill=255)
    draw.rectangle((img_size-quiet_eye_size, quiet_zone, img_size-quiet_zone, quiet_eye_size), fill=255)
    draw.rectangle((quiet_zone, img_size-quiet_eye_size, quiet_eye_size, img_size-quiet_zone), fill=255)
    return mask

mask = style_eyes(qr_eyes_img)

img_rounded = Image.composite(qr_eyes_img, qr_img, mask)

img_rounded.save('qr_rounded.png')