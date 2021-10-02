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

class financialData_insurance(FA_Valuation_gen.valuation_gen, FA_Profitability_gen.profitability_gen, FA_Efficiency_gen.efficiency_gen, FA_Liquidity_gen.liquidity_gen, FA_Solvency_gen.solvency_gen, FA_sub_dividendPaying.dividendPaying, FA_sub_haveSales.haveSales, FA_sub_inventoryHolding.inventoryHolding, fundamentalsAnalysis.financialData_main): # Method Resolution Order (MRO) second layer that inherit from first layer must be declared prior the first layer of inheritence. 
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
    
    # Insurance
    
    ## Profitability
    - Investment Return
    - Net Investment Income Ratio
    
    ## Efficiency / Activity
    - Loss Ratio
    - Underwriting Expense Ratio
    
    """
    
    def analyze_insurance(self):
        print("Analysis starting")
        
        self.analyzeValuation()
        self.analyzeProfitability()
        self.analyzeEfficiency()
        self.analyzeLiquidity()
        self.analyzeSolvency()
        
        self.analyzeDividend()
        
        self.analyzeSales()
        self.analyzeInventory()
    
        ## Profitability
        self.setOutput_row("Investment Return")
        self.setOutput_row("Net Investment Income Ratio")

        ## Efficiency / Activity
        self.setOutput_row("Loss Ratio")
        self.setOutput_row("Underwriting Expense Ratio")

        for year in self.getFinancialYears():
            # Profitability
            self.setOutput_element("Investment Return", year, self.investmentReturn(year))
            self.setOutput_element("Net Investment Income Ratio", year, self.netInvestmentIncomeRatio(year))

            # Efficiency / Activity 
            self.setOutput_element("Loss Ratio", year, self.lossRatio(year))
            self.setOutput_element("Underwriting Expense Ratio", year, self.underwritingExpenseRatio(year))
        
    # Unique Financial Ratios
    
    ## Profitability
    
    def investmentReturn(self, year):
        investmentIncome = self.getInputElement("Investment Income", year)
        investmentExpense = self.getInputElement("Investment Expense", year)
        
        netInvestmentIncome = investmentIncome - investmentExpense
        
        gainInvestmentAssets = self.getInputElement("Gains on Investment Assets", year)
        lossInvestmentAssets = self.getInputElement("Losses on Investment Assets", year)
        
        netGainsInvestmentAssets = gainInvestmentAssets - lossInvestmentAssets
        
        investmentAssets = self.getInputElement("Investment Assets", year)
        
        if investmentAssets == 0:
            print("ERROR - Investment Assets: denominator is zero")
            return 0
        
        return (netInvestmentIncome + netGainsInvestmentAssets)/investmentAssets
    
    def netInvestmentIncomeRatio(self, year):
        investmentIncome = self.getInputElement("Investment Income", year)
        investmentExpense = self.getInputElement("Investment Expense", year)
        
        netInvestmentIncome = investmentIncome - investmentExpense
        
        netPremiumsEarned = self.getInputElement("Net Premiums Earned", year)
        
        if netPremiumsEarned == 0:
            print("ERROR - Net Premiums Earned: denominator is zero")
            return 0
        
        return (netInvestmentIncome)/netPremiumsEarned
    
    ## Efficiency / Activity
    
    def lossRatio(self, year):
        netClaims = self.getInputElement("Net Claims", year)
        netPremiumsEarned = self.getInputElement("Net Premiums Earned", year)
        
        if netPremiumsEarned == 0:
            print("ERROR - Loss Ratio: denominator is zero")
            return 0
        
        return netClaims/netPremiumsEarned
    
    def underwritingExpenseRatio(self, year):
        commExp = self.getInputElement("Commission Expense", year)
        interestExp = self.getInputElement("Interest Expense", year)
        investmentExp = self.getInputElement("Investment Expenses", year)
        mgmtExp = self.getInputElement("Management Expense", year)
        
        underWritingExp = commExp + interestExp + investmentExp + mgmtExp
        
        netPremiumsEarned = self.getInputElement("Net Premiums Earned", year)
        
        if netPremiumsEarned == 0:
            print("ERROR - Loss Ratio: denominator is zero")
            return 0
        
        return underWritingExp/netPremiumsEarned         