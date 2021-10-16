from . import fundamentalsAnalysis

from . import Analysis_Valuation
from . import Analysis_Profitability
from . import Analysis_Efficiency
from . import Analysis_Liquidity
from . import Analysis_Solvency

from . import Analysis_sub_dividendPaying
from . import Analysis_sub_haveSales
from . import Analysis_sub_inventoryHolding

class sectorAnalysis_Insurance(Analysis_Valuation.Analysis_Valuation, Analysis_Profitability.Analysis_Profitability, Analysis_Efficiency.Analysis_Efficiency, Analysis_Liquidity.Analysis_Liquidity, Analysis_Solvency.Analysis_Solvency, Analysis_sub_dividendPaying.Analysis_dividendPaying, Analysis_sub_haveSales.Analysis_haveSales, Analysis_sub_inventoryHolding.Analysis_inventoryHolding, fundamentalsAnalysis.FA):
    
    def analyse_insurance(self):
        print("Analysing Insurance's Fundamentals")
        
        self.analyse_valuation()
        self.analyse_profitability()
        self.analyse_efficiency()
        self.analyse_liquidity()
        self.analyse_solvency()
        
        self.analyse_dividendPaying()
        
        self.analyse_haveSales()
        self.analyse_inventoryHolding()
        
        self.analyse_investmentReturn()
        self.analyse_netInvestmentIncomeRatio()
        self.analyse_lossRatio()
        self.analyse_underwritingExpenseRatio()
        
        """
        # Insurance
    
        ## Profitability
        - Investment Return
        - Net Investment Income Ratio
    
        ## Efficiency / Activity
        - Loss Ratio
        - Underwriting Expense Ratio
    
        """
        
    def analyse_investmentReturn(self):
        self.setGrowth("Investment Return")
            
    def analyse_netInvestmentIncomeRatio(self):
        self.setGrowth("Net Investment Income Ratio")
            
    def analyse_lossRatio(self):
        self.setGrowth("Loss Ratio")
        
    def analyse_underwritingExpenseRatio(self):
        self.setGrowth("Underwriting Expense Ratio")
            
       