import numpy as np
import cv2
import glob
from skimage.morphology import convex_hull_image
import csv
import os

def convex(folder):
    # 指定したディレクトリの画像を抽出
    imgs = folder+"/*jpg"
    imgs_list = glob.glob(imgs)

    # データを出力するcsv作成
    filename = "result.csv"
    with open(filename, "w", newline="") as f:
        header = ['img_name', 'convex_hull_area']
        writer = csv.writer(f)
        writer.writerow(header)       

        for i in imgs_list:
            img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
            img_hull = convex_hull_image(img)
            img_t = np.where(img_hull == False, 0, 255).astype(np.uint8)
            s = cv2.countNonZero(img_t)
            i = os.path.basename(i)
            writer.writerow([i, s])

    return filename

if __name__ == "__main__":
    print(convex("source"))
