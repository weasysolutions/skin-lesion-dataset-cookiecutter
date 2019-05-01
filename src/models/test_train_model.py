import unittest
import tempfile
import os, sys, shutil 
import random

from pathlib import Path

from train_model import train_model 

sys.path.append('../data/make_file_structure') 
from make_file_structure import make_file_structure


class TestTrainModel(unittest.TestCase):
    
    """
       Test Train Model 
    """
    
    def test_train_model_1(self):
        
        """        
          Sample           
        """

        def get_sample_files(path,nof_samples):
            
            pathlist = Path(path).glob("*")
            
            rc = []
            for k, path in enumerate(pathlist):
 
                if k < nof_samples:
                    rc.append(str(path)) # because path is object not string
            
                else:
                    i = random.randint(0, k)
                    if i < nof_samples:
                        rc[i] = str(path)
                 
            return rc
        
        def copy_files(files, destination_directory):
            
            for file in files:
                if os.path.isfile(file):
                    shutil.copy(file, destination_directory)
                else:
                    print('file does not exist', name)

                            
        
        with tempfile.TemporaryDirectory() as tmpdir:
               
            list_of_attributes = ['nv', 'mel', 'bkl', 'bcc', 'akiec', 'vasc', 'df']
            
            make_file_structure(tmpdir+'/base_dir',\
                                 [['val_dir','train_dir'],\
                                   list_of_attributes]
                        )
            
            
            for directory_name in ('train_dir','val_dir'):
                
                source_parent_dir = os.path.join('../../data/processed/base_dir',directory_name)
                destination_parent_dir = os.path.join(tmpdir,'base_dir',directory_name)     
            
                for attribute in list_of_attributes:

                    source_dir = os.path.join(source_parent_dir,attribute)
                    destination_dir = os.path.join(destination_parent_dir,attribute)                

                    #sample one tenth of total
                    filenames = os.listdir(source_dir)
                    nof_files = len(filenames)
                    nof_samples = 1 if nof_files < 50 else ( nof_files // 50 )

                    sample_files =  get_sample_files(source_dir,nof_samples)
                    copy_files(sample_files,destination_dir)
                    
                    print(destination_dir)
                    print(os.listdir(destination_dir))
            
            #mini batches
            
            train_batch_size = 10
            val_batch_size = 2

            #model results path
            file_path = tmpdir  + 'model.h5'            
            train_model(train_path = os.path.join(tmpdir,'base_dir','train_dir'), 
                       valid_path = os.path.join(tmpdir,'base_dir','valid_dir'),
                       file_path  = file_path,
                       val_batch_size = val_batch_size,
                       train_batch_size = train_batch_size \
                       ) 

             
        self.assertEqual(True,False)
        
if __name__ == '__main__':
    
    unittest.main()
    
    
    