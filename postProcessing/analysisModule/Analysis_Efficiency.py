from . import fundamentalsAnalysis

class Analysis_Efficiency(fundamentalsAnalysis.FA):
    
    def analyse_efficiency(self):
        print("Analysing Efficiency Ratios")
        
        self.analyse_ebidtdaToCashConversion()
        self.analyse_revenueToExpenseRatio()
        
    def analyse_ebidtdaToCashConversion(self):
        self.setGrowth("EBITDA to Cash Conversion")
        
    def analyse_revenueToExpenseRatio(self):
        self.setGrowth("Revenue to Expense Ratio")