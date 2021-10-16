from . import fundamentalsAnalysis

class Analysis_haveSales(fundamentalsAnalysis.FA):
    
    def analyse_haveSales(self):
        print("Checking for Sales Ratios")
        
        if (self.df_input[self.df_input.columns[0]] == "Gross Margin").any() == True: # Will return True if there is a matching value
            print("Analyising Sales Ratios")
            
            self.analyse_grossMargin()
            self.analyse_capitalProductivity()
            self.analyse_cogsPerSale()
            self.analyse_workingCapitalProductivity()
            self.analyse_tradeDebtorsProductivity()
            self.analyse_tradeDebtorsDays()
            self.analyse_tradeCreditorsProductivity()
            self.analyse_tradeCreditorsDays()
            self.analyse_fixedAssetsProductivity()

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
    
    - Trade Creditors Productivity
    - Trade Creditors Days
    
    - Fixed Assets Productivity
    """
    
    def analyse_grossMargin(self):
        self.setGrowth("Gross Margin")
    
    def analyse_capitalProductivity(self):
        self.setGrowth("Capital Productivity")
        
    def analyse_cogsPerSale(self):
        self.setGrowth("COGS per Sale")
        
    def analyse_workingCapitalProductivity(self):
        self.setGrowth("Working Capital Productivity")
        
    def analyse_tradeDebtorsProductivity(self):
        self.setGrowth("Trade Debtors Productivity")
        
    def analyse_tradeDebtorsDays(self):
        self.setGrowth("Trade Debtors Days")
        
    def analyse_tradeCreditorsProductivity(self):
        self.setGrowth("Trade Creditors Productivity")
        
    def analyse_tradeCreditorsDays(self):
        self.setGrowth("Trade Creditors Days")
        
    def analyse_fixedAssetsProductivity(self):
        self.setGrowth("Fixed Assets Productivity")
        