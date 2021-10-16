from . import financialRatios

class dividendPaying(financialRatios.financialData_main):
    
    """
    List of Financial Ratios
    
    # Profitability
    - Dividend Yield
    
    # Liquidity
    - Dividend Coverage
    - Dividend Payout Ratio
    """
    
    # Main Analyzer
    def analyzeDividend(self):
        # If Have Dividend Data, calculate Dividend Specific data. Based on the set input.
        if (self.df_input[self.df_input.columns[0]] == "Gross Dividend Payout (Currency per Unit)").any() == True: # Will return True if there is a matching value
            
            print("Dividend Data found")
            
            # Set Up Rows for Data to be Filled In
            self.setOutput_row("Dividend Yield")
            self.setOutput_row("Dividend Coverage Ratio")
            self.setOutput_row("Dividend Payout Ratio")
            
            self.setFinancialYears()

            # Calculate Relevant Data
            for year in self.getFinancialYears():                
                self.setOutput_element("Dividend Yield", year, self.dividendYield(year))
                
                self.setOutput_element("Dividend Coverage Ratio", year, self.dividendCoverage(year))
                self.setOutput_element("Dividend Payout Ratio", year, self.dividendPayoutRatio(year))
        else:
            print("No Dividend Data available")
    
    # Unique
    
    ## Profitability
    
        ## Dividend Yield
    def dividendYield(self, year):
        grossDivPayout = self.getInputElement("Gross Dividend Payout (Currency per Unit)", year)
        unitPrice = self.getInputElement("Unit Price (Currency)", year)
        
        if unitPrice == 0:
            print("ERROR - Dividend Yield: Denominator is zero")
            return 0.0
        
        return grossDivPayout/unitPrice
    
    ## Liquidity
    
        ## Dividend Coverage
    def dividendCoverage(self, year):
        netIncome = self.getInputElement("Net Income", year)
        
        grossDivPayout = self.getInputElement("Gross Dividend Payout (Currency per Unit)", year)
        outstandingShares = self.getInputElement("Outstanding Shares", year)
        
        totalDividendPayout = (grossDivPayout * outstandingShares)/1000 # Currency -> Currency '000 <Standard Unit>
        
        if totalDividendPayout == 0:
            print("ERROR - Dividend Coverage: Denominator is zero")
            return 0.0
        
        return netIncome/totalDividendPayout
    
        ## Dividend Payout Ratio
    def dividendPayoutRatio(self, year):
        netIncome = self.getInputElement("Net Income", year)
        
        grossDivPayout = self.getInputElement("Gross Dividend Payout (Currency per Unit)", year)
        outstandingShares = self.getInputElement("Outstanding Shares", year)
        
        totalDividendPayout = (grossDivPayout * outstandingShares)/1000 # Currency -> Currency '000 <Standard Unit>
        
        if netIncome == 0:
            print("ERROR - Dividend Payout Ratio: Denominator is zero")
            return 0.0
        
        return totalDividendPayout/netIncome 