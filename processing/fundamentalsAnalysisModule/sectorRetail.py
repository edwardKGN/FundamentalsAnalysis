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

class financialData_retail(FA_Valuation_gen.valuation_gen, FA_Profitability_gen.profitability_gen, FA_Efficiency_gen.efficiency_gen, FA_Liquidity_gen.liquidity_gen, FA_Solvency_gen.solvency_gen, FA_sub_dividendPaying.dividendPaying, FA_sub_haveSales.haveSales, FA_sub_inventoryHolding.inventoryHolding, fundamentalsAnalysis.financialData_main): # Method Resolution Order (MRO) second layer that inherit from first layer must be declared prior the first layer of inheritence. 
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
    
    # Inventory Holders
    
    ## Efficiency / Activity
    - Stock Days
    - Stock Turnover
    
    ## Liquidity
    - Quick Ratio
    """
    
    def analyze_retail(self):
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