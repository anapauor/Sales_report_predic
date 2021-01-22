#usefull modeules
import pandas as pd
import os
from jinja2 import FileSystemLoader, Environment


# Sale resport class for report generation from files 

env = Environment(
    loader=FileSystemLoader(searchpath="templates")
)
template = env.get_template("report.html")

content = "Hello, world!"

def main():
    """
    Entry point for the script.
    Render a template and write it to file.
    :return:
    """
    with open("Output/report.html", "w") as f:
        f.write(template.render(content=content)) # links the template wiht the code


"""  
## Programm for creating reports from monthly sales data

FileData cls -> loaded csv files containing monthly sales
    get_joined_data mtd: return a single file with charged period sales 

SalesReport cls -> Period Reports

"""

class FileData():
    """ 
    File prep
    """ 
    def __init__(self, files, path):
        self.files = files # name of the input files
        self.path = path # name of the input path
        self.all_months_data = pd.DataFrame()
        
    def get_joined_monthly_data(self): 
        "Joints the monthly sales data in a single file named in 'new_file_name' located in the 'op_path'"  
        for file in self.files:
            current_data = pd.read_csv(self.path+"/"+file)
            self.all_months_data = pd.concat([self.all_months_data, current_data])
        return self.all_months_data

    # def save_joined_monthly_data(self, new_file_name, op_path):
    #     self.all_months_data.to_csv((os.path.join(op_path, new_file_name+ '.csv')), index=False)

class AllMonthData():
    def __init__(self, all_months_data):
        self.all_months_data = pd.DataFrame(all_months_data)

    def get_clean_empty_val(self): 
        "Pre-processing data, eliminate NaN values and return cleaned DataFrame"
        self.all_months_data = self.all_months_data.dropna(how='all') # Find and remove NAN
        return self.all_months_data

    def set_month_column(self):
        "Set the month number in a new column 'Month', return updated DataFrane"
        self.all_months_data.rename(columns={'Order Date': 'Order_Date'})
        self.all_months_data['Month'] = pd.to_datetime(self.all_months_data['Order Date']).dt.month # Add a month column




    # def get_address(self):
    #     def get_city(address): # Func to extract the city adress
    #         return address.split(",")[1].strip(" ")
    #     def get_state(address): # Func to extract the state adress
    #         return address.split(",")[2].split(" ")[1]
    #     #  Create colum for city (state) applying get_city and get_state
    #     self.all_months_data['City'] = self.all_months_data['Purchase Address'].apply(lambda x: f"{get_city(x)}  ({get_state(x)})")
    #     return self.all_months_data



if __name__ == '__main__':
    main()

