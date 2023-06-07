# -*- coding: utf-8 -*-
# @Time: 2023/6/2 17:00
# Author: Steve Shaw
# E-mail: stevezmm11@gmail.com

import os
import glob
import argparse

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from keras.models import load_model
from layers import BilinearUpSampling2D
from utils import predict, load_images, display_images
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser(description='High Quality Monocular Depth Estimation via Transfer Learning')
parser.add_argument('--model', default='nyu.h5', type=str, help='Trained Keras model file.')
parser.add_argument('--input', default='videoToPictures/', type=str, help='Input folder.')
args = parser.parse_args()

custom_objects = {'BilinearUpSampling2D': BilinearUpSampling2D, 'depth_loss_function': None}

print('Loading model...')

model = load_model(args.model, custom_objects=custom_objects, compile=False)

print('\nModel loaded ({0}).'.format(args.model))

image_files = glob.glob(os.path.join(args.input, '*.png'))
print(image_files)

for image_file in image_files:
    input_image = load_images([image_file])

    output_image = predict(model, input_image)

    viz = display_images(output_image.copy(), input_image.copy())
    plt.figure(figsize=(10, 5))
    plt.imshow(viz)
    plt.savefig('outputs_Pictures/' + os.path.basename(image_file))
    plt.show()
