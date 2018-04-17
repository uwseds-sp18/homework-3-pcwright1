import unittest
from DATA515HW3 import create_dataframe

# Define a class in which the tests will run
class test_create_dataframe(unittest.TestCase):

    def test_smoke(self):
        #self.assertTrue(create_dataframe('class.db'))
        create_dataframe('class.db')
        
    def test_columns(self):
        #self.assertEqual(entropy_calc([1]),0)
        self.assertEqual(set(create_dataframe('class.db').columns), {'video_id', 'category_id', 'language'})
    
    def test_length(self):
        #self.assertEqual(entropy_calc([1]),0)
        self.assertTrue(len(create_dataframe('class.db')) >= 10)
    
    def test_is_key(self):
        #self.assertEqual(entropy_calc([1]),0)
        df = create_dataframe('class.db')
        #self.assertTrue(len(create_dataframe('class.db')) == len(create_dataframe('class.db').loc[:,['video_id','language']].drop_duplicates()))
        self.assertTrue(len(df) == len(df.loc[:,['video_id','language']].drop_duplicates()))

    def test_incorrect_file_path(self):
        #self.assertEqual(entropy_calc([1]),0)
        self.assertRaises(ValueError,create_dataframe,'foo_junk_bar.db')
    
if __name__ == '__main__':
    unittest.main()
