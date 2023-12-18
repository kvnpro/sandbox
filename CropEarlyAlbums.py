from PIL import Image
from pathlib import Path

kevalbumDir = "/Users/kevin/Desktop/album pages"
kphotoDir = f"/Users/kevin/Desktop/crops"

for p in Path(f"{kevalbumDir}/.").rglob("*.jpg"):
    print(f"{kevalbumDir}/{p.name}")
    img = Image.open(f"{kevalbumDir}/{p.name}")
    area = [(), (), (), (), (), ()]
    print(type(img))
    if p.name[-5] in ("1", "3", "5", "7", "9"):
        print(f"odd page:{p.name} -- {p.name[-5]}")
        area[0] = (240, 1, 1300, 1100)
        area[1] = (1400, 1, 2460, 1100)
        area[2] = (240, 1120, 1300, 2200)
        area[3] = (1400, 1200, 2440, 2240)
        area[4] = (240, 2220, 1275, 3300)
        area[5] = (1400, 2220, 2400, 3270)
    else:
        print(f"even page:{p.name} -- {p.name[-5]}")
        area[0] = (180, 1, 1220, 1070)
        area[1] = (1260, 1, 2370, 1100)
        area[2] = (180, 1120, 1220, 2160)
        area[3] = (1260, 1120, 2370, 2160)
        area[4] = (180, 2230, 1220, 3270)
        area[5] = (1260, 2230, 2370, 3270)
    for i in range(6):
        print(i)
        crop = img.crop(area[i])
        crop.save(f"{kphotoDir}/{p.name}-{i+1}.jpg")
