import os
import unittest
import pandas as pd
import pandas.testing as pd_testing
from non_duplicate_lesion_id import non_duplicate_lesion_id

 
class TestCreateNonDuplicateLesionId(unittest.TestCase):
    
    
    def assertDataframeEqual(self, a, b, msg):
        
        try:
            pd_testing.assert_frame_equal(a, b)
        except AssertionError as e:
            raise self.failureException(msg) from e
            
    def setUp(self):
        self.addTypeEqualityFunc(pd.DataFrame, self.assertDataframeEqual)

    def test_one(self):
                        
        """
        Test  non duplicate lesion_id
        """
        
        lesion_id = {'lesion_id':['ab','cd','ab','ef']}
        
        input_df = pd.DataFrame.from_dict({'lesion_id':['ab','cd','ab','ef']}) 
        
        expected_non_duplicate_df = pd.DataFrame \
                                       .from_dict({ \
                                                   'lesion_id':['cd','ef'],
                                                   'non_duplicate':[True,True] \
                                                  })
        
        expected_df = pd.DataFrame.from_dict({ \
                                                'lesion_id':['ab','cd','ab','ef'],
                                                'non_duplicate':[False,True,False,True] \
                                             })
           
        returned_df, returned_non_duplicate_df = non_duplicate_lesion_id(input_df)

        self.assertEqual(expected_df,returned_df)
        self.assertEqual(expected_non_duplicate_df,returned_non_duplicate_df)
        
if __name__ == '__main__':
    
    unittest.main()
 