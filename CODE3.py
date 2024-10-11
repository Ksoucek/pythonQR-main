import qrcode
import PIL
from PIL import Image, ImageDraw
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from  qrcode.image.styles.colormasks import SolidFillColorMask

x = 1
def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def style_inner_eyes(img):
  img_size = img.size[0] * x
  eye_size = 70 * x #default
  quiet_zone = 40 * x#default
  mask = Image.new('L', img.size, 0)
  draw = ImageDraw.Draw(mask)
  draw.rectangle((60*x, 60*x, 90*x, 90*x), fill=255) #top left eye
  draw.rectangle((img_size-90*x, 60*x, img_size-60*x, 90*x), fill=255) #top right eye
  draw.rectangle((60*x, img_size-90*x, 90*x, img_size-60*x), fill=255) #bottom left eye
  return mask

def style_outer_eyes(img):
  img_size = img.size[0]
  eye_size = 70*x #default
  quiet_zone = 40*x #default
  mask = Image.new('L', img.size, 0)
  draw = ImageDraw.Draw(mask)
  draw.rectangle((40*x, 40*x, 110*x, 110*x), fill=255) #top left eye
  draw.rectangle((img_size-110*x, 40*x, img_size-40*x, 110*x), fill=255) #top right eye
  draw.rectangle((40*x, img_size-110*x, 110*x, img_size-40*x), fill=255) #bottom left eye
  draw.rectangle((60*x, 60*x, 90*x, 90*x), fill=0) #top left eye
  draw.rectangle((img_size-90*x, 60*x, img_size-60*x, 90*x), fill=0) #top right eye
  draw.rectangle((60*x, img_size-90*x, 90*x, img_size-60*x), fill=0) #bottom left eye  
  return mask  


if not hasattr(PIL.Image, 'Resampling'):
  PIL.Image.Resampling = PIL.Image
# Now PIL.Image.Resampling.BICUBIC is always recognized.

im = Image.open('H_znak_05.png')
im = add_corners(im, 400)
im.save('rounded-logo.png')


qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=(10* x))
url = 'https://www.hanackabrest.cz/'

qr.add_data(url)

qr_inner_eyes_img = qr.make_image(image_factory=StyledPilImage,
                            eye_drawer=RoundedModuleDrawer(radius_ratio=1),
                            color_mask=SolidFillColorMask(front_color=(204, 45, 65)))

qr_outer_eyes_img = qr.make_image(image_factory=StyledPilImage,
                            eye_drawer=RoundedModuleDrawer(radius_ratio=1))                            

qr_img = qr.make_image(image_factory=StyledPilImage,
                       module_drawer=RoundedModuleDrawer(),
                       embeded_image_path="rounded-logo.png")

inner_eye_mask = style_inner_eyes(qr_img)
outer_eye_mask = style_outer_eyes(qr_img)
intermediate_img = Image.composite(qr_inner_eyes_img, qr_img, inner_eye_mask)
final_image = Image.composite(qr_outer_eyes_img, intermediate_img, outer_eye_mask)
final_image.save("final.pnG")
final_image