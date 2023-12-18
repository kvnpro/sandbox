from PIL import Image
from pathlib import Path

kevalbumDir = "/Users/kevin/Desktop/Album002"
kphotoDir = f"/Users/kevin/Desktop/Ross2crops"

for p in Path(f"{kevalbumDir}/.").rglob("*.jpeg"):
    print(f"{kevalbumDir}/{p.name}")
    img = Image.open(f"{kevalbumDir}/{p.name}")
    area = [(), (), (), (), (), ()]
    print(type(img))
    if p.name[-5] in ("1", "3", "5", "7", "9"):
        print(f"odd page:{p.name} -- {p.name[-5]}")
        area[0] = (0, 0, 1000, 1000)
        area[1] = (1345, 0, 2350, 1000)
        area[2] = (0, 1150, 1000, 2200)
        area[3] = (1345, 1150, 2350, 2200)
        area[4] = (0, 2250, 1000, 3300)
        area[5] = (1345, 2250, 2350, 3300)
    else:
        print(f"even page:{p.name} -- {p.name[-5]}")
        area[0] = (0, 0, 1000, 1000)
        area[1] = (1345, 0, 2350, 1000)
        area[2] = (0, 1150, 1000, 2200)
        area[3] = (1345, 1150, 2350, 2200)
        area[4] = (0, 2250, 1000, 3300)
        area[5] = (1345, 2250, 2350, 3300)
    for i in range(6):
        print(i)
        crop = img.crop(area[i])
        crop.save(f"{kphotoDir}/{p.name}-{i+1}.jpg")
