import unittest
import tempfile
import os, sys, shutil 
#import random

#from pathlib import Path

from gen_steps import gen_steps

sys.path.append('../../data/make_file_structure') 
from make_file_structure import make_file_structure


class TestGenSteps(unittest.TestCase):
    
    """
       Test generation of epoch and validation steps
    """
    
    def test_gen_steps_1(self):
        
        """        
            steps_per_epoch and validation_steps are equal to 10 and 1, respectively.
        """

        with tempfile.TemporaryDirectory() as tmpdir:
            
            make_file_structure(tmpdir+'/base_dir',
                                 [['val_dir','train_dir']] \
                                 )
            dirs = {}
            dirs['val'] = os.path.join(tmpdir,'base_dir','val_dir')
            dirs['train'] =  os.path.join(tmpdir,'base_dir','train_dir')      
            
            nof_samples = {}
            nof_samples['train'] = range(100)
            nof_samples['val'] = range(10)
            
            for train_val in ('train','val'):
                
                files = [ os.path.join(dirs[train_val], str(i) + '_tmp.txt') for i in nof_samples[train_val] ]
                #print(files)
                
                for file in files:
                    f = open(file,'w+')
                    f.close()
                
            steps_per_epoch, validation_steps =  gen_steps(
                                                    train_dir = dirs['train'],
                                                    val_dir = dirs['val'],
                                                    val_batch_size = 10,
                                                    train_batch_size = 10 \
                                                     )
                        
            print(steps_per_epoch, validation_steps)
            #steps_per_epoch and validation_steps
                       
        self.assertEqual(steps_per_epoch,10)
        self.assertEqual(validation_steps,1)
        
if __name__ == '__main__':
    
    unittest.main()
    
    