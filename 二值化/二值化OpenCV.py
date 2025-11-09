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
# 使用OpenCV 的接口去二值化一个灰度图
# ret中存放二值化所用到的阈值，ret没有任何作用
# 当我们使用OTSU计算最合适的阈值时，ret就有用了
# image_thresh 存放二值化后的图，本质上是一个单通道数组
ret, image_thresh = cv2.threshold(
    image_gray,  # 需要二值化的图像
    thresh,  # 阈值
    maxval,  # 最大值
    cv2.THRESH_BINARY,  # 使用阈值法二值化对象
)
# 单通道图也需要表示长宽，所以需要二维数组
print(image_thresh)
cv2.imwrite("./twoOpenCv.png", image_thresh)
# 使用opencv的函数 imshow去显示结果
# 显示原图
cv2.imshow("image_np", image_np)
# 显示灰度图
cv2.imshow("image_gray", image_gray)
# 显示二值化结果
cv2.imshow("image_thresh", image_thresh)

cv2.waitKey()
