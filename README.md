先把你想要深度估计的视频命名为original.mp4，然后放到根目录里面
###  **==1.运行step_1:==**

​	将对应的original.mp4的每帧画面保存为图片，保存在videoToPictures文件夹中，图片给他resize成(640，480)

```python
size = (640, 480)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 30, size)

frame_count = 0
while True:
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, size, interpolation=cv2.INTER_CUBIC)
        image_name = os.path.join('videoToPictures/' + str(frame_count) + '.png')

        frame_count = frame_count+1
        cv2.imwrite(image_name, frame)

        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break	
```

### **==2.运行step_2:==**

​	(1)参数设置

```python
parser = argparse.ArgumentParser(description='High Quality Monocular Depth Estimation via Transfer Learning')
parser.add_argument('--model', default='nyu.h5', type=str, help='Trained Keras model file.')
parser.add_argument('--input', default='videoToPictures/', type=str, help='Input folder.')
args = parser.parse_args()
```

​	(2)构建模型

```python
custom_objects = {'BilinearUpSampling2D': BilinearUpSampling2D, 'depth_loss_function': None}
model = load_model(args.model, custom_objects=custom_objects, compile=False)
```

​	(3)获得videoToPictures文件夹中的图片地址

```python
image_files = glob.glob(os.path.join(args.input, '*.png'))
```

​	(4)对每一个图片进行操作并保存，处理后的图片保存在outputs_Pictures文件夹中

```python
for image_file in image_files:
    input_image = load_images([image_file])

    output_image = predict(model, input_image)

    viz = display_images(output_image.copy(), input_image.copy())
    plt.figure(figsize=(10, 5))
    plt.imshow(viz)
    plt.savefig('outputs_Pictures/' + os.path.basename(image_file))
    plt.show()
```

### ==**3.运行step_3：**==

​	将上一步运行生成的图片逐帧写入视频，获得处理完之后的视频—output.video

```python
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    image = cv2.imread(image_path)
    video.write(image)
   
```



------

#### **ps:**

​	nye.h5是模型文件，layers.py跟utils.py包括了一些用到的函数

