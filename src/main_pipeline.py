
import logging 

import sys
import os

from data.make_dataset import make_dataset
from features.build_features import build_features      


        
def main_pipeline():

    print('starts dataset making...')
    #make_dataset(input_filepath = '../data')
    
    dirname = os.path.join(os.path.dirname( __file__ ),'..','data')
    
    metadata_csv = os.path.abspath(os.path.join(dirname, 'raw/HAM10000_metadata.csv'))
    images_dir = os.path.abspath(os.path.join(dirname, 'interim'))
    train_dir = os.path.abspath(os.path.join(dirname, 'processed', 'base_dir','train_dir'))
    val_dir = os.path.abspath(os.path.join(dirname,'processed','base_dir','val_dir'))
    
    print('starts building features...')
    build_features(metadata_csv = metadata_csv,
                        images_dir = images_dir, 
                        train_dir = train_dir,
                        val_dir = val_dir \
                    )
    
    logger = logging.getLogger(__name__)
    logger.info('Project completed')

if __name__ == '__main__':
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
   
    main_pipeline()