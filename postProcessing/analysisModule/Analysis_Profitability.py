from . import fundamentalsAnalysis

class Analysis_Profitability(fundamentalsAnalysis.FA):
    
    def analyse_profitability(self):
        print("Analyse Profitability Ratios")
        
        self.analyse_returnOnEquity()
        self.analyse_returnOnCapitalEmployed()
        self.analyse_ebitdaToRevenueRatio()
    
    def analyse_returnOnEquity(self):
        self.setGrowth("Return on Equity")
    
    def analyse_returnOnCapitalEmployed(self):
        self.setGrowth("Return on Capital Employed")
    
    def analyse_ebitdaToRevenueRatio(self):
        self.setGrowth("EBITDA to Revenue Ratio")
    