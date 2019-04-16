import os
import unittest
import pandas as pd
import tempfile
#import pandas.testing as pd_testing
from images_in_features_subdirs import images_in_features_subdirs


class TestImagesInFeaturesSubdirs(unittest.TestCase):
    

    def test_one(self):
        
                        
        """
         Test if images are placed in attributes subdirectories
        """
        
        with tempfile.TemporaryDirectory() as tmpdirname:
            
            #path names
            train_dir = os.path.join(tmpdirname, 'train_dir')
            val_dir  = os.path.join(tmpdirname, 'val_dir')
            images_dir = os.path.join(tmpdirname, 'images_dir')
               
            #create train val images directories    
            os.mkdir(train_dir)    
            os.mkdir(val_dir)
            os.mkdir(images_dir) 
                
            #attributes
            lesion_ids =  ['ab','cd','ab','ef']
            dxs = ['dxA','dxB','dxA','dxC']
            is_val = [False,True,False,True]
            
            
            #for every lesion_id there is one file
            for lesion_id in lesion_ids:
                file = os.path.join(images_dir,lesion_id + '.jpg')
                open(file, 'a').close()
            
            #for every dx there is one directory
            for dx in dxs:
                
                directory = os.path.join(train_dir, dx)
                exists = os.path.isdir(directory)
                
                if not exists:
                    os.mkdir(directory)
                    os.mkdir(os.path.join(val_dir, dx))

            
            #make the data frame
            input_df = pd.DataFrame \
                         .from_dict({ \
                                     'lesion_id': lesion_ids,
                                     'dx': dxs,
                                     'is_val': is_val \
                                    })
         
            expected_train_dxA = set(['ab.jpg','ab.jpg'])
            
            images_in_features_subdirs(input_df,
                                        train_dir = train_dir,
                                        val_dir = val_dir, 
                                        images_dir = images_dir)

            returned_train_dxA = set(os.listdir(os.path.join(train_dir,'dxA')))
                                
            self.assertEqual(expected_train_dxA,returned_train_dxA)
        
if __name__ == '__main__':
    
    unittest.main()
 