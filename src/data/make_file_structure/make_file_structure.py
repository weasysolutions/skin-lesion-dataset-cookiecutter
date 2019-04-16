
import os
import shutil
import itertools
import sys
import logging


def make_file_structure(abs_path, list_of_lists):
    
    
    """
        Takes the cartesian product of  list_of_lists and makes  recursively directories for every resulting
         combination and starting creation from abs_path
    """
    try:
        
        os.mkdir(abs_path)   
            
    except: 
            
        shutil.rmtree(abs_path)
        os.mkdir(abs_path)
            
    finally:
                
        for element in itertools.product(*list_of_lists):
            
            os.makedirs(os.path.join(abs_path,*element))
        
        logger = logging.getLogger(__name__)
        logger.info('making final data set from raw data')

    
   

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main(sys.argvs[1],sys.argvs[2])
