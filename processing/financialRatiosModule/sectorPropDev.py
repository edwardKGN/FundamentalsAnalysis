from . import financialRatios
from . import FR_Valuation_gen
from . import FR_Profitability_gen
from . import FR_Efficiency_gen
from . import FR_Liquidity_gen
from . import FR_Solvency_gen # to include in inheritance list, FA_Solvency_gen.solvency_gen
from . import FR_sub_dividendPaying

# Not Expected to be present due to nature of business.
from . import FR_sub_haveSales 
from . import FR_sub_inventoryHolding

class financialData_propDev(FR_Valuation_gen.valuation_gen, FR_Profitability_gen.profitability_gen, FR_Efficiency_gen.efficiency_gen, FR_Liquidity_gen.liquidity_gen, FR_Solvency_gen.solvency_gen, FR_sub_dividendPaying.dividendPaying, FR_sub_haveSales.haveSales, FR_sub_inventoryHolding.inventoryHolding, financialRatios.financialData_main): # Method Resolution Order (MRO) second layer that inherit from first layer must be declared prior the first layer of inheritence. 
    """
    # Financial Ratios Implemented
        
    # General
    ## Valuation
    - Price to Book
    - Price to Earnings
        
    ## Profitability
    - Return on Equity
    - Return on Capital Employed
    - Gross Margin
    - EBITDA to Revenue Ratio
        
    ## Efficiency / Activity
    - EBITDA to Cash Conversion
    
    - Revenue to Expense Ratio
    - Capital Productivity

    - COGS per Sale

    - Working Capital Productivity

    - Trade Debtor Productivity
    - Trade Debtor Days

    - Trade Creditor Productivity
    - Trade Creditor Days

    - Fixed Assets Productivity
        
    ## Liquidity
    - Current Ratio
    - Cash Ratio
    - Operating Cash Flow Ratio
    - Cash Conversion Ratio
        
    ## Leverage / Solvency / Gearing
    - Debt Ratio
    - Debt to Equity Ratio
        
    - Interest Coverage Ratio
        
    - Years to Repay Debt
        
    - Average Interest Rate
        
    # Dividend 
        
    ## Profitability
    - Dividend Yield
        
    ## Liquidity
    - Dividend Coverage
    - Dividend Payout Ratio
    """
    
    def analyze_propDev(self):
        print("Analysis starting")
        
        self.analyzeValuation()
        self.analyzeProfitability()
        self.analyzeEfficiency()
        self.analyzeLiquidity()
        self.analyzeSolvency()
        
        self.analyzeDividend()
        
        self.analyzeSales()
        self.analyzeInventory()

    # Unique Financial Ratios
    # N/A