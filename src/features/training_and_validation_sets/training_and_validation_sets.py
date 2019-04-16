# -*- coding: utf-8 -*-
import os
import pandas as pd

from sklearn.model_selection import train_test_split

def training_and_validation_sets(df_complete,df_unique_id):
    
    """ 
        From unique_id selects the validation set. From the rest, selects the training set.
        Returns validation and training dataframes
    """
    
    #percentage of unique_id cases 
    test_size =0.17
        
    _, df_val = train_test_split(df_unique_id, 
                                  test_size = test_size, 
                                  random_state = 101, 
                                  stratify = df_unique_id['dx'] )
    
    df_complete['is_val'] = df_complete \
                            .apply(lambda image: image.name in df_val.index, axis = 1) \
                            .values
    
    df_train = df_complete[~(df_complete['is_val'])]
    df_val = df_complete[df_complete['is_val']]

    
    return df_complete, df_train, df_val
    
       
if __name__ == '__main__':
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    create_non_duplicate_feature(sys.argvs[1])

    #main(**sys.argvs[1],sys.argvs[2])        
    