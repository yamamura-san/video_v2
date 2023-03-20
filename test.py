import numpy as np
import cv2
import random
import matplotlib.pyplot as plt
from skimage.morphology import convex_hull_image

img = np.zeros((500, 500), dtype= np.uint8)

random_num = 150

r_list = [random.randint(1, 100) for i in range(random_num)]
theta_list = [random.uniform(0, 6.27) for i in range(random_num)]

for i in range(len(r_list)):
    y = 250 - int(r_list[i] * np.sin(theta_list[i]))
    x = 250 + int(r_list[i] * np.cos(theta_list[i]))
    img[y][x] = 255

img_hull = convex_hull_image(img)

img_t = np.where(img_hull == False, 0, 255).astype(np.uint8)

print(cv2.countNonZero(img_t))


cv2.imshow('title',img)
cv2.waitKey()
cv2.imshow('title',img_t)
cv2.waitKey()
cv2.destroyAllWindows()