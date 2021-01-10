#usefull modeules
import pandas as pd
import os

# Sale resport class for report generation from files 
class SalesReport():
    """Genererates reports of mothly sales based on cvs data files"""

    def __init__(self, files, path):
        self.files = files # name of the input files
        self.path = path # name of the input path
        
    def join_monthly_data(self, new_file_name, op_path): 
        "Joints the monthly sales data in a single file named in 'new_file_name' located in the 'op_path'"
        all_months_data = pd.DataFrame()
        for file in self.files:
            current_data = pd.read_csv(self.path+"/"+file)
            all_months_data = pd.concat([all_months_data, current_data])
        all_months_data.to_csv((os.path.join(op_path, new_file_name+ '.csv')), index=False)
        return all_months_data
        
    def clean_empty_val(self, data): 
        'Pre-processing data'
        data = data.dropna(how='all') # Find and remove NAN
        data['Month'] = pd.to_datetime(data['Order Date']).dt.month # Add a month column
        def get_city(address): # Func to extract the city adress
            return address.split(",")[1].strip(" ")
        def get_state(address): # Func to extract the state adress
            return address.split(",")[2].split(" ")[1]
        # Generate colum for city (state)
        data['City'] = data['Purchase Address'].apply(lambda x: f"{get_city(x)}  ({get_state(x)})")
        return data



__name__ == '__main__'

