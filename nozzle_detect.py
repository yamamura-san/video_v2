import cv2
import numpy as np
import csv
import glob
import os
import pandas as pd

# 指定したフォルダ内の画像からノズルの下端位置を特定する関数
def nozzle_detect(folder):

    # フォルダ内の画像抽出
    dir = folder + "/*jpg"
    imgs_list = glob.glob(dir)

    # 下端位置の探索結果を格納するファイル作成
    filename = "nozzle_position.csv"
    with open(filename, "w", newline="") as f:
        header = ['img_name', 'nozzle_bottom_position']
        writer = csv.writer(f)
        writer.writerow(header)  
        
        # ループをかけて、抽出した画像を2値化してノズルの下端座標をcsvファイルへ
        for file in imgs_list:
            img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

            # ノイズ除去　メディアンフィルタ
            img = cv2.medianBlur(img, ksize=3)
            
            # ノズルだけが映るように2値化する閾値
            thresh = 10
            ret, img_binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

            # 画像内で255になる画素の最下段目を抽出
            bottom  = np.where(img_binary == 255)[0][-1]

            file = os.path.basename(file)        
            writer.writerow([file, bottom])
    
    # ノズルの下端位置の計算
    df = pd.read_csv(filename)
    nozzle_bottom_posi = df["nozzle_bottom_position"].max()
    return filename, nozzle_bottom_posi


if __name__ == "__main__":
    print(nozzle_detect("source"))