from PIL import Image, ImageOps
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# 画像読み込み
org_img = Image.open('data.png')
# グレースケール化
img = ImageOps.grayscale(org_img)
# 配列化
data = np.asarray(img)

# データ表示
X,Y = np.mgrid[:data.shape[0], :data.shape[1]]
ax = plt.gca(projection='3d')
ax.plot_surface(X,Y,data,cmap='jet',edgecolor='k',rcount=15,ccount=15)
plt.show()