#usefull modeules
import pandas as pd
import os
from jinja2 import FileSystemLoader, Environment


"""  
## Programm for creating reports from monthly sales data

FileData cls -> loaded csv files containing monthly sales
    get_joined_data mtd: return a single file with charged period sales 

SalesReport cls -> Period Reports

"""

class ReportResult():
    """
    Class to store the results of reports from sales data.
    """

    def __init__(self, path, files):
        self.path = path
        self.files = files
        self.all_months_data = get_joined_monthly_data(path, files)

    def get_clean_empty_val(self): 
        "Pre-processing data, eliminate NaN values and return cleaned DataFrame"
        self.all_months_data = self.all_months_data.dropna(how='all') # Find and remove NAN
        return self.all_months_data

    def set_month_column(self):
        "Set the month number in a new column 'Month', return updated DataFrane"
        self.all_months_data.rename(columns={'Order Date': 'Order_Date'})
        self.all_months_data['Month'] = pd.to_datetime(self.all_months_data['Order Date']).dt.month # Add a month column

    def get_df_as_html(self):
        """
        Return the results DataFrame as an HTML object.
        :return: String of HTML.
        """
        html = self.all_months_data.to_html()
        return html



def get_joined_monthly_data(path, files): 
    """
    Join monthly sales data in .csv format and put them into single df
    :param path: Path to de monthly data files
    :files: list of files with monthly data
    """  
    for file in files:
        current_data = pd.read_csv(path+"/"+file)
        df_all_months = pd.DataFrame()
        df_all_months = pd.concat([df_all_months, current_data])
    return df_all_months   

def csv_to_html(filepath):
    """
    Open a .csv file and return it in HTML format.
    :param filepath: Filepath to a .csv file to be read.
    :return: String of HTML to be published.
    """
    df = pd.read_csv(filepath, index_col=0)
    html = df.to_html()
    return html

# Configure Jinja and ready the loader
env = Environment(
    loader=FileSystemLoader(searchpath="templates")
)

# Assemble the templates I'll use
base_template = env.get_template("report.html")
table_section_template = env.get_template("table_section.html")


def main():
    """
    Entry point for the script.
    Render a template and write it to file.
    :return:
    """

    # Content to be published (code that I only want executed when explicitly run the script)
    title = "Model Report"
    sections = list()
    sections.append(table_section_template.render(
        model="FirstTry",
        dataset="all_data_copy.csv",
        table=csv_to_html("Output/all_data_sales.csv")
    ))
    with open("Output/report.html", "w") as f:
        f.write(base_template.render(
            title=title,
            sections=sections
        ))


if __name__ == '__main__':
    main()

