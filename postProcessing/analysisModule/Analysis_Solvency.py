from . import fundamentalsAnalysis

class Analysis_Solvency(fundamentalsAnalysis.FA):
    
    def analyse_solvency(self):
        print("Analysing Solvency Ratios")
        
        self.analyse_debtRatio()
        self.analyse_debtToEquityRatio()
        self.analyse_interestCoverageRatio()
        self.analyse_yearsToRepayDebt()
        self.analyse_averageInterestRate()
        
    def analyse_debtRatio(self):
        self.setQualities_row("Debt Ratio", 0.5, 4)
        self.setGrowth("Debt Ratio")
    
    def analyse_debtToEquityRatio(self):
        self.setQualities_row("Debt to Equity Ratio", 0.33, 4)
        self.setGrowth("Debt to Equity Ratio")
        
    def analyse_interestCoverageRatio(self):
        self.setQualities_row("Interest Coverage Ratio", 1, 2)
        self.setGrowth("Interest Coverage Ratio")
        
    def analyse_yearsToRepayDebt(self):
        self.setGrowth("Years to Repay Debt")
        
    def analyse_averageInterestRate(self):
        self.setQualities_row("Average Interest Rate", 0.03, 4) # 3% Below Interest Rate 
        self.setGrowth("Average Interest Rate")
