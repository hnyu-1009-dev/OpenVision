# 使用OTSU去计算合适的阈值并结合阈值法去二值化一张图像，且图像必须是灰度图
import cv2
import numpy as np

# 1.使用OpenCV去读取一张图片
image_np = cv2.imread("../image/huidu.png")

# 2. 使用OpenCv的函数去灰度化彩色图
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

image_shape = image_np.shape

image_thresh = np.zeros(image_shape, dtype=np.uint8)
# 对灰度图进行二值化
# 使用阈值法
# 定义所需要的阈值
thresh = 127

# 定义阈值法所需要的最大值，几乎所有的二值化都需要最大值
maxval = 255
# 3.使用反阈值法手写
for i in range(image_shape[0]):  # 遍历高
    for j in range(image_shape[1]):  # 遍历宽
        # 使用if判断灰度图中的第i行和第j列的像素点的值和阈值的大小关系
        # 如果灰度图的第i行第j列别阈值大，则将像素值设置为maxval
        if image_gray[i, j] < thresh:
            image_thresh[i, j] = maxval
        # 否则设置为0
        else:
            image_thresh[i, j] = 0

# 显示图像
cv2.imshow("image_thresh", image_thresh)
cv2.waitKey()
