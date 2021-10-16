from . import fundamentalsAnalysis

from . import Analysis_Valuation
from . import Analysis_Profitability
from . import Analysis_Efficiency
from . import Analysis_Liquidity
from . import Analysis_Solvency

from . import Analysis_sub_dividendPaying
from . import Analysis_sub_haveSales
from . import Analysis_sub_inventoryHolding

class sectorAnalysis_Retail(Analysis_Valuation.Analysis_Valuation, Analysis_Profitability.Analysis_Profitability, Analysis_Efficiency.Analysis_Efficiency, Analysis_Liquidity.Analysis_Liquidity, Analysis_Solvency.Analysis_Solvency, Analysis_sub_dividendPaying.Analysis_dividendPaying, Analysis_sub_haveSales.Analysis_haveSales, Analysis_sub_inventoryHolding.Analysis_inventoryHolding, fundamentalsAnalysis.FA):
    
    def analyse_retail(self):
        print("Analysing Retail's Fundamentals")
        
        self.analyse_valuation()
        self.analyse_profitability()
        self.analyse_efficiency()
        self.analyse_liquidity()
        self.analyse_solvency()
        
        self.analyse_dividendPaying()
        
        self.analyse_haveSales()
        self.analyse_inventoryHolding()