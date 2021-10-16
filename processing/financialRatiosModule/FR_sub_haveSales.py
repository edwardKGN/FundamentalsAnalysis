from . import financialRatios

class haveSales(financialRatios.financialData_main): # Declared as Sales in Financial Report
    
    """
    List of Financial Ratios
    
    # Profitability
    - Gross Margin
    
    # Efficiency
    - Capital Productivity
    
    - COGS per Sale
    
    - Working Capital Productivity
    
    - Trade Debtors Productivity
    - Trade Debtors Days
    
    - Trade Creditor Productivity
    - Trade Creditor Days
    
    - Fixed Assets Productivity
    """
    
    def analyzeSales(self):
        print("Analyzing Sales-related Financial Ratios") # Mostly related to effectiveness
        
        if (self.df_input[self.df_input.columns[0]] == "Sales").any() == True: # Check if Sales data is present.
            
            print("Sales data available.")
            
            self.setFinancialYears() # Input Financial Years data
            
            self.setOutput_row("Gross Margin")
        
            self.setOutput_row("Capital Productivity")
        
            self.setOutput_row("COGS per Sale")
        
            self.setOutput_row("Working Capital Productivity")
        
            self.setOutput_row("Trade Debtors Productivity")
            self.setOutput_row("Trade Debtors Days")
        
            self.setOutput_row("Trade Creditors Productivity")
            self.setOutput_row("Trade Creditors Days")
        
            self.setOutput_row("Fixed Assets Productivity")
        
            for year in self.getFinancialYears(): # Return Financial Ratios as fractions
                self.setOutput_element("Gross Margin", year, self.grossMargin(year))
                    
                self.setOutput_element("Capital Productivity", year, self.capitalProductivity(year))
            
                self.setOutput_element("COGS per Sale", year, self.cogsPerSale(year))
            
                self.setOutput_element("Working Capital Productivity", year, self.workingCapitalProductivity(year))
            
                self.setOutput_element("Trade Debtors Productivity", year, self.tradeDebtorProductivity(year))
                self.setOutput_element("Trade Debtors Days", year, self.tradeDebtorDays(year))
            
                self.setOutput_element("Trade Creditors Productivity", year, self.tradeCreditorProductivity(year))
                self.setOutput_element("Trade Creditors Days", year, self.tradeCreditorDays(year))
            
                self.setOutput_element("Fixed Assets Productivity", year, self.fixedAssetsProductivity(year))
        else:
            print("No Sales data available.")
    
    # Profitability
    ## Gross Margin
    def grossMargin(self, year):
        revenue = self.getInputElement("Revenue", year)
        COGS = self.getInputElement("Cost of Goods Sold", year) # Cost of Goods Sold
        
        grossProfit = revenue - COGS
        
        sales = self.getInputElement("Sales", year)
        
        if sales == 0:
            print("ERROR - Gross Margin: denominator is zero")
            return 0
        
        return grossProfit/sales
            
    ## Capital Productivity
    def capitalProductivity(self, year):
        operatingProfit = self.getInputElement("Operating Profit", year)
        sales = self.getInputElement("Sales" , year)
        
        if sales == 0:
            print("ERROR - Capital Productivity: denominator is zero")
            return 0
        
        return operatingProfit/sales
   
    ## COGS per Sale
    def cogsPerSale(self, year):
        COGS = self.getInputElement("Cost of Goods Sold", year) # Cost of Goods Sold
        
        sales = self.getInputElement("Sales" , year)
        
        if sales == 0:
            print("ERROR - Capital Productivity: denominator is zero")
            return 0
        
        return COGS/sales
   
    ## Working Capital Productivity
    def workingCapitalProductivity(self, year):
        sales = self.getInputElement("Sales" , year)
        
        currAssets = self.getInputElement("Current Assets", year)
        currLiabilities = self.getInputElement("Current Liabilities", year)
        
        workingCap = currAssets - currLiabilities
        
        if workingCap == 0:
            print("ERROR - Working Capital Producitivity: denominator is zero")
            return 0
        
        return sales/workingCap
    
    ## Trade Debtor Productivity
    def tradeDebtorProductivity(self, year):
        sales = self.getInputElement("Sales" , year)
        
        tradeDebtors = self.getInputElement("Trade Debtors", year)
        
        if tradeDebtors == 0:
            print("ERROR - Trade Debtors Productivity: denominator is zero")
            return 0
        
        return sales/tradeDebtors
    
    ## Trade Debtor Days
    def tradeDebtorDays(self, year):
        tradeDebtors = self.getInputElement("Trade Debtors", year)
        
        sales = self.getInputElement("Sales" , year)
        
        if sales == 0:
            print("ERROR - Trade Debtors Days: denominator is zero")
            return 0
        
        return tradeDebtors/sales * 365
    
    ## Trade Creditor Productivity
    def tradeCreditorProductivity(self, year):
        sales = self.getInputElement("Sales" , year)
        
        tradeCreditors = self.getInputElement("Trade Creditors", year)
        
        if tradeCreditors == 0:
            print("ERROR - Trade Creditors Productivity: denominator is zero")
            return 0
        
        return sales/tradeCreditors

    ## Trade Creditor Days
    def tradeCreditorDays(self, year):
        tradeCreditors = self.getInputElement("Trade Creditors", year)
        
        sales = self.getInputElement("Sales" , year)
        
        if sales == 0:
            print("ERROR - Trade Creditors Days: denominator is zero")
            return 0
        
        return tradeCreditors/sales * 365   
        
    ## Fixed Asset Productivity
    def fixedAssetsProductivity(self, year):
        sales = self.getInputElement("Sales" , year)
        fixedAssets = self.getInputElement("Fixed Assets", year)
        
        if fixedAssets == 0:
            print("ERROR - Fixed Assets Productivity: denominator is zero")
            return 0
        
        return sales/fixedAssets      