import ebooklib
from ebooklib import epub

book = epub.read_epub(
    "/Users/kevin/Documents/Digital Editions/Complete Guide to TRX Suspension Training.epub"
)

for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
    print(image)
