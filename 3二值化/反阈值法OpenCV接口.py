# 使用OTSU去计算合适的阈值并结合阈值法去二值化一张图像，且图像必须是灰度图
import cv2

# 1.使用OpenCV去读取一张图片
image_np = cv2.imread("../image/huidu.png")

# 2. 使用OpenCv的函数去灰度化彩色图
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 对灰度图进行二值化
# 使用阈值法
# 定义所需要的阈值
thresh = 127

# 定义阈值法所需要的最大值，几乎所有的二值化都需要最大值
maxval = 255
# 3.使用OpenCV调用OTSU
# Tips: OTSU在使用时，需要配合其他二值化方法去进行，其模式就是  cv2.THRESH_OTSU + 进行阈值化的方法
# ret存储通过OTSU计算出的阈值
ret, image_thresh = cv2.threshold(
    image_gray,  # 操作图片
    thresh,  # 阈值
    maxval,  # 最大值
    cv2.THRESH_BINARY + cv2.THRESH_OTSU,  # 阈值法
)
print(ret)

# 显示图像
cv2.imshow("image_thresh", image_thresh)
cv2.waitKey()
