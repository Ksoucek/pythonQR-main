import time

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

# from qrcode_xcolor import XStyledPilImage, XGappedSquareModuleDrawer, XRoundedModuleDrawer

qr = qrcode.QRCode()
qr.add_data("https://www.hanackabrest.cz/")

img = qr.make_image(
    image_factory=StyledPilImage,
    color_mask=SolidFillColorMask(
        front_color=(204,45, 65),
        back_color=(255, 255, 255),
    ),
    module_drawer=RoundedModuleDrawer(),
    eye_drawer=RoundedModuleDrawer(),
    embeded_image_path='H_znak_05.png',
)
img.save("qrcode_color_mask.png")


# st = time.time()
# qr = qrcode.QRCode()
# qr.add_data("https://www.hanackabrest.cz/")
# # The 4th value in all the colors is the opacity the color should use (0=clear <--> 255=solid)
# img = qr.make_image(
#     # Custom image factory
#     image_factory=XStyledPilImage,
#     back_color=(255, 255, 255, 255),  # Background color with opacity support
#     module_drawer=XGappedSquareModuleDrawer(
#         front_color=(59, 89, 152, 255),
#     ),
#     eye_drawer=XRoundedModuleDrawer(
#         front_color=(255, 110, 0, 255),
#         inner_eye_color=(65, 14, 158, 255),  # Only valid with the eye_drawer
#     ),
#     embeded_image_path='docs/gitlab.png',  # Still supports embedding logos in the middle
# )
# img.save("qrcode-xcolor.png")
# print(f"qrcode-xcolor: {time.time() - st:.4f}s")