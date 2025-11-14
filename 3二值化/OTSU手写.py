# 使用OTSU去计算合适的阈值并结合阈值法去二值化一张图像，且图像必须是灰度图
import cv2
import numpy as np

# 1.使用OpenCV去读取一张图片
image_np = cv2.imread("../image/image.jpg")
# 使用cv2.resize去改变图像的宽和高
# image_np = cv2.resize(image_np, (300, 300))

# 2. 使用OpenCv的函数去灰度化彩色图
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3.根据公式计算OTSU
# 使用np数组中的min（）函数获取数组中的最小值
min_value = image_gray.min()

# 使用np数组的max（）获取数组中的最大值

max_value = image_gray.max()

# 使用np数组中的shape属性获取灰度图的高度和宽度
image_shape = image_np.shape

image_thresh = np.zeros(image_shape, dtype=np.uint8)
# 定义计算最大类间方差中所定义的变量
n_0 = 0  # 前景像素点数
n_1 = 0  # 背景像素点数
w_0 = 0  # 前景像素点数占整幅图像的比例
w_1 = 0  # 背景像素点数占整幅图像的比例
u_0 = 0  # 前景的平均像素值
u_1 = 0  # 背景的平均像素值
u = 0  # 整幅的平均像素值
rows = image_shape[0]
cols = image_shape[1]

# 定义一个字典用来存储每一个阈值对应的最大类间方差，后面方便获取合适的阈值
var = {}

# 用来控制阈值T取值的循环，其取值返回是灰度图中的最小像素值+1
for t in range(min_value + 1, max_value):
    # 定义一个列表存储前景像素点
    foreground = []
    # 定义一个列表存储后景像素点
    background = []
    # 定义一个变量用来存储前景的像素值的总数
    forepix = 0
    # 定义一个变量用来存储背景的像素值的总数
    backpix = 0
    # 定义一个变量用来记录所有像素值的总和
    pix = 0
    # 使用嵌套for循环遍历灰度图，用来区分在当前阈值下哪些点是前景点，哪些值是背景点
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            # 统计图像的总像素值
            pix += image_gray[i, j]
            # 将灰度图的每个像素点和阈值进行比较，如果大于阈值就是前景像素点
            if image_gray[i, j] > t:
                foreground.append([i, j])
                # 求前景像素点的总像素值
                forepix += image_gray[i, j]
            else:
                background.append([i, j])
                # 求背景像素点的总像素值
                backpix += image_gray[i, j]
    # 获取前景像素点数
    n_0 = len(foreground)

    # 获取背景像素点水
    n_1 = len(background)

    # 通过计算获取w_0
    w_0 = n_0 / (image_shape[0] * image_shape[1])

    # 通过计算获取w_1
    w_1 = n_1 / (image_shape[0] * image_shape[1])

    # 通过计算获取前景的平均像素值
    u_0 = forepix / n_0

    # 通过计算获取背景的平均像素值
    u_1 = backpix / n_1

    # 通过计算获取整幅图的平均像素值
    u = pix / (image_shape[0] * image_shape[1])

    # 通过最大类间方差公式去计算最后的结果
    g = w_0 * ((u_0 - u) ** 2) + w_1 * ((u_1 - u) ** 2)
    # 将阈值和最大类间方差填入字典中
    var[t] = g

# for循环结束后就可以去比较最大类间方差了
# 寻找字典中最大的值所对应的键
thresh = max(var, key=var.get)
maxval = 255

# 使用一个嵌套for循环进行二值化操作
for i in range(image_shape[0]):  # 遍历高
    for j in range(image_shape[1]):  # 遍历宽

        if image_gray[i, j] > thresh:
            image_thresh[i, j] = maxval
        # 否则设置为0
        else:
            image_thresh[i, j] = 0

cv2.imshow("image_gray", image_gray)
cv2.waitKey()
