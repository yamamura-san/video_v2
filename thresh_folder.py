import cv2
import os
import glob

def thresh_folder(folder, thresh):
    # 二値化結果を格納するフォルダ作成
    folder_name = "xxx_binary"
    os.makedirs(folder_name, exist_ok=True)

    # 指定したディレクトリの画像を抽出
    imgs = folder+"/*jpg"
    imgs_list = glob.glob(imgs)

    for i in imgs_list:
        img = cv2.imread(i, cv2.IMREAD_GRAYSCALE)
        ret, img_bin = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
        i = os.path.basename(i)
        cv2.imwrite(folder_name + "/" +i, img_bin)

if __name__ == "__main__":
    thresh_folder("source", 100)