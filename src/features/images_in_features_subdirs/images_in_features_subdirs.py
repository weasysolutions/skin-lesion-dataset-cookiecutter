# -*- coding: utf-8 -*-
import os
import pandas as pd
import shutil 

from sklearn.model_selection import train_test_split

def images_in_features_subdirs(df_data,**kwargs):
    

    """ 
       Copy images to attribures directories in the corresponding training and validation directoires
    """
    
    train_dir = kwargs['train_dir']
    val_dir = kwargs['val_dir']
    images_dir = kwargs['images_dir']
    
    for index in df_data.index:

        image = df_data.iloc[index]
        directory =  val_dir if image.is_val else train_dir

        source = os.path.join(images_dir, image.image_id + '.jpg')
        destination = os.path.join(directory, image.dx, image.image_id+ '.jpg')
                
        shutil.copyfile(source,destination)        
       

if __name__ == '__main__':
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    create_non_duplicate_feature(sys.argvs[1])

    #main(**sys.argvs[1],sys.argvs[2])        
    