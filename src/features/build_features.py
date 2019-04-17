# -*- coding: utf-8 -*-
import click
import os
import logging
import sys
import pandas as pd

import os, sys, inspect

cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"images_in_features_subdirs")))
if cmd_subfolder not in sys.path:
     sys.path.append(cmd_subfolder)
        
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"non_duplicate_lesion_id")))
if cmd_subfolder not in sys.path:
     sys.path.append(cmd_subfolder)
        
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"training_and_validation_sets")))
if cmd_subfolder not in sys.path:
     sys.path.append(cmd_subfolder)
                                

from images_in_features_subdirs import images_in_features_subdirs 
from non_duplicate_lesion_id import non_duplicate_lesion_id
from training_and_validation_sets import training_and_validation_sets


def build_features(**kwargs):
    
    
    metadata_csv = kwargs['metadata_csv']
    train_dir = kwargs['train_dir']
    images_dir = kwargs['images_dir']
    val_dir = kwargs['val_dir']
    
        
    """ 
     Takes data in ../data/interim. Splits training and validation data.
     Stores splitted sets in ../data/processed/base_dir/train_dir 
     and ../data/processed/base_dir/val_dir
    """
    #load meta-data-set
    df = pd.read_csv(metadata_csv)
    
    #Create non_duplicate column. 
    # Make a new df with unique_ids
   
    df, df_unique_id  = non_duplicate_lesion_id(df)
    
    #split in training and validation dataframes
    df, df_train, df_val = training_and_validation_sets(df,df_unique_id)
    
    #place images in named attributes directories 
    
    images_in_features_subdirs(df,
                                images_dir = images_dir, 
                                train_dir = train_dir,
                                val_dir = val_dir \
                              )
    
     
    logger = logging.getLogger(__name__)
    logger.info('Features added. Data is ready for modelling.')

    
if __name__ == '__main__':
    
    import json 
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    data=json.loads(argv[1])

    build_features(data)