# 使用OpenCV进行灰度化
import cv2

image_np = cv2.imread("../image/huidu.png")

# 默认使用加权平均值
image_gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)


cv2.imshow("image_np", image_np)
cv2.imshow("image_gray", image_gray)


cv2.waitKey()
