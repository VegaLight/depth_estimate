# -*- coding: utf-8 -*-
# @Time: 2023/6/2 17:15
# Author: Steve Shaw
# E-mail: stevezmm11@gmail.com

import cv2
import os

image_folder = 'outputs_Pictures'
output_video = 'output.mp4'

# 获取图片文件列表
image_files = sorted(os.listdir(image_folder), key=lambda x: int(''.join(filter(str.isdigit, x))))
print(image_files)

# 读取第一张图像，获得图像的宽度和高度
first_image = cv2.imread(os.path.join(image_folder, image_files[0]))
height, width, _ = first_image.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_video, fourcc, 30.0, (width, height))

# 逐帧写入视频
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = cv2.imread(image_path)
    video.write(image)

video.release()
print("合成视频已保存为:", output_video)
