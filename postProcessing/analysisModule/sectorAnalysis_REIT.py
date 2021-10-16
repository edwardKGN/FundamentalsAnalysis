from . import fundamentalsAnalysis

from . import Analysis_Valuation
from . import Analysis_Profitability
from . import Analysis_Efficiency
from . import Analysis_Liquidity
from . import Analysis_Solvency

from . import Analysis_sub_dividendPaying
from . import Analysis_sub_haveSales
from . import Analysis_sub_inventoryHolding

class sectorAnalysis_REIT(Analysis_Valuation.Analysis_Valuation, Analysis_Profitability.Analysis_Profitability, Analysis_Efficiency.Analysis_Efficiency, Analysis_Liquidity.Analysis_Liquidity, Analysis_Solvency.Analysis_Solvency, Analysis_sub_dividendPaying.Analysis_dividendPaying, Analysis_sub_haveSales.Analysis_haveSales, Analysis_sub_inventoryHolding.Analysis_inventoryHolding, fundamentalsAnalysis.FA):
    
    def analyse_REIT(self):
        print("Analysing REIT's Fundamentals")
        
        self.analyse_efficiency()
        self.analyse_liquidity()
        self.analyse_solvency()
        
        self.analyse_dividendPaying()
        self.analyse_haveSales()
        self.analyse_inventoryHolding()
        
        self.analyse_FFO()
        self.analyse_AFFO()
        
        self.analyse_netAssetValue()
        self.analyse_priceToFFO()
        self.analyse_priceToAFFO()
        self.analyse_affoYield()
        self.analyse_capitalizationRate()
        self.analyse_managementExpenseToProfitRatio()
    
    """
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
    """
    
    def analyse_FFO(self):
        self.setGrowth("FFO")
        
    def analyse_AFFO(self):
        self.setGrowth("AFFO")
        
    def analyse_netAssetValue(self):
        self.setGrowth("Net Asset Value")
        
    def analyse_priceToFFO(self):
        self.setGrowth("Price to FFO Ratio")
        
    def analyse_priceToAFFO(self):
        self.setGrowth("Price to AFFO Ratio")
        
    def analyse_affoYield(self):
        self.setGrowth("AFFO Yield")
        
    def analyse_capitalizationRate(self):
        self.setGrowth("Capitalization Rate")
        
    def analyse_managementExpenseToProfitRatio(self):
        self.setGrowth("Management Expense to Profit Ratio")