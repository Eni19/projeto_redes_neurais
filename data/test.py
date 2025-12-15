import pandas as pd
import os
from PIL import Image
import matplotlib.pyplot as plt

IMAGE_DIR = r"data\images"   # simples e fixo

df = pd.read_csv("captions.csv")
row = df.iloc[0]

img_path = os.path.join(IMAGE_DIR, row["image"])

print("Abrindo:", img_path)
print("Existe?", os.path.exists(img_path))

img = Image.open(img_path)
plt.imshow(img)
plt.axis("off")
plt.show()
