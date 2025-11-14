# 使用阈值法去二值化一张图像，且图像必须是灰度图
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


# 因为需要将灰度图中的所有像素点和阈值进行比较
# 所以需要使用循环去遍历灰度图，并去除所有的像素值于阈值进行一一比较
# 如果像素值大于阈值，就设置maxval，否则就设置0
for i in range(image_shape[0]):  # 遍历高
    for j in range(image_shape[1]):  # 遍历宽
        # 使用if判断灰度图中的第i行和第j列的像素点的值和阈值的大小关系
        # 如果灰度图的第i行第j列别阈值大，则将像素值设置为maxval
        if image_gray[i, j] > thresh:
            image_thresh[i, j] = maxval
        # 否则设置为0
        else:
            image_thresh[i, j] = 0
# 使用opencv的函数 imshow去显示结果
# 显示原图
cv2.imshow("image_np", image_np)
# 显示灰度图
cv2.imshow("image_gray", image_gray)
# 显示二值化结果
cv2.imshow("image_thresh", image_thresh)

cv2.waitKey()
