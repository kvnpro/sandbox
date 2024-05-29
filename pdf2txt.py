from pdf2image import convert_from_path
import cv2
import pytesseract
import numpy as np


def deskew(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bitwise_not(gray)
    coords = np.column_stack(np.where(gray > 0))
    angle = cv2.minAreaRect(coords)[-1]

    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(
        image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE
    )

    return rotated


def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text


easy_text_path = "/Users/kevin/Desktop/Tower73-pages.pdf"
pages = convert_from_path(easy_text_path)
# easy_img = cv2.imread(easy_text_path)

for page in pages:
    preprocessed_image = deskew(np.array(page))
    text = extract_text_from_image(preprocessed_image)

    print(text)
    print("_____________________")
