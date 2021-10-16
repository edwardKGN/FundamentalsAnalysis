# Header Files
import pandas as pd # Pre-requisite to run Pandas
from pandas import Series, DataFrame
import numpy as np # Pre-requisite to run numpy

import datetime # Import date time for datetime data type
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

from analysisModule.statisticsModule.statisticsMod import linReg # Apparently it's read from the calling page
from scipy import stats

import math # For isnan() function

class FA:
    df_quality = pd.DataFrame(columns = ["Financial Ratios", "Condition"])
    df_growth = pd.DataFrame(columns = ["Financial Ratios", "Growth", "Intercept", "Correlation Coefficient", "Growth Uncertainty", "Intercept Uncertainty"])
    financialYears = []
    
    # Read FA Output Excel file 
    def __init__(self, xlsx_name, sheet_name, index_col_pos = None):
        print("Financial Data Object created")
        
        self.df_input = pd.read_excel(xlsx_name, sheet_name, index_col = index_col_pos)
        self.df_input = (self.df_input).dropna() # Clean dataframe and remove any irrelevant data
        self.setFinancialYears()
    
    # Getters
    def getFinancialYears(self):
        return self.financialYears
    
    def getInput(self):
        return self.df_input
    
    def getOutput(self, df_option):  
        if df_option == 0:
            return self.df_quality
        elif df_option == 1:
            return self.df_growth
        else:
            print("ERROR - Option not recognized")
            return 
    
    # Read Row
    def getInput_row(self, item):
        return ((self.df_input.loc[self.df_input[self.df_input.columns[0]] == item]).values[0])[1:]
    
    # Setters
    def setFinancialYears(self):
        # Assuming consistent formatting of columns: items, source documents, year 00 -> year 05.
        self.financialYears = (self.df_input.columns.values)[1:(len(self.df_input.columns.values))]
    
    def setFirstColumn_element(self, item, df_option):
        if df_option == 0:
            #print("Setting First Column Element:", item)
            self.df_quality = self.df_quality.append({"Financial Ratios": item}, ignore_index = True, sort = False)
        elif df_option == 1:
            #print("Setting First Column Element:", item)
            self.df_growth = self.df_growth.append({"Financial Ratios": item}, ignore_index = True, sort = False)
        else:
            print("ERROR - Option not recognized")
            return 
    
    # Applicable to df_quality only
    def setCondition_element(self, item, element): 
        self.df_quality.loc[self.df_quality[self.df_quality.columns[0]] == item, "Condition"] = element
        
    def setQualities_row(self, item, condition_value, condition_option):
        self.setFirstColumn_element(item, 0)
        
        input_row = self.getInput_row(item)
        
        if condition_option == 0:
            ls_quality = input_row == condition_value
            self.setCondition_element(item, ("==" + str(condition_value)))
        elif condition_option == 1:
            ls_quality = input_row > condition_value
            self.setCondition_element(item, (">" + str(condition_value)))
        elif condition_option == 2:
            ls_quality = input_row >= condition_value
            self.setCondition_element(item, (">=" + str(condition_value)))
        elif condition_option == 3:
            ls_quality = input_row < condition_value
            self.setCondition_element(item, ("<" + str(condition_value)))
        elif condition_option == 4:
            ls_quality = input_row <= condition_value
            self.setCondition_element(item, ("<=" + str(condition_value)))
        else: 
            print("ERROR - Option not recognized")
            return
        
        #print(ls_quality)
        
        for index, year in enumerate(self.getFinancialYears()):
            #print(index, year)
            self.df_quality.loc[self.df_quality[self.df_quality.columns[0]] == item, year] = ls_quality[index]
    
    # Applicable to df_growth only
    def setGrowth(self, item):
        self.setFirstColumn_element(item, 1)
        
        input_row = self.getInput_row(item) 
        years = self.getFinancialYears()
        
        #print("Type Financial Ratios ", type(input_row), "Items: ", input_row)
        #print("Type Financial Years ", type(years), "Years: ", years)
        
        #linReg_out = linReg(years, input_row)
        #print(linReg_out, type(linReg_out), linReg_out[0])
        
        linReg_result = stats.linregress(list(years), list(input_row)) # Use Scipy.stats Linear Regression method       
        linReg_out = (linReg_result.slope, linReg_result.intercept, linReg_result.rvalue, linReg_result.stderr, linReg_result.intercept_stderr)
        
        #print(self.getOutput(1).columns[1:])
        for index, column_name in enumerate(self.getOutput(1).columns[1:]):
            #print(index, column_name)
            self.df_growth.loc[self.df_growth[self.df_growth.columns[0]] == item, column_name] = linReg_out[index]
        
    # Write to Excel
    def writeOutput(self, doc_name):
        xlsx_name = doc_name + ".xlsx"
        
        #print(doc_name , xlsx_name)
        (self.getOutput(0)).to_excel(("quality_" + xlsx_name), sheet_name = 'output')
        (self.getOutput(1)).to_excel(("growth_" + xlsx_name), sheet_name = 'output')