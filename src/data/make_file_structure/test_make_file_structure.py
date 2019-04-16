from make_file_structure import file_structure
import tempfile
import unittest
import os
 
class TestMakeFileStructure(unittest.TestCase):
    
    """
    Test the add function from the mymath library
    """
    
    def test_temp_dir_1(self):
        
        """        
        Test that tmp and tmp/tmp directories are created       
        """
        
        with tempfile.TemporaryDirectory() as tmpdirname:
            
            #print('created temporary directory', tmpdirname,type(tmpdirname))
            base_dir=os.path.join(tmpdirname,'tmp')  
            
            make_file_structure(base_dir,[['tmp']]);        
                 
            self.assertEqual(os.listdir(tmpdirname),['tmp'])
            self.assertEqual(os.listdir(base_dir),['tmp'])

    def test_temp_dir_2(self):
        
        
        """        
        Test that  tmp/tmp directories are created        
        """
        
        with tempfile.TemporaryDirectory() as tmpdirname:
            
            #print('created temporary directory', tmpdirname,type(tmpdirname))
            base_dir=os.path.join(tmpdirname,'tmp')  
            
            make_file_structure(base_dir,[['tmp1','tmp2'],['tmp3','tmp4']]);        
                 
            self.assertEqual(os.listdir(tmpdirname),['tmp'])
            self.assertEqual(set(os.listdir(base_dir)),set(['tmp1','tmp2']))
            self.assertEqual(set(os.listdir(os.path.join(base_dir,'tmp1'))),set(['tmp3','tmp4']))
     
 
if __name__ == '__main__':
    
    with tempfile.TemporaryDirectory() as tmpdirname:
                
        print('created temporary directory', type(tmpdirname))
    
    unittest.main()
 