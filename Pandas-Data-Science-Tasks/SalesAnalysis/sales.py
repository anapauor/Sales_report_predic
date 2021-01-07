#usefull modeules
import pandas as pd

# Sale resport class for report generation from files 
class SalesReport():

    def __init__(self, files, path):
        self.files = []
        self.path = path
        
    def join_monthly_data(self, path, files):
        for file in self.files:
            current_data = pd.read_csv(path+"/"+file)
            all_months_data = pd.concat([all_months_data, current_data])
        return all_months_data.to_csv(('{}.cvs').format(self.files), index=False)




__name__ == '__main__'
