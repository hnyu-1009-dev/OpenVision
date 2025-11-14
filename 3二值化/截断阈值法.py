# 截断阈值法
import cv2
import numpy as np

# 使用OpenCV去读取一张图片
image_np = cv2.imread("../image/huidu.png")

# 使用OpenCv的函数去灰度化彩色图
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 为了能遍历所有像素点，所以需要获取灰度图的形状
image_shape = image_np.shape
# 创建一个与灰度图大小相同的单通道图像，用来接受灰度图与阈值比较的结果
image_thresh = np.zeros(image_shape, np.uint8)
# 对灰度图进行二值化
# 使用阈值法
# 定义所需要的阈值
thresh = 127

# 定义阈值法所需要的最大值，几乎所有的二值化都需要最大值
maxval = 255

# 通过循环去遍历灰度图中的所有像素点，并和阈值进行比较：
# for i in range(image_shape[0]):
#     for j in range(image_shape[1]):
#         if image_gray[i, j] > thresh:
#             image_thresh[i, j] = thresh
#         else:
#             image_thresh[i, j] = image_gray[i, j]

# 使用OpenCV
ret, image_thresh = cv2.threshold(image_gray, thresh, maxval, cv2.THRESH_TRUNC)

cv2.imshow("image_gray", image_gray)
cv2.imshow("image_thresh", image_thresh)

cv2.waitKey()
