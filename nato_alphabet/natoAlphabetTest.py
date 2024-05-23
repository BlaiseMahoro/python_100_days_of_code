import unittest
from unittest.mock import patch
import pandas as pd
from main import read_csv, setup_dict


class NatoAlphabetTest(unittest.TestCase):
    @patch('pandas.read_csv')
    def test_read_csv(self, mock_read_csv):
        mock_read_csv.return_value = pd.DataFrame({
            'letter': ['A', 'B', 'C'],
            'code': ['Alpha', 'Bravo', 'Charlie']
        })
        csv_file = 'nato_phonetic_alpha_test1.csv'
        data = read_csv(csv_file)
        expected_data = mock_read_csv()
        self.assertEqual(data.code.to_list(), expected_data.code.to_list())
        
    # @patch('pandas.DataFrame')
    # def test_setup_dict(self, mock_data_frame):
    #     mock_data_frame.return_value = 
        
        
    
        
        
if __name__ == '__main__':
    unittest.main()
    
        
        
        
        
        