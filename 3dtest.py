import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("data2.png", cv2.IMREAD_GRAYSCALE)

y = np.arange(img.shape[0])
x = np.arange(img.shape[1])
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection = "3d")
ax.plot_surface(X, Y, img, cmap='jet', linewidth=0)
plt.show()
