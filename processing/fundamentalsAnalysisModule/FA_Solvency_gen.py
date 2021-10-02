from . import fundamentalsAnalysis

class solvency_gen(fundamentalsAnalysis.financialData_main):
    
    """
    List of Financial Ratios
    
    # Solvency
    - Debt Ratio
    - Debt to Equity Ratio
    - Interest Coverage Ratio
    - Years to Repay Debt
    - Average Interest Rate
    """
    
    def analyzeSolvency(self):
        print("Analyzing Solvency")

        self.setOutput_row("Debt Ratio")
        self.setOutput_row("Debt to Equity Ratio")
        self.setOutput_row("Interest Coverage Ratio")
        self.setOutput_row("Years to Repay Debt")
        self.setOutput_row("Average Interest Rate")
        
        self.setFinancialYears()
        
        for year in self.getFinancialYears():
            self.setOutput_element("Debt Ratio", year, self.debtRatio(year))
            self.setOutput_element("Debt to Equity Ratio", year, self.debtToEquityRatio(year))
            self.setOutput_element("Interest Coverage Ratio", year, self.interestCoverageRatio(year))
            self.setOutput_element("Years to Repay Debt", year, self.yearsToRepayDebt(year))
            self.setOutput_element("Average Interest Rate", year, self.averageInterestRate(year))
    
    # Financial Ratio
    ## Debt Ratio
    def debtRatio(self, year):
        totDebt = self.getInputElement("Total Debt", year)
        totAssets = self.getInputElement("Total Assets", year)
        
        if totAssets == 0:
            print("ERROR - Debt Ratio: Total Assets is zero")
            return 0
        
        return totDebt/totAssets
    
    ## Debt to Equity Ratio
    def debtToEquityRatio(self, year):
        totDebt = self.getInputElement("Total Debt", year)
        totAssets = self.getInputElement("Total Assets", year)
        totLiab = self.getInputElement("Total Liabilities", year)
        
        totEquity = totAssets - totLiab
        
        if totEquity == 0:
            print("ERROR - Debt to Equity Ratio: Total Equity is zero")
            return 0
        
        return totDebt/totEquity
    
    ## Interest Coverage Ratio
    def interestCoverageRatio(self, year):
        netIncome = self.getInputElement("Net Income", year) 
        depreciation = self.getInputElement("Depreciation", year)
        amortization = self.getInputElement("Amortization", year)
        interest = self.getInputElement("Interest Expense", year)
        tax = self.getInputElement("Tax", year)
        
        EBITDA = netIncome + interest + tax + depreciation + amortization
        interest = self.getInputElement("Interest Expense", year)
        
        if interest == 0:
            print("ERROR - Interest Coverage Ratio: Interest Expense is zero")
            return 0
        
        return EBITDA/interest
    
    # Years to Repay Debt
    def yearsToRepayDebt(self, year):
        totDebt = self.getInputElement("Total Debt", year)
        
        netIncome = self.getInputElement("Net Income", year) 
        depreciation = self.getInputElement("Depreciation", year)
        amortization = self.getInputElement("Amortization", year)
        interest = self.getInputElement("Interest Expense", year)
        tax = self.getInputElement("Tax", year)
        
        EBITDA = netIncome + interest + tax + depreciation + amortization
        
        if EBITDA == 0:
            print("ERROR - Years to Repay Debt: denominator is zero")
            return 0
        
        return totDebt/EBITDA
        
    ## Average Interest Rate
    def averageInterestRate(self, year):
        totDebt = self.getInputElement("Total Debt", year)
        interest = self.getInputElement("Interest Expense", year)
        
        if totDebt == 0:
            print("ERROR - Average Interest Rate: Total Debt is zero")
            return 0
        
        return interest/totDebt