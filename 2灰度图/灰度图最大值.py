# 在文件中，使用最大值的方法去灰度化一张彩色图
# 最大值的灰度化方法适合于偏暗的图像
import cv2
import numpy as np

# 1.使用opencv的imread方法读取需要灰度化的图片
image_np = cv2.imread("../image/huidu.png")

# 2.获取彩色图的形状，方便后面建立灰度图的模板
# shape 获取到的顺序是高和宽
image_shape = image_np.shape

# 3.创建灰度图模板，方便后续去接受彩色图所计算的灰度结果
# numpy.zeros也是按照高和宽的顺序去创建图像的
image_gray = np.zeros((image_shape[0], image_shape[1]), dtype=np.uint8)

# 4.遍历像素点，求取最大的部分
# 使用嵌套的for循环去遍历彩色图的所有像素点
for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        list = []
        list.append(int(image_np[i, j][0]))
        list.append(int(image_np[i, j][1]))
        list.append(int(image_np[i, j][2]))
        image_gray[i][j] = max(list)

# 5.显示图像
cv2.imshow("image_np", image_np)
cv2.imshow("image_gray", image_gray)

cv2.waitKey()
