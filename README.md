# The images and .json annotation folder is divided into train and val subfolders for labelme2coco.
Before, the image and the corresponding annotation files were in one folder, but later they were divided into train and val folders. 
The images and json annotation folders are divided into train and val subfolders for labelme2coco. The usage method is described in the file.

This file  automatically divides the train, val directory according to
the provided image file path( images and jsons).

Command:
```
conda activate labelme
python img2coco_train_val.py 
--img_dir realsense/priority_test3_coco/ 
--val_size 0.1
```

Then using the labelme tool, you can complete the generation of labelme annotation json to coco annotation file.  

Command to get coco annotation file: path/to/labelme/dir should includs img and json
Advanced Usage see https://github.com/fcakyon/labelme2coco 
Notice: in this labelme2coco code, you can modify category_ind value(in labelme2coco.py) from 0 to 1. So that object labels start at 1 instead of 0. 0 means the object background. And you can do not, that object labels start at 0.

To use this tool:
```
conda activate labelme
labelme2coco path/to/labelme/dir
```

Instead of this labelme2coco tool, you also can use another code to operate labelme2coco.
It is recommended to use this. You can modify the pathname or filename.
Installation and usage see:https://github.com/wkentaro/labelme 

Finally modify the folder name to [reconstruct the structure](https://github.com/facebookresearch/detectron2/blob/main/datasets/README.md).
