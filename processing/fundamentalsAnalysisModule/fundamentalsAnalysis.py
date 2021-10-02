# Header Files
import pandas as pd # Pre-requisite to run Pandas
from pandas import Series, DataFrame
import numpy as np # Pre-requisite to run numpy

import datetime # Import date time for datetime data type
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

import math # For isnan() function

class financialData_main:
    df_output = pd.DataFrame(columns = ["Financial Ratios"])
    financialYears = [] # List but later input to array?
    
    # Initialization
    
    def __init__(self, df_name, sheet_name, index_col_pos = None):
        print("Financial Data Object created")
        
        self.df_input = pd.read_excel(df_name, sheet_name, index_col = index_col_pos)
        self.df_input = (self.df_input).dropna() # Clean dataframe and remove any irrelevant data

    # Getters
    
    def getInput(self):
        return self.df_input
        
    def getOutput(self):
        return self.df_output
    
    def getInputElement(self, itemName, financialYear): # Update to include failure to find item
        if (self.df_input[self.df_input.columns[0]] == itemName).any() == True:
            return (self.df_input.loc[self.df_input[self.df_input.columns[0]] == itemName, financialYear].values)[0]
        else:
            print(itemName, " not Found")
            return 0.0
    
    def getFinancialYears(self):
        return self.financialYears
    
    # Setters
    
    def setOutput_row(self, itemName):
        self.df_output = self.df_output.append({"Financial Ratios": itemName}, ignore_index = True, sort = False)
        
    def setOutput_element(self, itemName, financialYear, value):
        self.df_output.loc[self.df_output[self.df_output.columns[0]] == itemName, financialYear] = value
    
    def setFinancialYears(self):
        # Assuming consistent formatting of columns: items, source documents, year 00 -> year 05.
        self.financialYears = (self.df_input.columns.values)[2:(len(self.df_input.columns.values))]
        
    # Write to Excel
    def writeOutput(self, doc_name):
        xlsx_name = doc_name + ".xlsx"
        
        #print(doc_name , xlsx_name)
        (self.getOutput()).to_excel(xlsx_name, sheet_name = 'output')