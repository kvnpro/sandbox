import cv2
import pytesseract


def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text


easy_text_path = (
    "/Users/kevin/Desktop/SMA Parents Handbook with 75-76 Insert/Scan 29.png"
)

easy_img = cv2.imread(easy_text_path)


text = extract_text_from_image(easy_img)

print(text)
