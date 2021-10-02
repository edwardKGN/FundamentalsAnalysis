from . import fundamentalsAnalysis
from . import FA_Valuation_gen
from . import FA_Profitability_gen
from . import FA_Efficiency_gen
from . import FA_Liquidity_gen
from . import FA_Solvency_gen # to include in inheritance list, FA_Solvency_gen.solvency_gen
from . import FA_sub_dividendPaying

# Not Expected to be present due to nature of business.
from . import FA_sub_haveSales 
from . import FA_sub_inventoryHolding

class financialData_REIT(FA_Valuation_gen.valuation_gen, FA_Profitability_gen.profitability_gen, FA_Efficiency_gen.efficiency_gen, FA_Liquidity_gen.liquidity_gen, FA_Solvency_gen.solvency_gen, FA_sub_dividendPaying.dividendPaying, FA_sub_haveSales.haveSales, FA_sub_inventoryHolding.inventoryHolding, fundamentalsAnalysis.financialData_main): # Method Resolution Order (MRO) second layer that inherit from first layer must be declared prior the first layer of inheritence. 
    
    """
    # Financial Ratios Implemented
    
    # General
        
    ## Efficiency
    - Revenue to Expense Ratio
        
    ## Liquidity
    - Current Ratio
    - Cash Ratio
    - Operating Cash Flow Ratio
    - Cash Conversion Ratio
        
    ## Leverage / Solvency / Gearing
    - Debt Ratio
    - Debt to Equity Ratio
        
    - Average Interest Rate
        
    # Unique
        
    ## Derived
    - Funds from Operations (FFO)
    - Adjusted Funds from Operations (AFFO)
        
    ## Valuation
    - Net Asset Value
    - Price to FFO
    - Price to AFFO
        
    ## Profitability
    - AFFO Yield
    - Capitalization Rate
        
    ## Efficiency
    - Management Expense to Profit Ratio
        
    # Dividend 
        
    ## Profitability
    - Dividend Yield
        
    ## Liquidity
    - Dividend Coverage
    - Dividend Payout Ratio
    """
    
    def analyze_REIT(self):
        
        self.analyzeEfficiency()
        self.analyzeLiquidity()
        self.analyzeSolvency()
        
        self.analyzeDividend()
        
        # Unique
        ## Derived
        self.setOutput_row("FFO")
        self.setOutput_row("AFFO")
        
        ## Valuation
        self.setOutput_row("Net Asset Value")
        self.setOutput_row("Price to FFO Ratio")
        self.setOutput_row("Price to AFFO Ratio")
        
        ## Profitability
        self.setOutput_row("AFFO Yield")
        self.setOutput_row("Capitalization Rate")
        
        ## Efficiency
        self.setOutput_row("Management Expense to Profit Ratio")
        
        self.setFinancialYears()
        
        for year in self.getFinancialYears():
            
            # Unique 
            
            ## Derived
            self.setOutput_element("FFO", year, self.FFO(year))
            self.setOutput_element("AFFO", year, self.AFFO(year))
            
            ## Valuation
            self.setOutput_element("Net Asset Value", year, self.netAssetValue(year))
            self.setOutput_element("Price to FFO Ratio", year, self.priceToFFO(year))
            self.setOutput_element("Price to AFFO Ratio", year, self.priceToAFFO(year))
            
            ## Profitability
            self.setOutput_element("AFFO Yield", year, self.AFFOyield(year))
            self.setOutput_element("Capitalization Rate", year, self.capitalizationRate(year))
            
            ## Efficiency
            self.setOutput_element("Management Expense to Profit Ratio", year, self.managementExToProfitRatio(year))
            
    # Unique Financial Ratios
    
    ## Derived Fund From Operations
    
    def FFO(self, year): # Funds from Operations
        netIncome = self.getInputElement("Net Income", year)
        depreciation = self.getInputElement("Depreciation", year)
        amortization = self.getInputElement("Amortization", year)
        propSalesLoss = self.getInputElement("Losses on Property Sales", year)
        propSalesGain = self.getInputElement("Gains on Property Sales", year)
        interestIncome = self.getInputElement("Interest Income", year)
        otherIncome = self.getInputElement("Other Income", year)
        
        return netIncome + depreciation + amortization + propSalesLoss - (propSalesGain + interestIncome + otherIncome)
        
    def AFFO(self, year): # Adjusted Funds from Operations
        capEx = self.getInputElement("Capital Expenditure", year)
        rentIncreases = self.getInputElement("Rent Increases", year)
        propOpsEx = self.getInputElement("Property Operating Expenses", year)
        
        return self.FFO(year) + rentIncreases - capEx - propOpsEx
    
    ## Valuation
    
    def netAssetValue(self, year):
        totAssets = self.getInputElement("Total Assets", year)
        totLiab = self.getInputElement("Total Liabilities", year)
        
        netAsset = (totAssets - totLiab) * 1000 # Convert to Currency
        
        outstandingShares = self.getInputElement("Outstanding Shares", year)
        
        if outstandingShares == 0:
            print("ERROR - Net Asset Value: Outstanding Shares is zero")
            return 0
        
        return netAsset/outstandingShares
    
    def priceToFFO(self, year):
        unitPrice = self.getInputElement("Unit Price (Currency)", year)
        outstandingShares = self.getInputElement("Outstanding Shares", year)
        
        marketCap = (unitPrice * outstandingShares)/1000 # Currency -> Currency '000 <Standard Unit>
        
        if self.FFO(year) == 0:
            print("ERROR - Price to FFO: FFO is zero")
            return 0
        
        return marketCap/(self.FFO(year))
        
    def priceToAFFO(self, year):
        unitPrice = self.getInputElement("Unit Price (Currency)", year)
        outstandingShares = self.getInputElement("Outstanding Shares", year)
        
        marketCap = (unitPrice * outstandingShares)/1000 # Currency -> Currency '000 <Standard Unit>
        
        if self.AFFO(year) == 0:
            print("ERROR - FFO to AFFO: AFFO is zero")
            return 0
        
        return marketCap/(self.AFFO(year))
    
    ## Profitability
    
    def AFFOyield(self, year):
        unitPrice = self.getInputElement("Unit Price (Currency)", year)
        outstandingShares = self.getInputElement("Outstanding Shares", year)
        
        marketCap = (unitPrice * outstandingShares)/1000 # Currency -> Currency '000 <Standard Unit>
        
        if marketCap == 0:
            print("Error - AFFO yield: Market capitalization is zero")
            return 0
        
        return (self.AFFO(year))/marketCap
    
    def capitalizationRate(self, year):
        unitPrice = self.getInputElement("Unit Price (Currency)", year)
        outstandingShares = self.getInputElement("Outstanding Shares", year)
        
        marketCap = (unitPrice * outstandingShares)/1000 # Currency -> Currency '000 <Standard Unit>
        
        if marketCap == 0:
            print("Error - Capitalization Rate: Market capitalization is zero")
            return 0
        
        netOpIncome = self.getInputElement("Net Operating Income", year)
        
        return netOpIncome/marketCap
    
    ## Efficiency / Activity
        
    def managementExToProfitRatio(self, year):
        netIncome = self.getInputElement("Net Income", year)
        managementEx = self.getInputElement("Management Expense", year)
        
        if netIncome == 0:
            print("ERROR - Management Expense to Profit Ratio: Profit (After Tax) is zero")
            return 0
        
        return managementEx/netIncome
    
    ## Liquidity

    # N/A
    
    ## Solvency / Gearing
    
    # N/A