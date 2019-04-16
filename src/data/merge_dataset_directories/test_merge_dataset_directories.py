from merge_dataset_directories import merge_dataset_directories
import tempfile
import unittest
import os
 
class TestMergeDatasetDirectories(unittest.TestCase):
    
    """
    Test the add function from the mymath library
    """
    
    def test_temp_dir_1(self):
        
        """        
        Test that tmp and tmp/tmp directories are created       
        """
        with tempfile.TemporaryDirectory() as tmpdir1:
            with tempfile.TemporaryDirectory() as tmpdir2:
                with tempfile.TemporaryDirectory() as tmpdir3:
                    with tempfile.NamedTemporaryFile(dir=tmpdir1) as tmpfile1:
                        with tempfile.NamedTemporaryFile(dir=tmpdir2) as tmpfile2:
                            
                            merge_dataset_directories(
                                      final_dir = tmpdir3,\
                                      directories = [tmpdir1,tmpdir2] \
                                      )
                            
                            self.assertEqual(set(os.listdir(tmpdir3)),set(os.listdir(tmpdir1) + os.listdir(tmpdir2)))

if __name__ == '__main__':
    
   
    print('created temporary directory', type(tmpdirname))    
    unittest.main()