# -*- coding: utf-8 -*-
import click
import os
import logging
import sys
import pandas as pd
from images_in_features_subdirs.images_in_features_subdirs import images_in_features_subdirs 
from non_duplicate_lesion_id.non_duplicate_lesion_id import non_duplicate_lesion_id
from training_and_validation_sets.training_and_validation_sets import training_and_validation_sets

#@click.command()
#@click.argument('input_metadata_file', type=click.Path(exists=True))
#@click.argument('images_dir', type=click.Path(exists=True))
#@click.argument('train_dir', type=click.Path(exists=True))
#@click.argument('val_dir', type=click.Path(exists=True))
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
     
    # '../data/raw/HAM10000_metadata.csv'   
    #'../data/processed/base_dir/val_dir'
    #'../data/interim'
    #'../data/processed/base_dir/train_dir '
    
if __name__ == '__main__':
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)


    build_features(sys.argv[1],sys.argv[2],sys.argv[3])