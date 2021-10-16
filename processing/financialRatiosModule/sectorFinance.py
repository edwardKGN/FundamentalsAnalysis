from . import financialRatios
from . import FR_Valuation_gen
from . import FR_Profitability_gen
from . import FR_Efficiency_gen
from . import FR_Liquidity_gen
# from . import FR Solvency_gen # to include in inheritance list, FR_Solvency_gen.solvency_gen
from . import FR_sub_dividendPaying

# Not Expected to be present due to nature of business.
from . import FR_sub_haveSales 
from . import FR_sub_inventoryHolding

class financialData_finance(FR_Valuation_gen.valuation_gen, FR_Profitability_gen.profitability_gen, FR_Efficiency_gen.efficiency_gen, FR_Liquidity_gen.liquidity_gen, FR_sub_dividendPaying.dividendPaying, FR_sub_haveSales.haveSales, FR_sub_inventoryHolding.inventoryHolding, financialRatios.financialData_main):
    
    """
    # Financial Ratios Implemented
        
    # General
        
    ## Valuation
    - Price to Book
    - Price to Earnings
        
    ## Profitability
    - Return on Equity
    - Return on Capital Employed
    - EBITDA to Revenue
        
    ## Efficiency / Activity
    - EBITDA to Cash Conversion
    - Revenue to Expense Ratio
            
    ## Liquidity
    - Current Ratio
    - Cash Ratio
    - Operating Cash Flow Ratio
    - Cash Conversion Ratio

    # Dividend 
        
    ## Profitability
    - Dividend Yield
        
    ## Liquidity
    - Dividend Coverage
    - Dividend Payout Ratio
    
    # Unique
        
    ## Profitability
    - Net Interest Margin
    - Net Non-Interest Margin
    - Return on Assets
    - CASA Ratio
    - Net Bank Operating Margin
    - Net Profit Margin
    - Asset Utilization
        
    ## Efficiency / Activity
    - Efficiency Ratio
    - Operating Efficiency Ratio
        
    ## Liquidity
    - Credit to Deposit
        
    ## Leverage / Solvency / Gearing
    - Leverage Ratio
    - CET1 Ratio
    - Loans to Assets
    - Capital Adequacy
    - Bad Loan Ratio
    - Loan Loss Provision Coverage Ratio
    """
    
    def analyze_sectorFinance(self):
        print("Analysis starting")
        
        self.analyzeValuation()
        self.analyzeProfitability()
        self.analyzeEfficiency()
        self.analyzeLiquidity()
        # self.analyzeSolvency() # Debt is not part of Financing Business, Unique calculations required to account for loaning instead
        
        self.analyzeDividend()
        
        self.analyzeSales()
        self.analyzeInventory()
        
        self.setFinancialYears()
        
        # Unique Financial Ratios 
        ## Profitability
        
        self.setOutput_row("Net Interest Margin")
        self.setOutput_row("Net Non-Interest Margin")
        self.setOutput_row("Return on Assets")
        self.setOutput_row("CASA Ratio")
        self.setOutput_row("Net Bank Operating Margin")
        self.setOutput_row("Net Profit Margin")
        self.setOutput_row("Asset Utilization")
        
        ## Efficiency / Activity
        
        self.setOutput_row("Efficiency Ratio")
        self.setOutput_row("Operating Efficiency Ratio")
        
        ## Liquidity
        
        self.setOutput_row("Credit to Deposit Ratio")
        
        ## Leverage / Gearing / Solvency
        
        self.setOutput_row("Leverage Ratio")
        self.setOutput_row("CET-1 Ratio")
        self.setOutput_row("Loans to Assets Ratio")
        self.setOutput_row("Capital Adequacy Ratio")
        self.setOutput_row("Bad Loan Ratio")
        self.setOutput_row("Loan Loss Provision Coverage Ratio")
           
        for year in self.getFinancialYears():
            # Unique
            
            ## Profitability
            self.setOutput_element("Net Interest Margin", year, self.netInterestMargin(year))
            self.setOutput_element("Net Non-Interest Margin", year, self.netNonInterestMargin(year))
            self.setOutput_element("Return on Assets", year, self.ROA(year))
            self.setOutput_element("CASA Ratio", year, self.casaRatio(year))
            self.setOutput_element("Net Bank Operating Margin", year, self.netBankOperatingMargin(year))
            self.setOutput_element("Net Profit Margin", year, self.netProfitMargin(year))
            self.setOutput_element("Asset Utilization", year, self.assetUtilization(year))
            
            ## Efficiency / Activity
            self.setOutput_element("Efficiency Ratio", year, self.efficiencyRatio(year))
            self.setOutput_element("Operating Efficiency Ratio", year, self.operatingEfficiencyRatio(year))
            
            ## Liquidity
            self.setOutput_element("Credit to Deposit Ratio", year , self.creditToDeposit(year))
            
            ## Leverage / Gearing / Solvency
            self.setOutput_element("Leverage Ratio", year, self.leverageRatio(year))
            self.setOutput_element("CET-1 Ratio", year, self.CET1Ratio(year))
            self.setOutput_element("Loans to Assets Ratio", year, self.loansToAssets(year))
            self.setOutput_element("Capital Adequacy Ratio", year, self.capitalAdequacy(year))
            self.setOutput_element("Bad Loan Ratio", year, self.badLoanRatio(year))
            self.setOutput_element("Loan Loss Provision Coverage Ratio", year, self.loanLossProvisionCoverageRatio(year))
            
    # Unique Financial Ratios
    
     # Profitability
    
    def netInterestMargin(self, year):
        intInc = self.getInputElement("Interest Income", year)
        intExp = self.getInputElement("Interest Expense", year)
        totAssets = self.getInputElement("Total Assets", year)
        intAssets = self.getInputElement("Intangible Assets", year)
        
        tangibleAssets = totAssets - intAssets
        
        if tangibleAssets == 0:
            print("ERROR - Net interest margin: denominator is zero")
            return 0
        
        return (intInc - intExp)/tangibleAssets
    
    def netNonInterestMargin(self, year):
        nonIntInc = self.getInputElement("Non-Interest Income", year)
        nonIntExp = self.getInputElement("Non-Interest Expense", year)
        totAssets = self.getInputElement("Total Assets", year)
        intAssets = self.getInputElement("Intangible Assets", year)
        
        tangibleAssets = totAssets - intAssets
        
        if tangibleAssets == 0:
            print("ERROR - Net interest margin: denominator is zero")
            return 0
        
        return (nonIntInc - nonIntExp)/tangibleAssets
    
    def ROA(self, year):
        netIncome = self.getInputElement("Net Income", year)
        totAssets = self.getInputElement("Total Assets", year)
        intAssets = self.getInputElement("Intangible Assets", year)
        
        tangibleAssets = totAssets - intAssets
        
        if tangibleAssets == 0:
            print("ERROR - ROA: denominator is zero")
            return 0.0
        
        return netIncome/tangibleAssets
    
    def casaRatio(self, year):
        currentAccounts = self.getInputElement("Current Accounts Deposit", year)
        savingsAccounts = self.getInputElement("Savings Accounts Deposit", year)
        
        if savingsAccounts == 0:
            print("ERROR - CASA ratio: denominator is zero")
            return 0
        
        return currentAccounts/savingsAccounts
    
    def netBankOperatingMargin(self, year):
        opRevenue = self.getInputElement("Operating Revenue", year)
        opExpense = self.getInputElement("Operating Expense", year)
        
        totAssets = self.getInputElement("Total Assets", year)
        intAssets = self.getInputElement("Intangible Assets", year)
        
        tangibleAssets = totAssets - intAssets
        
        if tangibleAssets == 0:
            print("ERROR - Net Bank Operating Margin: denominator is zero")
            return 0.0
        
        return (opRevenue - opExpense)/tangibleAssets
    
    def netProfitMargin(self, year):
        netIncome = self.getInputElement("Net Income", year)
        opRevenue = self.getInputElement("Operating Revenue", year)
        
        if opRevenue == 0:
            print("ERROR - Net Profit Margin: denominator is zero")
            return 0.0
        
        return netIncome/opRevenue
    
    def assetUtilization(self, year):
        opRevenue = self.getInputElement("Operating Revenue", year)
        
        totAssets = self.getInputElement("Total Assets", year)
        intAssets = self.getInputElement("Intangible Assets", year)
        
        tangibleAssets = totAssets - intAssets
        
        if tangibleAssets == 0:
            print("ERROR - Asset Utilization: denominator is zero")
            return 0.0
        
        return opRevenue/tangibleAssets
        
    # Efficiency / Activity
    
    def efficiencyRatio(self, year):
        nonIntExp = self.getInputElement("Non-Interest Expense", year)
        revenue = self.getInputElement("Revenue", year)
        
        if revenue == 0:
            print("ERROR - Efficiency ratio: denominator is zero")
            return 0
        
        return nonIntExp/revenue 
    
    def operatingEfficiencyRatio(self, year):
        opExpense = self.getInputElement("Operating Expense", year)
        opRevenue = self.getInputElement("Operating Revenue", year)
        
        if opRevenue == 0:
            print("ERROR - Operating Efficiency Ratio: denominator is zero")
            return 0
        
        return opExpense/opRevenue
    
    # Liquidity
    
    def creditToDeposit(self, year):
        netLoanAndAcceptance = self.getInputElement("Gross Loans and Acceptance", year)
        totalDeposits = self.getInputElement("Total Deposits", year)
        
        if totalDeposits == 0:
            print("ERROR - Credit to Deposit ratio: denominator is zero")
            return 0
        
        return netLoanAndAcceptance/totalDeposits
        
    # Leverage / Gearing / Solvency
    
    def leverageRatio(self, year):
        tier1Cap = self.getInputElement("Tier 1 Capital", year)
        totAssets = self.getInputElement("Total Assets", year)
        intAssets = self.getInputElement("Intangible Assets", year)
        
        tangibleAssets = totAssets - intAssets
        
        if tangibleAssets == 0:
            print("ERROR - Leverage Ratio: denominator is zero")
            return 0
        
        return tier1Cap/tangibleAssets
    
    def CET1Ratio(self, year):
        CET1Cap = self.getInputElement("Common Equity Tier 1 Capital", year)
        RWA = self.getInputElement("Risk Weighted Assets", year)
        
        if RWA == 0:
            print("ERROR - CET1 Ratio: denominator is zero")
            return 0
        
        return CET1Cap/RWA
    
    def loansToAssets(self, year):
        netLoansAndAcceptance = self.getInputElement("Gross Loans and Acceptance", year)
        
        totAssets = self.getInputElement("Total Assets", year)
        intAssets = self.getInputElement("Intangible Assets", year)
        
        #print("Net Loans and Acceptance", netLoansAndAcceptance, " Total Assets: ", totAssets, " Intangible Assets: ", intAssets)
        
        tangibleAssets = totAssets - intAssets
        
        if tangibleAssets == 0:
            print("ERROR - Loans to Assets ratio: denominator is zero")
            return 0
        
        return netLoansAndAcceptance/tangibleAssets
    
    def capitalAdequacy(self, year):
        tier1Cap = self.getInputElement("Tier 1 Capital", year)
        tier2Cap = self.getInputElement("Tier 2 Capital", year)
        RWA = self.getInputElement("Risk Weighted Assets", year)
        
        if RWA == 0:
            print("ERROR - CET1 Ratio: denominator is zero")
            return 0
        
        return (tier1Cap + tier2Cap)/RWA
    
    def badLoanRatio(self, year):
        totNPA = self.getInputElement("Total NPA", year)
        netLoansAndAcceptance = self.getInputElement("Gross Loans and Acceptance", year)
        
        if netLoansAndAcceptance == 0:
            print("ERROR - Bad Loan ratio: denominator is zero")
            return 0
        
        return totNPA/netLoansAndAcceptance
    
    def loanLossProvisionCoverageRatio(self, year):
        totNPA = self.getInputElement("Total NPA", year)
        creditLossProvision = self.getInputElement("Provision for Credit Loss", year)
        
        if totNPA == 0:
            print("ERROR - Loan Loss Provision Coverage Ratio: denominator is zero")
            return 0
        
        return creditLossProvision/totNPA