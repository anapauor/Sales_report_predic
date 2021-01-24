# usefull modules
from sales import ReportResult
from sales import csv_to_df, get_joined_monthly_data

import pandas as pd
from pandas._testing import assert_frame_equal
import unittest
import os

# Set Up samples

path_test = "/home/ana/Documentos/Proyectos/Sales/data"
files_test = [file for file in os.listdir(path_test) if not file.startswith('.')] # Ignore hidden files

file_report = FileData(files=files_test, path=path_test)

new_name_file = 'all_data_sales'
op_path = '/home/ana/Documentos/Proyectos/Sales/Data-Science-Solution/Output'

saved = (pd.read_csv(os.path.join(op_path, new_name_file + '.csv'))).reset_index(drop=True)

df = AllMonthData(saved)

# -------------------------------> TEST <---------------------------------------------------------------

class TestFileData(unittest.TestCase):

    def test_FileData_files(self):
        self.assertEqual(file_report.files, files_test)
    
    def test_FileData_path(self):
        self.assertEqual(file_report.path, path_test)
    
    def test_save_joined_monthly_data(self):
    #     Report1.save_joined_monthly_data(new_name_file, op_path)
        self.assertTrue(os.path.exists(op_path+'/'+new_name_file+'.csv'))

    def test_join_monthly_data(self): # test the  jointed and the saved data
        assert_frame_equal((file_report.get_joined_monthly_data()).reset_index(drop=True), saved.reset_index(drop=True))

class TestAllMonthData(unittest.TestCase):

    def test_clean_empty_val(self):
        self.assertFalse((df.clean_empty_val()).isnull().values.any())
    
    def test_set_month_column(self):
        
        self.assertTrue('Month' in (df.set_month_column()))



# ----------------------------------------------
if __name__ == '__main__':
    unittest.main()

