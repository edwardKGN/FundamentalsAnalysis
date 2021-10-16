from . import financialRatios

class efficiency_gen(financialRatios.financialData_main):
    
    """
    List of Financial Ratios
    
    # Efficiency
    - EBITDA to Cash Conversion
    - Revenue to Expense Ratio
    """
    
    def analyzeEfficiency(self): # Equivalent to Run All
        print("Analyze Efficiency")
        
        # Set Up Rows to Fill In Key information
        self.setOutput_row("EBITDA to Cash Conversion")
        self.setOutput_row("Revenue to Expense Ratio")
        
        self.setFinancialYears()
        
        for year in self.getFinancialYears(): # Return Financial Ratios as fractions
            #print(year)
        
            self.setOutput_element("EBITDA to Cash Conversion", year, self.ebitdaToCashConversion(year))
            
            self.setOutput_element("Revenue to Expense Ratio", year, self.revenueToExpenseRatio(year))
    
    # Financial Ratio
    
    ## EBITDA to Cash Conversion
    def ebitdaToCashConversion(self, year):
        netCashOps = self.getInputElement("Net Cash Flow from Operations", year)
        
        netIncome = self.getInputElement("Net Income", year) 
        depreciation = self.getInputElement("Depreciation", year)
        amortization = self.getInputElement("Amortization", year)
        interest = self.getInputElement("Interest Expense", year)
        tax = self.getInputElement("Tax", year)
        
        EBITDA = netIncome + interest + tax + depreciation + amortization
        
        if EBITDA == 0:
            print("ERROR - EBITDA to Cash Conversion: denominator is zero")
            return 0.0
        
        return netCashOps/EBITDA
    
    ## Revenue to Expense Ratio
    def revenueToExpenseRatio(self, year):
        revenue = self.getInputElement("Revenue", year)
        
        totalExpenses = self.getInputElement("Total Expenses", year)
        
        if totalExpenses == 0:
            print("ERROR - Revenue to Expense Ratio: denominator is zero")
            return 0
        
        return revenue/totalExpenses