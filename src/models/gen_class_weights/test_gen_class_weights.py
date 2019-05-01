
import unittest
from class_weights import gen_class_weights
 
class TestGenClassWeights(unittest.TestCase):
    
    """
       Test class_weigths module 
    """
    
    def test_gen_class_weights_1(self):
        
        """        
          'mel' attribute has weight 3.0 and 'bbc' attribute does not has weight 2.0
        """
        
        class_indices = {'akiec': 0, 'bcc': 1, 'bkl': 2, 'df': 3, 'mel': 4, 'nv': 5, 'vasc': 6}
        
        expected_class_weights = gen_class_weights(class_indices = class_indices)
        
        self.assertEqual(expected_class_weights[4],3.0)
        self.assertEqual(expected_class_weights[1]==2.0,False)

if __name__ == '__main__':
    
    unittest.main()
    
    
    