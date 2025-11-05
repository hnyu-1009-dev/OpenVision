# 使用numpy库来来创建数组
import numpy as np

# 使用OpenCV库查看图像及其他操作
import cv2

# 使用matplotlib库来一次性展示多个图像
import matplotlib.pyplot as plt

# 创建一个700*700 的三位数组
# 使用np.zero 创建一数值全为0的数组，对应一张黑色图
# dtype=np.uint8：设置数据类型为  unsigned int 无符号整数 0-255
image = np.zeros((700, 700, 3), dtype=np.uint8)
# 用来代表分割出来的矩形大小
block_size = 100


# 使用一个嵌套循环对褐色图像进行分割
# 使用i来代表每一行
for i in range(0, 700, block_size):
    # 使用j来代表每一列
    for j in range(0, 700, block_size):
        # # i 的取值 ：0，100，200，300，400，500，600
        # # j 的取值 ：0，100，200，300，400，500，600
        # # 使用三位数组切片修改的方式去修改像素值
        # image[i, :, :] = (255, 255, 255)
        # image[:, j, :] = (255, 255, 255)
        # if (
        #     i != 0
        #     and j != 0
        #     and i != 600
        #     and j != 600
        #     and ((i == j) or (i + j) == 600)  # 502
        # ):  # 502
        #     # 在OpenCV中，颜色的顺序是BGR
        #     image[i : i + block_size, j : j + block_size, :] = (0, 0, 255)

        # OpenCV中，以右为x轴正方向，以下为y正方向
        # 对应到我们的程序中，以j为x轴坐标，以i为y轴坐标
        top_left = (j, i)
        bottom_right = (j + block_size - 1, i + block_size - 1)
        # 如果满足条件，就是用cv2.rectangle()来画红色的实心矩阵
        if i != 0 and i != 600 and (i == j or i + j == 600):
            cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), -1)
        # 如果不满足条件，就需要画白线
        else:
            cv2.rectangle(image, top_left, bottom_right, (255, 255, 255), 1)

# matplotlib的颜色顺序是RGB，所以需要进行BGR到RGB的转换
# 在image_rgb 里存放的是RGB顺序的图像，在image里存放的是BGR顺序的图像
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


plt.subplot(232)
# imshow是用来展示图像的
plt.imshow(image_rgb)

# title是用来给图像添加标签
plt.title("Original Image")

# # 不显示坐标轴
# plt.axis("off")

# 获取原图中的三通道的像素值
# 有两种方法
# 第一种使用数组切片的方式去获取
b = image[:, :, 0]
g = image[:, :, 1]
r = image[:, :, 2]
# 第二种方法，使用cv2.split()来进行分割
# b, g, r = cv2.split()


# 创建新的图像，用来展示三通道图
blue_channel = np.zeros((700, 700, 3), dtype=np.uint8)
green_channel = np.zeros((700, 700, 3), dtype=np.uint8)
red_channel = np.zeros((700, 700, 3), dtype=np.uint8)
# 将获取到的原图像的
blue_channel[:, :, 0] = b
green_channel[:, :, 1] = g
red_channel[:, :, 2] = r

# 将BGR转换为RGB
blue_channel_rgb = cv2.cvtColor(blue_channel, cv2.COLOR_BGR2RGB)
green_channel_rgb = cv2.cvtColor(green_channel, cv2.COLOR_BGR2RGB)
red_channel_rgb = cv2.cvtColor(red_channel, cv2.COLOR_BGR2RGB)


# plt.subplot()用来对将要展示的图像进行布局
plt.subplot(234)
plt.imshow(blue_channel_rgb)
# 设置标签
plt.title("Blue Channel")
# 设置坐标轴
plt.axis("off")

plt.subplot(235)
plt.imshow(green_channel_rgb)
# 设置标签
plt.title("Green Channel")
# 设置坐标轴
plt.axis("off")

plt.subplot(236)
plt.imshow(red_channel_rgb)
# 设置标签
plt.title("Red Channel")
# 设置坐标轴
plt.axis("off")

# 合理布局
plt.tight_layout()
plt.show()

# # 注意： 窗口的名字尽量不要崇明，否则后面的图像会把前面的图像给覆盖掉
# cv2.imshow("image", image)


# # 等待键盘输入，关闭图片, 也可以传入等待的参数作为等待时间，
# # 如果输入，返回值是输入字符的ASCII码
# temp = cv2.waitKey()
# print(temp)
