
# Image Rotation

from PIL import Image       # Pillow Library

img_path = Image.open("C:\\Users\\JavedAnsari\\Desktop\\Images\\qq.png")

rot_90 = img_path.rotate(90)
rot_180 = img_path.rotate(180)
rot_270 = img_path.rotate(270)

img_path.show()
rot_180.show()
rot_270.show()