from . import fundamentalsAnalysis 

class profitability_gen(fundamentalsAnalysis.financialData_main):
    
    """
    List of Financial Ratios
    
    # Valuation
    - Return on Equity
    - Return on Capital Employed
    - EBITDA to Revenue Ratio
    """
    
    def analyzeProfitability(self): # Equivalent to Run All
        print("Analyzing Profitability")
        
        self.setOutput_row("Return on Equity")
        self.setOutput_row("Return on Capital Employed")
        self.setOutput_row("EBITDA to Revenue Ratio")
        
        self.setFinancialYears()
        
        for year in self.getFinancialYears():
            self.setOutput_element("Return on Equity", year, self.ROE(year))
            self.setOutput_element("Return on Capital Employed", year, self.ROCE(year))
            self.setOutput_element("EBITDA to Revenue Ratio", year, self.ebitdaToRevenueRatio(year))
        
    # Financial Ratios
    ## Return on Equity # TAG for future search
    def ROE(self, year): 
        netIncome = self.getInputElement("Net Income", year) 
        shareholderEquity = self.getInputElement("Shareholders Equity", year)
        # Note the apostrophe in Python script differ from libreoffice text. Copy apostrophy from source.
        
        if shareholderEquity == 0:
            print("ERROR - ROE: denominator is zero")
            return 0.0
        
        return netIncome/shareholderEquity
    
    ## Return on Capital Employed
    def ROCE(self, year):
        operatingProfit = self.getInputElement("Operating Profit", year)
        
        totAssets = self.getInputElement("Total Assets", year)
        curLiabilities = self.getInputElement("Current Liabilities", year)
        
        capitalEmployed = totAssets - curLiabilities
        
        if capitalEmployed == 0:
            print("ERROR - ROCE: denominator is zero")
            return 0
        
        return operatingProfit/capitalEmployed
    
    ## EBITDA to Revenue Ratio  
    def ebitdaToRevenueRatio(self, year):        
        netIncome = self.getInputElement("Net Income", year) 
        depreciation = self.getInputElement("Depreciation", year)
        amortization = self.getInputElement("Amortization", year)
        interest = self.getInputElement("Interest Expense", year)
        tax = self.getInputElement("Tax", year)
        
        EBITDA = netIncome + interest + tax + depreciation + amortization
        
        revenue = self.getInputElement("Revenue", year)
        
        if revenue == 0:
            print("ERROR - EBITDA to Revenue Ratio: denominator is zero")
            return 0
        
        return EBITDA/revenue
        
    