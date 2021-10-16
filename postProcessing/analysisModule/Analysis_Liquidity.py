from . import fundamentalsAnalysis 

class Analysis_Liquidity(fundamentalsAnalysis.FA):
    
    def analyse_liquidity(self):
        print("Analysing Liquidity Ratios")
        
        self.analyse_currentRatio()
        self.analyse_cashRatio()
        self.analyse_operatingCashFlowRatio()
        self.analyse_cashConversionRatio()
    
    def analyse_currentRatio(self):
        self.setQualities_row("Current Ratio", 2, 2)
        self.setGrowth("Current Ratio")
        
    def analyse_cashRatio(self):
        self.setGrowth("Cash Ratio")
        
    def analyse_operatingCashFlowRatio(self):
        self.setGrowth("Operating Cash Flow Ratio")
        
    def analyse_cashConversionRatio(self):
        self.setQualities_row("Cash Conversion Ratio", 1, 2)
        self.setGrowth("Cash Conversion Ratio")