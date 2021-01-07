# usefull modules
from sales import SalesReport
import unittest
import os

# SAMPLES
path_test = "/home/ana/Documentos/Proyectos/Sales/Pandas-Data-Science-Tasks/SalesAnalysis/Sales_Data"
files_test = [file for file in os.listdir(path_test) if not file.startswith('.')] # Ignore hidden files
report1 = SalesReport(files=files_test, path=path_test)



# all_months_data = pd.DataFrame()

# # for file in files:
# #     current_data = pd.read_csv(path+"/"+file)
# #     all_months_data = pd.concat([all_months_data, current_data])
    
# all_months_data.to_csv("all_data_copy.csv", index=False)


# -------------------------------> TEST <---------------------------------------------------------------

class TestSalesReport(unittest.TestCase):
    def test_SalesReport(self):
        self.assertEqual(report1.files(), files_test)










# ----------------------------------------------
if __name__ == '__main__':
    unittest.main()