from . import fundamentalsAnalysis

class Analysis_dividendPaying(fundamentalsAnalysis.FA):
    
    def analyse_dividendPaying(self):
        print("Checking for Dividend Paying Ratios")
        
        # Check for dividend Yield presence in dataframe
        if (self.df_input[self.df_input.columns[0]] == "Dividend Yield").any() == True: # Will return True if there is a matching value
            print("Analyising Dividend Paying Ratios")
        
            self.analyse_dividendYield()
            self.analyse_dividendCoverage()
            self.analyse_dividendPayoutRatio()
        
    def analyse_dividendYield(self):
        self.setQualities_row("Dividend Yield", 0.03, 2) # >= 3% 
        self.setGrowth("Dividend Yield")
        
    def analyse_dividendCoverage(self):
        self.setQualities_row("Dividend Coverage Ratio", 1, 2) # >= 1 
        self.setGrowth("Dividend Coverage Ratio")
        
    def analyse_dividendPayoutRatio(self):
        self.setQualities_row("Dividend Payout Ratio", 1, 4) # <= 1
        self.setGrowth("Dividend Payout Ratio")