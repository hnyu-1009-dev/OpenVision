# OpenVision

一个以 `OpenCV + NumPy + Matplotlib + Jupyter Notebook` 为核心的图像处理学习仓库。项目内容按主题拆分为独立章节，覆盖图像基础表示、灰度化、二值化、形态学、颜色处理、几何变换、轮廓分析、滤波去噪、梯度/边缘检测、模板匹配、霍夫变换等常见入门知识点。

仓库当前更接近“学习笔记 + 可运行示例集”，而不是封装好的 Python 包。适合以下场景：

- 系统学习 OpenCV 常见 API 和图像处理基础概念
- 边看 Notebook 边修改参数，观察不同处理效果
- 作为课程作业、练习项目或自学路线的参考仓库

## 项目概览

- 23 个 `ipynb` Notebook
- 12 个 `.py` 脚本示例
- 1 个统一的示例图片目录 `image/`
- 章节编号覆盖 `1-11`、`15-24`，`12-14` 目前未包含在仓库中

从仓库内容看，主要学习栈如下：

- `opencv-python`
- `numpy`
- `matplotlib`
- `jupyter notebook` / `jupyter lab`

## 你能学到什么

- 图像在计算机中的表示方式、通道拆分与颜色空间转换
- 灰度化、固定阈值、自适应阈值、OTSU 二值化
- 腐蚀、膨胀、开闭运算、礼帽/黑帽等形态学操作
- ROI 切割、缩放、旋转、镜像、仿射变换、透视变换
- Canny、Sobel、Scharr、Laplacian 等边缘与梯度算法
- 轮廓查找、凸包、外接矩形、最小外接圆等几何特征提取
- 模板匹配、霍夫直线/圆检测、直方图均衡化、亮度变换

## 仓库结构

```text
OpenVision/
├─1计算机眼中的图像/
├─2灰度图/
├─3二值化/
├─4自适应二值化/
├─5形态学变换/
├─6图片颜色识别/
├─7图片颜色替换/
├─8ROI切割/
├─9图像缩放/
├─10图像旋转/
├─11图像镜像旋转/
├─15图像边缘检测/
├─16图像矫正/
├─16绘制图像轮廓/
├─17凸包检测/
├─17图像添加水印/
├─18图像噪点消除/
├─19图像梯度处理/
├─20图像轮廓特征查找/
├─21直方图均衡化/
├─22模板匹配/
├─23霍夫变换/
├─24图像亮度变换/
├─image/
├─图像变换与矩阵.ipynb
└─README.md
```

## 环境准备

建议使用 Python `3.9+`。如果你只是想运行仓库中的示例，下面这组依赖已经足够：

```bash
pip install opencv-python numpy matplotlib jupyter
```

如果你希望隔离环境，推荐：

```bash
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install opencv-python numpy matplotlib jupyter
```

## 运行方式

### 1. 运行 Notebook

在仓库根目录启动：

```bash
jupyter lab
```

或：

```bash
jupyter notebook
```

然后按目录打开对应的 `ipynb` 文件即可。

### 2. 运行 Python 脚本

部分章节同时提供了 `.py` 脚本版本，可直接执行，例如：

```bash
python "2灰度图/使用OpenCV.py"
python "3二值化/二值化OpenCV.py"
python "4自适应二值化/自适应二值化.py"
```

### 3. 关于图片路径

仓库中的大多数 Notebook 和脚本使用相对路径读取图片，例如：

```python
cv2.imread("../image/image.jpg")
```

这意味着运行时的工作目录需要与文件所在目录匹配，或者你需要手动调整路径。最稳妥的方式是：

- 在 VS Code / Jupyter 中直接打开对应目录下的 Notebook
- 保持示例图片目录 `image/` 不变
- 如果读取失败，优先检查当前工作目录和相对路径是否一致

## 章节导览

下表按照仓库当前内容整理，便于快速定位每章的主题、文件和核心知识点。

| 章节 | 主要文件 | 核心内容 | 典型 API / 方法 |
| --- | --- | --- | --- |
| 理论补充 | `图像变换与矩阵.ipynb` | 仿射变换、透视变换、旋转矩阵之间的数学关系总结 | `getAffineTransform` `getPerspectiveTransform` `getRotationMatrix2D` `warpAffine` `warpPerspective` |
| 1 计算机眼中的图像 | `1计算机眼中的图像/计算机眼中的图像.ipynb` `1计算机眼中的图像/计算机眼中的图像.py` | 认识图像矩阵、BGR/RGB、通道拆分、绘制基础图形 | `split` `cvtColor` `rectangle` |
| 2 灰度图 | `2灰度图/*.py` | 灰度图生成方式，对比 OpenCV 转灰度与手工算法 | `cvtColor` |
| 3 二值化 | `3二值化/*.py` | 固定阈值、反阈值、截断阈值、OTSU 手写实现 | `threshold` `THRESH_BINARY` `THRESH_TRUNC` `THRESH_OTSU` |
| 4 自适应二值化 | `4自适应二值化/自适应二值化.py` | 局部区域阈值、自适应阈值处理 | `adaptiveThreshold` |
| 5 形态学变换 | `5形态学变换/形态学变换.ipynb` `5形态学变换/开运算和闭运算.ipynb` | 腐蚀、膨胀、开运算、闭运算、结构元素 | `erode` `dilate` `morphologyEx` `getStructuringElement` |
| 6 图片颜色识别 | `6图片颜色识别/图片颜色识别.ipynb` | RGB 与 HSV 的关系、颜色区间筛选 | `cvtColor` `inRange` |
| 7 图片颜色替换 | `7图片颜色替换/图片颜色替换.ipynb` `7图片颜色替换/礼帽与黑帽.ipynb` | 颜色替换、掩膜融合、礼帽/黑帽形态学操作 | `bitwise_or` `morphologyEx` `MORPH_TOPHAT` `MORPH_BLACKHAT` |
| 8 ROI 切割 | `8ROI切割/ROI切割.ipynb` | 利用 NumPy 切片做局部区域提取 | NumPy slicing |
| 9 图像缩放 | `9图像缩放/图像缩放.ipynb` | 不同插值方法的缩放效果对比 | `resize` `INTER_NEAREST` `INTER_LINEAR` `INTER_CUBIC` `INTER_AREA` |
| 10 图像旋转 | `10图像旋转/图像旋转.ipynb` | 图像旋转、仿射变换、边界填充模式 | `getRotationMatrix2D` `warpAffine` |
| 11 图像镜像旋转 | `11图像镜像旋转/图像镜像旋转.ipynb` | 水平/垂直/双向翻转 | `flip` |
| 15 图像边缘检测 | `15图像边缘检测/图像边缘检测.ipynb` | 灰度化、平滑、阈值化、Canny 边缘检测 | `GaussianBlur` `threshold` `Canny` |
| 16 图像矫正 | `16图像矫正/(透视变换)图像矫正.ipynb` | 透视变换、四点定位、文档/平面校正 | `getPerspectiveTransform` `warpPerspective` |
| 16 绘制图像轮廓 | `16绘制图像轮廓/绘制图像轮廓.ipynb` | 不同轮廓检索模式与绘制方式 | `findContours` `drawContours` |
| 17 凸包检测 | `17凸包检测/凸包检测.ipynb` | 轮廓凸包、是否为凸轮廓、外接矩形 | `convexHull` `isContourConvex` `boundingRect` |
| 17 图像添加水印 | `17图像添加水印/图像添加水印.ipynb` | 基于阈值掩膜的 Logo/水印叠加 | `threshold` `bitwise_and` `add` |
| 18 图像噪点消除 | `18图像噪点消除/滤波.ipynb` | 均值滤波、方框滤波、高斯滤波、中值滤波、双边滤波、非局部均值去噪 | `blur` `boxFilter` `GaussianBlur` `medianBlur` `bilateralFilter` `fastNlMeansDenoising` |
| 19 图像梯度处理 | `19图像梯度处理/图像梯度处理.ipynb` | Sobel、Scharr、Laplacian 梯度与边缘增强 | `Sobel` `Scharr` `Laplacian` `convertScaleAbs` |
| 20 图像轮廓特征查找 | `20图像轮廓特征查找/图像轮廓特征查找.ipynb` | 外接矩形、最小外接矩形、最小外接圆等轮廓几何特征 | `boundingRect` `boxPoints` `circle` |
| 21 直方图均衡化 | `21直方图均衡化/直方图均衡化.ipynb` | 灰度直方图、全局均衡化、CLAHE | `calcHist` `equalizeHist` `createCLAHE` |
| 22 模板匹配 | `22模板匹配/模板匹配.ipynb` | 多种模板匹配策略对比与定位 | `matchTemplate` `rectangle` |
| 23 霍夫变换 | `23霍夫变换/霍夫变换.ipynb` | 普通霍夫直线、概率霍夫直线、霍夫圆检测 | `HoughLines` `HoughLinesP` `HoughCircles` |
| 24 图像亮度变换 | `24图像亮度变换/图像亮度变换.ipynb` | 亮度增强、像素级变换、图像保存 | `imwrite` |

## 示例资源说明

`image/` 目录集中存放了大部分案例图片。按主题大致可以分为：

- 基础读图与颜色处理：`image.jpg` `huidu.png` `four_color.png`
- 几何变换与 ROI：`OpenCVaxis.png` `jiaozheng.png`
- 轮廓与凸包：`work4.png` `31.png`
- 直方图与亮度：`statue.png`
- 模板匹配与水印：`jinbi.png` `maliao.png`
- 边缘、霍夫、梯度：`road.png` `huofu.png` `my_shudu.jpg`
- 噪声与滤波：`color_noise.png`

如果你想扩展自己的实验，最简单的做法是直接替换这些图片，或在对应 Notebook 中修改 `cv2.imread(...)` 的路径。

## 适合的学习顺序

如果你是第一次系统接触 OpenCV，建议按下面的顺序阅读：

1. `1计算机眼中的图像` -> `2灰度图` -> `3二值化` -> `4自适应二值化`
2. `5形态学变换` -> `6图片颜色识别` -> `7图片颜色替换`
3. `8ROI切割` -> `9图像缩放` -> `10图像旋转` -> `11图像镜像旋转`
4. `15图像边缘检测` -> `18图像噪点消除` -> `19图像梯度处理`
5. `16绘制图像轮廓` -> `17凸包检测` -> `20图像轮廓特征查找`
6. `16图像矫正` -> `21直方图均衡化` -> `22模板匹配` -> `23霍夫变换` -> `24图像亮度变换`

## 已知事项

- `21直方图均衡化/直方图均衡化.ipynb` 中引用了 `../image/dark.jpg`，但仓库当前未找到该图片；如果运行报错，需要自行补充图片或修改路径。
- `24图像亮度变换/图像亮度变换.ipynb` 中使用了当前目录下的 `image.jpg`，该文件目前不在仓库中；建议改成读取 `../image/image.jpg` 或放入同名文件。
- 多数示例使用 `cv2.imshow()` 打开窗口，因此需要本地具备图形界面；在纯远程/无 GUI 环境中可能无法直接显示。
- 部分章节既有 Notebook 又有脚本实现，Notebook 更适合学习过程，脚本更适合快速运行验证。

## 后续可改进方向

- 补充 `requirements.txt` 或 `environment.yml`
- 为每个章节增加“输入图 / 输出图 / 关键参数”的说明
- 统一所有 Notebook 的图片路径与命名方式
- 增加 `12-14` 章节，补齐学习路线
- 将常用函数沉淀为可复用脚本或工具模块

## 说明

这个仓库的核心价值在于“按知识点拆开的可运行示例”。如果你正在学习 OpenCV，建议不要只看结果图，最好同时做三件事：

- 修改阈值、卷积核、插值方法、边界模式等参数
- 对同一张图尝试不同算法，观察输出差异
- 把 Notebook 中的示例整理成自己的函数库或实验报告

这样这个仓库才会从“看过”真正变成“会用”。
