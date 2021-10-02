from . import fundamentalsAnalysis

class liquidity_gen(fundamentalsAnalysis.financialData_main):
    
    """
    List of Financial Ratios
    
    # Liquidity
    - Current Ratio
    - Cash Ratio
    - Operating Cash Flow Ratio
    - Cash Conversion Ratio
    """
    
    def analyzeLiquidity(self): # Equivalent to Run All
        print("Analyzing Liquidity")
        
        self.setOutput_row("Current Ratio")
        self.setOutput_row("Cash Ratio")
        
        self.setOutput_row("Operating Cash Flow Ratio")
        self.setOutput_row("Cash Conversion Ratio")
        
        self.setFinancialYears()
        
        for year in self.getFinancialYears(): # Return Financial Ratios as fractions
            # print(year)
            
            self.setOutput_element("Current Ratio", year, self.currentRatio(year))
            self.setOutput_element("Cash Ratio", year, self.cashRatio(year))
            
            self.setOutput_element("Operating Cash Flow Ratio", year, self.operatingCashFlowRatio(year))
            self.setOutput_element("Cash Conversion Ratio", year, self.cashConversionRatio(year))
    
    # Financial Ratio
    ## Current Ratio
    def currentRatio(self, year):
        curAssets = self.getInputElement("Current Assets", year)
        curLiabilities = self.getInputElement("Current Liabilities", year)
        
        if curLiabilities == 0:
            print("ERROR - Current Ratio: denominator is zero")
            return 0.0
        
        return curAssets/curLiabilities
    
    ## Cash Ratio
    def cashRatio(self, year):
        cashAndCashEq = self.getInputElement("Cash and Cash Equivalent", year)
        curLiabilities = self.getInputElement("Current Liabilities", year)
        
        if curLiabilities == 0:
            print("ERROR - Current Ratio: denominator is zero")
            return 0.0
        
        return cashAndCashEq/curLiabilities
    
    ## Operating Cash Flow Ratio
    def operatingCashFlowRatio(self, year):
        netCashOps = self.getInputElement("Net Cash Flow from Operations", year)
        curLiabilities = self.getInputElement("Current Liabilities", year)
        
        if curLiabilities == 0:
            print("ERROR - Operating Cash Flow Ratio: denominator is zero")
            return 0.0
       
        return netCashOps/curLiabilities
    
    ## Cash Conversion Ratio
    def cashConversionRatio(self, year):
        netCashOps = self.getInputElement("Net Cash Flow from Operations", year)
        netIncome = self.getInputElement("Net Income", year)
        
        if netIncome == 0:
            print("ERROR - Cash Conversion Ratio: denominator is zero")
            return 0.0
       
        return netCashOps/netIncome