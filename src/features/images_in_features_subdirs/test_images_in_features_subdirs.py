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
            images_id = ['image' + str(n)  for n in range(len(lesion_ids))]

            
            
            #for every lesion_id there is one file
            for image_id in images_id:
                file = os.path.join(images_dir,image_id + '.jpg')
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
                                     'is_val': is_val,
                                     'image_id': images_id \
                                    })
         
            expected_train_dxA = set(['image0.jpg','image2.jpg'])
            
            images_in_features_subdirs(input_df,
                                        train_dir = train_dir,
                                        val_dir = val_dir, 
                                        images_dir = images_dir)

            returned_train_dxA = set(os.listdir(os.path.join(train_dir,'dxA')))
                                
            self.assertEqual(returned_train_dxA.issubset(expected_train_dxA),True)
        
if __name__ == '__main__':
    
    unittest.main()
 