import os
import unittest
import pandas as pd
import tempfile
#import pandas.testing as pd_testing
from build_features import build_features


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
            lesion_ids =  ['a','a','a','b','c','d']
            dxs = ['dx1','dx1','dx1','dx2','dx2','dx2']
            image_id = ['image' +  str(n) for n in list(range(len(lesion_ids)))]
            
                        
            #make the data frame
            input_df = pd.DataFrame \
                         .from_dict({ \
                                     'lesion_id': lesion_ids,
                                     'image_id': image_id,
                                     'dx': dxs \
                                    })
           
            metadata_csv = os.path.join(tmpdirname, 'input_metadata.csv')
            
            input_df.to_csv(metadata_csv)
                                                
            for image in set(image_id):
                file = os.path.join(images_dir,image + '.jpg')             
                open(file, 'a').close()
            
            print('images_dir',os.listdir(images_dir))
             
            
            #for every dx there is one directory
            for dx in dxs:
                
                directory = os.path.join(train_dir, dx)
                exists = os.path.isdir(directory)
                
                if not exists:
                    os.mkdir(directory)
                    os.mkdir(os.path.join(val_dir, dx))
                    
                        
            build_features(metadata_csv = metadata_csv,
                                images_dir = images_dir, 
                                train_dir = train_dir,
                                val_dir = val_dir \
                              )
     
            expected_train_dx1 = set(['image0.jpg','image1.jpg','image2.jpg'])
           
            
            returned_train_dx1 = set(os.listdir(os.path.join(train_dir,'dx1')))
            

            #print(returned_train_dx1 in expected_train_dx1) 
            
            self.assertEqual(returned_train_dx1.issubset(expected_train_dx1),True)
        
if __name__ == '__main__':
    
    unittest.main()
 