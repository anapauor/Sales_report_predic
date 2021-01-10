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


# -------------------------------> TEST <---------------------------------------------------------------

class TestSalesReport(unittest.TestCase):

    def test_SalesReport_files(self):
        self.assertEqual(Report1.files, files_test)
    
    def test_SalesReport_path(self):
        self.assertEqual(Report1.path, path_test)
    
    def test_join_monthly_data(self):
        report = (Report1.join_monthly_data(new_name_file, op_path)).reset_index(drop=True)
        df = (pd.read_csv(os.path.join(op_path, new_name_file + '.csv'))).reset_index(drop=True)
        assert_frame_equal(report.reset_index(drop=True), df.reset_index(drop=True))


# all_months_data = pd.DataFrame()

# # for file in files:
# #     current_data = pd.read_csv(path+"/"+file)
# #     all_months_data = pd.concat([all_months_data, current_data])
    
# all_months_data.to_csv("all_data_copy.csv", index=False)


# ----------------------------------------------
if __name__ == '__main__':
    unittest.main()

