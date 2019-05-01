import os

def count_files(**kwargs):
    
    """ 
       Counts the number of files and folders in a given directory 
    """
    
    directory = kwargs['directory']
       
    return len(os.listdir(directory))
    
if __name__ == '__main__':

    import sys
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    class_weights(sys.argv[1])
    
    