from . import fundamentalsAnalysis

from . import Analysis_Valuation
from . import Analysis_Profitability
from . import Analysis_Efficiency
from . import Analysis_Liquidity
from . import Analysis_Solvency

from . import Analysis_sub_dividendPaying
from . import Analysis_sub_haveSales
from . import Analysis_sub_inventoryHolding

class sectorAnalysis_Finance(Analysis_Valuation.Analysis_Valuation, Analysis_Profitability.Analysis_Profitability, Analysis_Efficiency.Analysis_Efficiency, Analysis_Liquidity.Analysis_Liquidity, Analysis_Solvency.Analysis_Solvency, Analysis_sub_dividendPaying.Analysis_dividendPaying, Analysis_sub_haveSales.Analysis_haveSales, Analysis_sub_inventoryHolding.Analysis_inventoryHolding, fundamentalsAnalysis.FA):
    
    def analyse_finance(self):
        print("Analysing Finance's Fundamentals")
        
        self.analyse_valuation()
        self.analyse_profitability()
        self.analyse_efficiency()
        self.analyse_liquidity()
        #self.analyse_solvency() # No Solvency / Debt. Unique Calculation Required.
        
        self.analyse_dividendPaying()
        self.analyse_haveSales()
        self.analyse_inventoryHolding()
        
        self.analyse_netInterestMargin()
        self.analyse_netNonInterestMargin()
        self.analyse_ROA()
        self.analyse_casaRatio()
        self.analyse_netProfitMargin()
        self.analyse_assetUtilization()
        
        self.analyse_efficiencyRatio()
        self.analyse_operatingEfficiencyRatio()
        
        self.analyse_creditToDepositRatio()
        
        self.analyse_leverageRatio()
        self.analyse_cet1Ratio()
        self.analyse_loanToAssetsRatio()
        self.analyse_capitalAdequacyRatio()
        self.analyse_badLoanRatio()
        self.analyse_loanLossProvisionCoverageRatio()
        
    # Unique
    ## Profitability Ratios
        
    def analyse_netInterestMargin(self):
        self.setGrowth("Net Interest Margin")
        
    def analyse_netNonInterestMargin(self):
        self.setGrowth("Net Non-Interest Margin")
    
    def analyse_ROA(self):
        self.setQualities_row("Return on Assets", 0.01, 2)
        self.setGrowth("Return on Assets")
        
    def analyse_casaRatio(self):
        self.setGrowth("CASA Ratio")
     
    def analyse_netBankOperatingMargin(self):
        self.setGrowth("Net Bank Operating Margin")
        
    def analyse_netProfitMargin(self):
        self.setGrowth("Net Profit Margin")
    
    def analyse_assetUtilization(self):
        self.setGrowth("Asset Utilization")
        
    ## Efficiency Ratios
    
    def analyse_efficiencyRatio(self):
        self.setGrowth("Efficiency Ratio")
        
    def analyse_operatingEfficiencyRatio(self):
        self.setGrowth("Operating Efficiency Ratio")
        
    ## Liquidity
    def analyse_creditToDepositRatio(self):
        self.setGrowth("Credit to Deposit Ratio")
        
    ## Solvency
    def analyse_leverageRatio(self):
        self.setQualities_row("Leverage Ratio", 0.03, 2)
        self.setGrowth("Leverage Ratio")
    
    def analyse_cet1Ratio(self):
        self.setGrowth("CET-1 Ratio")
    
    def analyse_loanToAssetsRatio(self):
        self.setGrowth("Loans to Assets Ratio")
    
    def analyse_capitalAdequacyRatio(self):
        self.setQualities_row("Capital Adequacy Ratio", 0.08, 2)
        self.setGrowth("Capital Adequacy Ratio")
        
    def analyse_badLoanRatio(self):
        self.setGrowth("Bad Loan Ratio")
        
    def analyse_loanLossProvisionCoverageRatio(self):
        self.setGrowth("Loan Loss Provision Coverage Ratio")