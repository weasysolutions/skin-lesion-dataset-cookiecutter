# -*- coding: utf-8 -*-
import click
import os
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from merge_dataset_directories.merge_dataset_directories import merge_dataset_directories
from make_file_structure.make_file_structure import make_file_structure


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
#@click.argument('output_filepath', type=click.Path())
def main(input_filepath):
    
    
    """ 
        Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
            
       
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
                                 [['var_dir','train_dir'],\
                                   ['nv', 'mel', 'bkl', 'bcc', 'akiec', 'vasc', 'df']]
                        )
    


    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')


if __name__ == '__main__':
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
