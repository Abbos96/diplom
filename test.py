import pandas as pd
import cv2


df = pd.read_csv('datasets/celeba/annotations/val.csv')

ok = []

for index, row in df.iterrows():
    img = cv2.imread('datasets/celeba/images/'+row.image_name)
    mask = cv2.imread('datasets/celeba/images/'+row.mask_name)

    print(img.shape)

# df = df.loc[ok]
# df.to_csv('val_filtered.csv', index=False)