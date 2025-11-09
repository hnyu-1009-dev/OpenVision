# 对图像做自适应二值化的彩色图
import cv2
import numpy as np

# 1.读取一张想要进行自适应二值化的彩色图
image_np = cv2.imread("../image/image.jpg")


# 2. 读取收到的彩色图像进行灰度化
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)


# 3. 对转化好的灰度图进行自适应二值化
# cv2.adaptiveThreshold
# 第一个参数：单通道图
# 第二个参数：二值化过程中所用到的最大值
# 第三个参数：计算与之的方法：1.平均值法 cv2.ADAPTIVE_THRESH_MEAN_C
#                          2.使用高斯和的加权平均法  cv2.THRESH_BINARY
# 第四个参数：二值化的方法：1.阈值法cv2.THRESH_BINARY 2.反阈值法cv2.THRESH_BINARY_INV
# 第五个参数：blocksize： 核的大小，通常位技术 3*3 5*5
# 第六个参数：要减去的常数C的大小 通常是证书，但也有可能是0 或 复数
image_binary = cv2.adaptiveThreshold(
    image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10
)

# 4.对计算的结果进行显示
cv2.imshow("image_np", image_np)
cv2.imshow("image_gray", image_gray)
cv2.imshow("image_binary", image_binary)

cv2.waitKey()
