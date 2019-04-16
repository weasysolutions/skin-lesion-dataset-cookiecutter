import os
import unittest
import pandas as pd
import pandas.testing as pd_testing
from training_and_validation_sets import training_and_validation_sets


class TestTrainingAndValidationSets(unittest.TestCase):
    


    def test_one(self):
                        
        """
        Test if validation set is contained in input_unique_id_df
        Test if training set is contained in input_df
        """

        
        input_df = pd.DataFrame.from_dict({ \
                                                'lesion_id':['ab','cd','ab','ef'],
                                                'dx':['1','1','1','1'],
                                                'non_duplicate':[False,True,False,True] \
                                             })
        
        input_unique_id_df = pd.DataFrame \
                                       .from_dict({ \
                                                   'lesion_id':['cd','ef'],
                                                   'dx':['1','1'],
                                                   'non_duplicate':[True,True] \
                                                  }) 
        

        returned_complete_df, returned_train_df, returned_val_df = \
                                               training_and_validation_sets(input_df,input_unique_id_df)

        self.assertEqual(returned_val_df.lesion_id.isin(input_unique_id_df.lesion_id).all(),True)

        
if __name__ == '__main__':
    
    unittest.main()
 