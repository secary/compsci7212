from PIL import Image

image = Image.open('scenario11-Newshack case.png')
image.save('scenario11-Newshack case.pdf', 'PDF', resolution=100.0)