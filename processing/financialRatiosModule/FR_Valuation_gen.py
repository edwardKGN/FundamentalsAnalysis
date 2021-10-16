from . import financialRatios

class valuation_gen(financialRatios.financialData_main):
                
    """
    List of Financial Ratios
    
    # Valuation
    - Price to Book
    - Price to Earnings
    """
    
    def analyzeValuation(self): # Equivalent to Run All  
        print("Analyzing Valuation")
        
        # Set Up Rows to Fill In Key information
        self.setOutput_row("Price to Book")
        self.setOutput_row("Price to Earnings")
        
        self.setFinancialYears()
        
        for year in self.getFinancialYears(): # Return Financial Ratios as fractions
            #print(year)
            
            # Valuation Analysis
            #print("Price to Book: ", self.priceToBook(year))
            #print("Price to Earnings: ", self.priceToEarnings(year))
            self.setOutput_element("Price to Book", year, self.priceToBook(year))
            self.setOutput_element("Price to Earnings", year, self.priceToEarnings(year))
    
    # Financial Ratios
    ## Price to Book
    def priceToBook(self, year):
        unitPrice = self.getInputElement("Unit Price (Currency)", year) 
        outstandingShares = self.getInputElement("Outstanding Shares", year)
        
        marketCap = (unitPrice * outstandingShares)/1000 # Currency -> Currency '000 <Standard Unit>
        
        #print("Unit Price (Currency): ", unitPrice, ", Outstanding Shares: ", outstandingShares, ", Market Cap.: ", marketCap)  
        
        totAssets = self.getInputElement("Total Assets", year) 
        intAssets = self.getInputElement("Intangible Assets", year) 
        totLiabilities = self.getInputElement("Total Liabilities", year) 
        
        bookVal = totAssets - intAssets - totLiabilities
        
        #print("Book Value: ", bookVal)
        
        if bookVal == 0:
            print("ERROR - Price to Book: denominator is zero")
            return 0.0
        
        return marketCap/bookVal
    
    ## Price to Earnings
    def priceToEarnings(self, year):
        unitPrice = self.getInputElement("Unit Price (Currency)", year)
        outstandingShares = self.getInputElement("Outstanding Shares", year)
        
        netIncome = self.getInputElement("Net Income", year)
        
        marketCap = (unitPrice * outstandingShares)/1000 # Currency -> Currency '000 <Standard Unit>
        
        if netIncome == 0:
            print("ERROR - Price to Earnings: denominator is zero")
            return 0.0
        
        return marketCap/netIncome