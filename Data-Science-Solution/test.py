# usefull modules
from sales import SalesReport
import pandas as pd
from pandas._testing import assert_frame_equal
import unittest
import os

# SAMPLES

path_test = "/home/ana/Documentos/Proyectos/Sales/Data-Science-Solution/SalesAnalysis/Sales_Data"
files_test = [file for file in os.listdir(path_test) if not file.startswith('.')] # Ignore hidden files
Report1 = SalesReport(files=files_test, path=path_test)
new_name_file = 'all_data_sales'
op_path = '/home/ana/Documentos/Proyectos/Sales/Data-Science-Solution/Output'
df = (pd.read_csv(os.path.join(op_path, new_name_file + '.csv'))).reset_index(drop=True)


# -------------------------------> TEST <---------------------------------------------------------------

class TestSalesReport(unittest.TestCase):

    def test_SalesReport_files(self):
        self.assertEqual(Report1.files, files_test)
    
    def test_SalesReport_path(self):
        self.assertEqual(Report1.path, path_test)
    
    def test_join_monthly_data(self):
        jointed = (Report1.join_monthly_data(new_name_file, op_path)).reset_index(drop=True)
        assert_frame_equal(jointed.reset_index(drop=True), df.reset_index(drop=True))

    def test_clean_empty_val(self):
        cleaned = Report1.clean_empty_val(df)
        self.assertEqual(cleaned.isnull().values.any(), False)

# ----------------------------------------------
if __name__ == '__main__':
    unittest.main()

