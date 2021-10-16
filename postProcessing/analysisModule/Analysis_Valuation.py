from . import fundamentalsAnalysis

class Analysis_Valuation(fundamentalsAnalysis.FA):
    
    def analyse_valuation(self):
        print("Analyising Valuation Ratios")
        
        self.analyse_priceToBook()
        self.analyse_priceToEarnings()
        
    def analyse_priceToBook(self):
        self.setQualities_row("Price to Book", 1.3, 4)
        self.setGrowth("Price to Book")
       
    def analyse_priceToEarnings(self):
        self.setQualities_row("Price to Earnings", 10, 2)
        self.setGrowth("Price to Earnings")