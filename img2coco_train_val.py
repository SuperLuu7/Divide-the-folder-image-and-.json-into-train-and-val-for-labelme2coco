'''
Created on Apr 21, 2023

@author: LULU LI

Divide the image train and val folders:
This file  automatically divides the train, val directory according to
the provided image file path( images and jsons).

#Command:
$conda activate labelme
$python img2coco_train_val.py --img_dir realsense/priority_test3_coco/ --val_size 0.1

Then using the labelme official tool, you can complete the generation
of labelme annotation json to coco annotation file.  

# Command to get coco annotation file: path/to/labelme/dir should includs img and json
# Advanced Usage see https://github.com/fcakyon/labelme2coco 
### Notice: in this labelme2coco code, you can modify category_ind value(in labelme2coco.py)
 from 0 to 1. So that object labels start at 1 instead of 0. 0 means the object background.
 And you can do not that object labels start at 0.
To use this tool:
$conda activate labelme
$labelme2coco path/to/labelme/dir

Instead of this labelme2coco code, you also can use another code to operate labelme2coco.
It is recommended to use this, you can modify the pathname filename to succeed.
Installation and usage see:https://github.com/wkentaro/labelme 
Finally modify the folder name to reconstruct the structure.
'''
import os
import sys
import argparse
import shutil
import random
from collections import OrderedDict

from sklearn.model_selection import train_test_split
from labelme import utils


class img2coco_train_val():

    def make_dir(self, source):
        '''
        创建和源文件相似的文件路径函数
        :param source: 源文件位置
        :param target: 目标文件位置
        '''
        for i in ['train2017', 'val2017', 'test2017']:
            path = source + i + '/'
            if not os.path.exists(path):
                os.makedirs(path)

    def divideTrainValiTest(self, source, val_size):
        '''
            创建和源文件相似的文件路径
            :param source: 源文件位置
            :param target: 目标文件位置
        '''
        # 得到源文件下的种类
        img_names = os.listdir(source)
        img_path_names=[]
        # 对于每一类里的数据进行操作
        for classes in img_names:
            if os.path.splitext(classes)[-1] in ['.png', '.jpg', '.JPG']:#classes == '*.png' or classes == '*.jpg':
                # only keep img tpye得到这一种类的图片的名字
                #print(os.path.splitext(classes)[-1])
                img_path_name = os.path.join(os.getcwd(), source, classes)
                img_path_names.append(str(img_path_name))
        #img_names_list = os.listdir(pic_classed_names)
        img_names_list = img_path_names
        random.shuffle(img_names_list)
        # 按照8：1：1比例划分
        train_list = img_names_list[0:int((1-2*val_size) * len(img_names_list))]
        valid_list = img_names_list[int((1-2*val_size) * len(img_names_list)):int((1-val_size) * len(img_names_list))]
        test_list = img_names_list[int((1-val_size) * len(img_names_list)):]
        # 对于每个图片，移入到对应的文件夹里面
        for train_pic in train_list:
            shutil.copyfile(train_pic, os.getcwd() + '/' + source + 'train2017' + '/' + os.path.basename(train_pic))
            # 分离文件名和扩展名
            file_name, ext = os.path.splitext(train_pic)
            # 更改扩展名
            new_ext = '.json'
            # 拼接回去
            new_path = file_name + new_ext
            # Copy the json file with the same name, or other suffix files to the coco directory
            shutil.copyfile(new_path, os.getcwd() + '/' + source + 'train2017' + '/' + os.path.basename(new_path))

        for validation_pic in valid_list:
            shutil.copyfile(validation_pic, os.getcwd() + '/' + source + 'val2017' + '/' + os.path.basename(validation_pic))
            file_name, ext = os.path.splitext(validation_pic)
            new_ext = '.json'
            new_path = file_name + new_ext
            shutil.copyfile(new_path, os.getcwd() + '/' + source + 'val2017' + '/' + os.path.basename(new_path))

        for test_pic in test_list:
            shutil.copyfile(test_pic, os.getcwd() + '/' + source + 'test2017' + '/' + os.path.basename(test_pic))
            file_name, ext = os.path.splitext(test_pic)
            new_ext = '.json'
            new_path = file_name + new_ext
            shutil.copyfile(new_path, os.getcwd() + '/' + source + 'test2017' + '/' + os.path.basename(new_path))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_dir',type=str,
                        help='Please input the path of the image files.')
    parser.add_argument('--val_size',type=float, nargs='?', default=None,
                        help='Please input the validation dataset size, for example 0.1 for val')

    args = parser.parse_args(sys.argv[1:])
    
    #operation function
    op = img2coco_train_val()
    op.make_dir(source = args.img_dir)
    op.divideTrainValiTest(args.img_dir, args.val_size)

"""
#Command:
conda activate labelme
python img2coco_train_val.py --img_dir realsense/priority_test3_coco/ --val_size 0.1
"""
    
