# -*- coding: utf-8 -*-
import os
import pandas as pd

def non_duplicate_lesion_id(dataframe):
    
    """ 
        Creates boolean 'non_duplicate' column in dataframe: True if lesion_id is unique.
        Returns dataframe and its version with no duplicates
    """
    
    
    #returns true if lesion_id is unique
    def is_unique_lesion(image):
        
        # count images related to lesion_id
        lesion_counts = dataframe['lesion_id']\
                        .value_counts()
        
        return lesion_counts[image['lesion_id']] == 1
    
    
    #create non_duplicate feature 
    dataframe['non_duplicate'] = dataframe \
                                  .apply(is_unique_lesion , axis = 1) \
                                   .values
    
    non_duplicate_df = dataframe[dataframe['non_duplicate']].reset_index(drop = True)
    
    
    return dataframe, non_duplicate_df
    
       
if __name__ == '__main__':
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    create_non_duplicate_feature(sys.argvs[1])

    #main(**sys.argvs[1],sys.argvs[2])        
    