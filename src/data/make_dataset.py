# -*- coding: utf-8 -*-
#import click
import os
import logging

import os, sys, inspect

 # Use this if you want to include modules from a subfolder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"make_file_structure")))
if cmd_subfolder not in sys.path:
     sys.path.append(cmd_subfolder)
        
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"merge_dataset_directories")))
if cmd_subfolder not in sys.path:
     sys.path.append(cmd_subfolder)        

from merge_dataset_directories import merge_dataset_directories
from make_file_structure import make_file_structure

def make_dataset(**kwargs):
    
    
    """ 
        Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """

    input_filepath = kwargs['input_filepath'] 
                  
    #put images in the same directory 
    merged_dir = os.path.join(input_filepath,'interim/')
    dir1 =  os.path.join(input_filepath,'raw/HAM10000_images_part_1')
    dir2 =  os.path.join(input_filepath,'raw/HAM10000_images_part_2')
    
    merge_dataset_directories( final_dir = merged_dir,\
                                directories = [dir1,dir2]
                              )
            
        #Create directory structure for modelling: base_dir/element
        #element= var_dir/nv,...train_dir/df
    make_file_structure(input_filepath+'/processed/base_dir',\
                                 [['val_dir','train_dir'],\
                                   ['nv', 'mel', 'bkl', 'bcc', 'akiec', 'vasc', 'df']]
                        )
    
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    #project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    #load_dotenv(find_dotenv())

    make_dataset(sys.argv[1])
