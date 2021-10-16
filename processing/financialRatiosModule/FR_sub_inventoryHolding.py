from . import financialRatios

class inventoryHolding(financialRatios.financialData_main): # Often Declared as "Stock" in Financial Reports
    
    """
    List of Financial Ratios
    
    # Effectiveness
    - Stock Days
    - Stock Turnover
    
    # Liquidity
    - Quick Ratio
    """
    
    # Main Analyzer
    def analyzeInventory(self):
        print("Analyze Inventory Holding")
        
        if (self.df_input[self.df_input.columns[0]] == "Stock").any() == True: # Check if Stock data is present.
            print("Stock data found.")
        
            self.setOutput_row("Stock Days")
            self.setOutput_row("Stock Turnover")
        
            self.setOutput_row("Quick Ratio")
        
            self.setFinancialYears()
        
            for year in self.getFinancialYears(): # Return Financial Ratios as fractions
                self.setOutput_element("Stock Days", year, self.stockDays(year))
                self.setOutput_element("Stock Turnover", year, self.stockTurnover(year))
            
                self.setOutput_element("Quick Ratio", year, self.quickRatio(year))
        else:
            print("No Stock data found.")
    
    ## Efficicency
    
    ## Stock Days
    def stockDays(self, year):
        stock = self.getInputElement("Stock", year)
        COGS = self.getInputElement("Cost of Goods Sold", year) # Cost of Goods Sold
        
        if COGS == 0:
            print("ERROR - Stock Days: denominator is zero")
            return 0
        
        return stock/COGS * 365
    
    ## Stock Turnover
    def stockTurnover(self, year):
        sales = self.getInputElement("Sales" , year)
        stock = self.getInputElement("Stock", year)
        
        if stock == 0:
            print("ERROR - Stock Turnover: denominator is zero")
            return 0
            
        return sales/stock
    
    ## Liquidity
    
    ## Quick Ratio
    def quickRatio(self, year):
        curAssets = self.getInputElement("Current Assets", year)
        stock = self.getInputElement("Stock", year)
        curLiabilities = self.getInputElement("Current Liabilities", year)
        
        if curLiabilities == 0:
            print("ERROR - Quick Ratio: denominator is zero")
            return 0.0
        
        return (curAssets - stock)/curLiabilities