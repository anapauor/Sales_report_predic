
This is a program for sales report generator- 

## Content info 

'Sales_Data' folder contains the input monthly data to be process
'Output' folder contains the results obtained
'Test' folder contains the tests performed to the processing program 

Some formulas taken from https://python-programming.quantecon.org/python_oop.html

## Background Processing Information:

Start by cleaning our data, including:
- Drop NaN values from DataFrame
- Removing rows based on a condition
- Change the type of columns (to_numeric, to_datetime, astype)

Once cleaned up the data a bit, move the data exploration section. In this section we explore 5 high level business questions related to our data:
- What was the best month for sales? How much was earned that month?
- What city sold the most product?
- What time should we display advertisemens to maximize the likelihood of customer’s buying product?
- What products are most often sold together?
- What product sold the most? Why do you think it sold the most?

To answer these questions we walk through many different pandas & matplotlib methods. They include:
- Concatenating multiple csvs together to create a new DataFrame (pd.concat)
- Adding columns
- Parsing cells as strings to make new columns (.str)
- Using the .apply() method
- Using groupby to perform aggregate analysis
- Plotting bar charts and lines graphs to visualize our results
- Labeling our graphs
