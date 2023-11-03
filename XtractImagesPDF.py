import os
import fitz
import io
from PIL import Image
from pathlib import Path
from pprint import pprint

CarePlanDir = "/Users/kevin/Downloads"

outputDir = "/Users/kevin/CarePlan"
outputFormat = "png"

min_width = 100
min_height = 100


def outputImages(imageLst, imageMeta):
    ### https://thepythoncode.com/article/extract-pdf-images-in-python
    # imageLst = page.get_images(full=True)
    if imageLst:
        print(f"[+] Found a total of {len(imageLst)} images on page {pageIndex}")
        # print(f"[+] Found a total of {len(imageNamesLst)} image names.")
    else:
        print(f"[!] No images found on page {pageIndex}")
    for imageIndex, img in enumerate(imageLst, start=1):
        xref = img[0]
        baseImg = pdfFile.extract_image(xref)
        imageBytes = baseImg["image"]
        imageExt = baseImg["ext"]
        image = Image.open(io.BytesIO(imageBytes))
        if image.width >= min_width and image.height >= min_height:
            image.save(
                open(
                    f"{outputDir}/{imageMeta[imageIndex]['name']}.{outputFormat}",
                    "wb",
                ),
                format=outputFormat.upper(),
            )

            with open(
                f"{outputDir}/{imageMeta[imageIndex]['name']}.txt", "w"
            ) as txtFile:
                txtFile.write("\n".join(str(i) for i in imageMeta[imageIndex]["desc"]))
        else:
            print(
                f"[-] Skipping imge {imageIndex} on page {pageIndex} due to its size."
            )
    return


def outputText(page):
    ### https://thepythoncode.com/article/extract-text-from-pdf-in-python
    imageCapsLst = []
    imageCapsLst.append({})
    imgIdx = 0
    imageName = None
    desc = []
    pageLines = page.splitlines()

    for idx in range(len(pageLines)):
        line = pageLines[idx].strip()

        captionBlock = line.find("Sets:")
        if captionBlock > -1:
            if len(desc) > 0:
                if imageName is not None:
                    imageCapsLst[imgIdx]["name"] = imageName
                    imageCapsLst[imgIdx]["desc"] = desc[:-1]
                desc = []

            imageCapsLst.append({})
            imageName = pageLines[idx - 1]

            imgIdx += 1

        desc.append(pageLines[idx])

    if len(desc) > 0:
        imageCapsLst[imgIdx]["name"] = imageName
        imageCapsLst[imgIdx]["desc"] = desc[:-1]

    return imageCapsLst


if __name__ == "__main__":
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for f in Path(f"{CarePlanDir}/.").rglob("CarePlan*.pdf"):
        print(f.name)
        pdfFile = fitz.open(f"{CarePlanDir}/{f.name}")

        for pageIndex in range(len(pdfFile)):
            page = pdfFile[pageIndex]

            imageInfo = outputText(page.get_text())
            # pprint(f"{imageInfo[1:]}")
            outputImages(page.get_images(full=True), imageInfo)

        #
