# dataset

import numpy as np
import os
import cv2


def dataset(data_path):
   
    img_data_array=[]
    class_name=[]


   
    for dir1 in os.listdir(data_path):
        for file in os.listdir(os.path.join(data_path, dir1)):
            image_path= os.path.join(data_path, dir1,  file)
            image= cv2.imread( image_path, cv2.COLOR_BGR2RGB)
            if image is None:
                continue
            image=cv2.resize(image, (64, 64))
            image=np.array(image)
            image = image.astype('float32')
            image /= 255 
            if len(image.shape) < 3:
                continue
            elif dir1 == "meningioma_tumor":
                img_data_array.append(image)
                class_name.append(1)
            elif dir1 =="no_tumor":
                img_data_array.append(image)
                class_name.append(0)

    img_data_array = np.stack(img_data_array, axis=0)
    class_name = np.stack(class_name, axis=0)


    return img_data_array, class_name
