import os
import logging
import shutil


def merge_dataset_directories(**kwargs):
    
    directories = kwargs['directories']
    destination = kwargs['final_dir']
    
    images = [os.path.join(directory,file) for directory in directories for file in os.listdir(directory)]
    #print('copying images..')
    #print(images)
        
    for image in images:
        shutil.copy(image, destination)  
    
        
if __name__ == '__main__':
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    #main(**sys.argvs[1],sys.argvs[2])        


    