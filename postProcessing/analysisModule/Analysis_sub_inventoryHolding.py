from . import fundamentalsAnalysis

class Analysis_inventoryHolding(fundamentalsAnalysis.FA):
    
    def analyse_inventoryHolding(self):
        print("Checking for Inventory Ratios")
        
        if (self.df_input[self.df_input.columns[0]] == "Stock Days").any() == True: # Check if Stock data is present.
            print("Analysing Inventory Ratios")
            
            self.analyse_stockDays()
            self.analyse_stockTurnover()
            self.analyse_quickRatio()
        
    """
    List of Financial Ratios
    
    # Effectiveness
    - Stock Days
    - Stock Turnover
    
    # Liquidity
    - Quick Ratio
    """
            
    def analyse_stockDays(self):
        self.setGrowth("Stock Days")
        
    def analyse_stockTurnover(self):
        self.setGrowth("Stock Turnover")
     
    def analyse_quickRatio(self):
        self.setGrowth("Quick Ratio")