from PIL import Image
from PyPDF2 import PdfMerger

image = Image.open('scenario11-Newshack case.png')
image.save('scenario11-Newshack case.pdf', 'PDF', resolution=100.0)

merger = PdfMerger()
merger.append('scenario11-Newshack case.pdf')
merger.append('reference.pdf')

with open('mindmap_scenario11.pdf', 'wb') as output:
    merger.write(output)

merger.close()