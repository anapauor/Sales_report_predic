#usefull modeules
import pandas as pd
import os

# Sale resport class for report generation from files 
class SalesReport():

    def __init__(self, files, path):
        self.files = files
        self.path = path
        
    def join_monthly_data(self, new_file_name, op_path):
        all_months_data = pd.DataFrame()
        
        for file in self.files:
            current_data = pd.read_csv(self.path+"/"+file)
            all_months_data = pd.concat([all_months_data, current_data])
        
        # all_months_data.to_csv(('{}.cvs').format(new_file_name), index=False)
        all_months_data.to_csv((os.path.join(op_path, new_file_name+ '.csv')), index=False)
        
        return all_months_data
        



__name__ == '__main__'

path_test = "/home/ana/Documentos/Proyectos/Sales/Data-Science-Solution/SalesAnalysis/Sales_Data"
files_test = [file for file in os.listdir(path_test) if not file.startswith('.')] # Ignore hidden files
Report1 = SalesReport(files=files_test, path=path_test)
new_name_file = 'all_data_sales'
op_path = '/home/ana/Documentos/Proyectos/Sales/Data-Science-Solution/Output'


report = (Report1.join_monthly_data(new_name_file, op_path)).reset_index(drop=True)
df = (pd.read_csv(os.path.join(op_path, new_name_file + '.csv'))).reset_index(drop=True)



# print(report.head())
# print(df.head())

((report) == (df))

from pandas._testing import assert_frame_equal


assert_frame_equal(report.reset_index(drop=False), df.reset_index(drop=True))