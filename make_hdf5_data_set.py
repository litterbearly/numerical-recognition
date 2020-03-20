# 将images中分好类（名称前缀即类别）的字符文件制作成h5数据集，
# 存放到data_set中文件名为data_thresh.h5
import os, random
import h5py
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split

"""
h5py: 2.7.1
PIL 4.3.0 (pip install pillow)
numpy 1.13.1
sklearn: 0.19.1
"""
if not os.path.exists('./data_set'):
    os.mkdir('./data_set')


def make_hdf5_data_set():
    x, y = [], []
    filelist = os.listdir('./images/train/')  # 存放图片的目录
    random.shuffle(filelist)  # 打乱文件顺序
    for image_path in filelist:
        # label转为独热编码后再保存
        label = int(image_path.split('_')[0])
        label_one_hot = [0 if i != label else 1 for i in range(10)]  # 总共10类
        y.append(label_one_hot)

        # 图片像素值映射到 0 - 1之间
        image = Image.open('./images/train/{}'.format(image_path)).convert('L')
        image_arr = 1 - np.reshape(image, 784) / 255.0
        x.append(image_arr)

    with h5py.File('./data_set/data_thresh.h5', 'w') as f:
        f.create_dataset('x_data', data=np.array(x))
        f.create_dataset('y_data', data=np.array(y))


if __name__ == '__main__':
    make_hdf5_data_set()