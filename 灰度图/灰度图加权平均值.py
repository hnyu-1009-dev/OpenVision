# 在这个文件中，使用加权平均的方法去灰度化一张彩色图
import cv2
import numpy as np

# 使用opencv去读取一张图片，再opencv中使用cv2.imread去读取一张图片 
# cv2,imread():获取两个参数，第一个是尧都区的图片的位置及名称（名称要包括文件的后缀名）
# 第二个参数是指定读取进来的图片的格式，默认使用RGB彩色图的格式
image_np = cv2.imread("../image/huidu.png")
print(type(image_np))

# shape:是ndarray的一个属性，用来查看数组的形状
# shape读取道德形状与图像的实际宽和高是相反的，shape[0]代表的是图像的高度，shape[1]代表的是图像的宽度
image_shape = image_np.shape


# 创建一个单通道的全0数组，此时就需要创建一个与原图大小相同的单通道数组
# zeros:按照高和宽的顺序来创建
# image_gray就是创建的灰度图模板
image_gray = np.zeros((image_shape[0], image_shape[1]), dtype=np.uint8)


# 按照加权平均的方法处理灰度值

# 定义三通道权重
weight_red = 0.299
weight_green = 0.587
weight_blue = 0.114

# 要便利彩色图像，对彩色图像中的每个像素点进行加权平均的操作
# 从而求出来每个像素点的灰度值，然后将得到的灰度值赋值给image_gray

# 通过一个嵌套循环让我们能遍历到图片中的所有像素点
# round函数进行四舍五入
for i in range(image_shape[0]):
    for j in range(image_shape[1]):
        # 遍历到所有的像素点之后，开始进行加权平均的计算
        image_gray[i][j] = round(
            (
                image_np[i, j][0] * weight_blue
                + image_np[i, j][1] * weight_green
                + image_np[i, j][2] * weight_red
            )
        )


# imshow是非阻塞弹窗
# 使用cv2.imshow()显示一下原图像
# 参数1 窗口名称 参数二 图像变量
cv2.imshow("image_np", image_np)

# 使用cv2.imshow()曲线是一下image_gray
cv2.imshow("image_gray", image_gray)

# 使用cv.waitKey(0) 将图像固定下来
cv2.waitKey()
