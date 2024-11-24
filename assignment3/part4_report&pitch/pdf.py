from PIL import Image
from PyPDF2 import PdfMerger

# image = Image.open('scenario11-Newshack case.png')
# image.save('scenario11-Newshack case.pdf', 'PDF', resolution=100.0)

pdf1 = input('Please input pdf1 path:')
pdf2 = input('Please input pdf2 path:')
filename = input('Please input output path:')

merger = PdfMerger()
merger.append(pdf1)
merger.append(pdf2)

with open(filename, 'wb') as output:
    merger.write(output)

merger.close()