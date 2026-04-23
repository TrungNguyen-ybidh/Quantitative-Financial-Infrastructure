fmp_endpoints = [
    # --- Company Profile --- 
    {
        "endpoint": "profile",
        "params": {}

    },

    # --- Quote ---
    {
        "endpoint": "quote",
        "params": {}
    },

    # --- Core Statements ---
    {
        "endpoint": "income-statement",
        "params": {"period": "quarter", "limit": 1000}
    },
    {
        "endpoint": "balance-sheet-statement",
        "params": {"period": "quarter", "limit": 1000}
    },
    {
        "endpoint": "cash-flow-statement",
        "params": {"period": "quarter", "limit": 1000}
    },

    # --- Metrics & Ratios ---
    {
        "endpoint": "key-metrics",
        "params": {"limit": 1000}
    },
    {
        "endpoint": "ratios",
        "params": { "limit": 1000}
    },

     {
        "endpoint": "financial-scores",
        "params": {}
    },

    # --- Valuation ---
    {
        "endpoint": "enterprise-values",
        "params": {"period": "annual", "limit": 1000}
    },
    {
        "endpoint": "discounted-cash-flow",
        "params": {}
    },
    {
        "endpoint": "levered-discounted-cash-flow",
        "params": {}
    },

    # --- Growth ---
    {
        "endpoint": "income-statement-growth",
        "params": {"period": "annual", "limit": 1000}
    },
    {
        "endpoint": "balance-sheet-statement-growth",
        "params": {"period": "annual", "limit": 1000}
    },
    {
        "endpoint": "cash-flow-statement-growth",
        "params": {"period": "annual", "limit": 1000}
    },
    {
        "endpoint": "financial-growth",
        "params": {"period": "annual", "limit": 1000}
    },

    # --- Segmentation ---
    {
        "endpoint": "revenue-product-segmentation",
        "params": {"period": "annual", "limit": 1000}
    },
    {
        "endpoint": "revenue-geographic-segmentation",
        "params": {"period": "annual", "limit": 1000}
    },

    # --- Dividends ---
    {
        "endpoint": "dividends",
        "params": {"limit": 1000}
    },

    # --- Analyst --- 
     {
        "endpoint": "analyst-estimates",
        "params": {"period": "annual", "limit": 1000, "page":0}
    },

     {
        "endpoint": "ratings-historical",
        "params": {"limit": 1000}
    },
]

fmp_update_endpoints = [
    # --- Quote (snapshot, no history) ---
    {
        "endpoint": "quote",
        "params": {}
    },

    # --- Core Statements ---
    # Quarterly: limit=4 grabs ~1 year of quarters, enough to catch
    # the latest release + any prior-quarter restatements
    {
        "endpoint": "income-statement",
        "params": {"period": "quarter", "limit": 1}
    },
    {
        "endpoint": "balance-sheet-statement",
        "params": {"period": "quarter", "limit": 1}
    },
    {
        "endpoint": "cash-flow-statement",
        "params": {"period": "quarter", "limit": 1}
    },

    # --- Metrics & Ratios ---
    # These default to annual when no period is specified.
    # limit=2 catches the latest + one prior (for revision checks)
    {
        "endpoint": "key-metrics",
        "params": {"limit": 2}
    },
    {
        "endpoint": "ratios",
        "params": {"limit": 2}
    },

    # --- Financial Scores (snapshot, no history) ---
    {
        "endpoint": "financial-scores",
        "params": {}
    },

    # --- Valuation ---
    # Annual: limit=2 for latest + prior year
    {
        "endpoint": "enterprise-values",
        "params": {"period": "annual", "limit": 1}
    },
    # DCF endpoints are point-in-time snapshots
    {
        "endpoint": "discounted-cash-flow",
        "params": {}
    },
    {
        "endpoint": "levered-discounted-cash-flow",
        "params": {}
    },

    # --- Growth ---
    # Annual: limit=2 for latest + prior year
    {
        "endpoint": "income-statement-growth",
        "params": {"period": "annual", "limit": 1}
    },
    {
        "endpoint": "balance-sheet-statement-growth",
        "params": {"period": "annual", "limit": 1}
    },
    {
        "endpoint": "cash-flow-statement-growth",
        "params": {"period": "annual", "limit": 1}
    },
    {
        "endpoint": "financial-growth",
        "params": {"period": "annual", "limit": 1}
    },

    # --- Segmentation ---
    # Annual: limit=2 for latest + prior year
    {
        "endpoint": "revenue-product-segmentation",
        "params": {"period": "annual", "limit": 1}
    },
    {
        "endpoint": "revenue-geographic-segmentation",
        "params": {"period": "annual", "limit": 1}
    },

    # --- Dividends ---
    # limit=4 covers roughly the last year of quarterly dividends
    {
        "endpoint": "dividends",
        "params": {"limit": 1}
    },

    # --- Analyst ---
    {
        "endpoint": "analyst-estimates",
        "params": {"period": "annual", "limit": 1, "page": 0}
    },

    # Ratings: already limit=1, perfect for updates
    {
        "endpoint": "ratings-historical",
        "params": {"limit": 1}
    },
]

schema_map = {
    "profile.csv": {
        "primary_key": ["symbol"],
        "keep": [
            "symbol", "companyName", "price", "marketCap", "beta",
            "sector", "industry", "country", "cik", "isin", "cusip",
            "exchange", "ceo", "ipoDate", "description"
        ],
        "rename": {
            "symbol": "ticker",
            "companyName": "company_name",
            "price": "price",
            "marketCap": "market_cap",
            "beta": "beta",
            "sector": "sector",
            "industry": "industry",
            "country": "country",
            "cik": "cik",
            "isin": "isin",
            "cusip": "cusip",
            "exchange": "exchange",
            "ceo": "ceo",
            "ipoDate": "ipo_date",
            "description": "description"
        },
        "drop": [
            "lastDividend", "range", "change", "changePercentage", "fullTimeEmployees",
            "volume", "averageVolume", "currency", "exchangeFullName",
            "website", "phone", "address", "city", "state", "zip",
            "image", "defaultImage", "isEtf", "isActivelyTrading",
            "isAdr", "isFund"
        ]
    },

    "quote.csv": {
        "primary_key": ["symbol"],
        "keep": [
            "symbol", "name", "price", "marketCap",
            "yearHigh", "yearLow", "priceAvg50", "priceAvg200", "volume"
        ],
        "rename": {
            "symbol": "ticker",
            "name": "name",
            "price": "price",
            "marketCap": "market_cap",
            "yearHigh": "year_high",
            "yearLow": "year_low",
            "priceAvg50": "price_avg_50",
            "priceAvg200": "price_avg_200",
            "volume": "volume"
        },
        "drop": [
            "changePercentage", "change", "dayLow", "dayHigh",
            "exchange", "open", "previousClose", "timestamp"
        ]
    },

    "financial-scores.csv": {
        "primary_key": ["symbol"],
        "keep": [
            "symbol", "altmanZScore", "piotroskiScore",
            "workingCapital", "totalAssets", "retainedEarnings",
            "ebit", "marketCap", "totalLiabilities", "revenue"
        ],
        "rename": {
            "symbol": "ticker",
            "altmanZScore": "altman_z_score",
            "piotroskiScore": "piotroski_score",
            "workingCapital": "working_capital",
            "totalAssets": "total_assets",
            "retainedEarnings": "retained_earnings",
            "ebit": "ebit",
            "marketCap": "market_cap",
            "totalLiabilities": "total_liabilities",
            "revenue": "revenue"
        },
        "drop": [
            "reportedCurrency"
        ]
    },

    "discounted-cash-flow.csv": {
        "primary_key": ["symbol", "date"],
        "keep": [
            "symbol", "date", "dcf", "Stock Price"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "dcf": "dcf",
            "Stock Price": "stock_price"
        },
        "drop": []
    },

    "levered-discounted-cash-flow.csv": {
        "primary_key": ["symbol", "date"],
        "keep": [
            "symbol", "date", "dcf", "Stock Price"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "dcf": "levered_dcf",
            "Stock Price": "stock_price"
        },
        "drop": []
    },

    # ======================== TIME-SERIES STATEMENTS ========================
    # PK: (symbol, date, period)

        "income-statement.csv": {
            "primary_key": ["symbol", "date", "period"],
            "keep": [
                "date", "symbol", "fiscalYear", "period", "filingDate", "acceptedDate",
                "revenue", "costOfRevenue", "grossProfit",
                "researchAndDevelopmentExpenses",
                "sellingGeneralAndAdministrativeExpenses",
                "operatingExpenses", "operatingIncome",
                "interestIncome", "interestExpense",
                "depreciationAndAmortization",
                "ebitda", "ebit",
                "incomeBeforeTax", "incomeTaxExpense", "netIncome",
                "eps", "epsDiluted",
                "weightedAverageShsOut", "weightedAverageShsOutDil"
            ],
            "rename": {
                "date": "date",
                "symbol": "ticker",
                "fiscalYear": "fiscal_year",
                "period": "period",
                "filingDate": "filing_date", 
                "acceptedDate": "accepted_date",
                "revenue": "revenue",
                "costOfRevenue": "cost_of_revenue",
                "grossProfit": "gross_profit",
                "researchAndDevelopmentExpenses": "rd_expenses",
                "sellingGeneralAndAdministrativeExpenses": "sga_expenses",
                "operatingExpenses": "operating_expenses",
                "operatingIncome": "operating_income",
                "interestIncome": "interest_income",
                "interestExpense": "interest_expense",
                "depreciationAndAmortization": "depreciation_amortization",
                "ebitda": "ebitda",
                "ebit": "ebit",
                "incomeBeforeTax": "income_before_tax",
                "incomeTaxExpense": "income_tax_expense",
                "netIncome": "net_income",
                "eps": "eps",
                "epsDiluted": "eps_diluted",
                "weightedAverageShsOut": "shares_outstanding",
                "weightedAverageShsOutDil": "shares_outstanding_diluted"
            },
            "drop": [
                "reportedCurrency", "cik",
                "generalAndAdministrativeExpenses",
                "sellingAndMarketingExpenses", "otherExpenses",
                "costAndExpenses", "netInterestIncome",
                "nonOperatingIncomeExcludingInterest",
                "totalOtherIncomeExpensesNet",
                "netIncomeFromContinuingOperations",
                "netIncomeFromDiscontinuedOperations",
                "otherAdjustmentsToNetIncome",
                "netIncomeDeductions", "bottomLineNetIncome"
            ]
        },

        "balance-sheet-statement.csv": {
            "primary_key": ["symbol", "date", "period"],
            "keep": [
                "date", "symbol", "fiscalYear", "period", "filingDate", "acceptedDate",
                "cashAndCashEquivalents", "shortTermInvestments",
                "cashAndShortTermInvestments",
                "netReceivables", "inventory",
                "totalCurrentAssets",
                "propertyPlantEquipmentNet",
                "goodwill", "intangibleAssets",
                "longTermInvestments", "taxAssets",
                "totalNonCurrentAssets", "totalAssets",
                "accountPayables", "accruedExpenses",
                "shortTermDebt", "deferredRevenue",
                "totalCurrentLiabilities",
                "longTermDebt",
                "totalNonCurrentLiabilities", "totalLiabilities",
                "retainedEarnings", "additionalPaidInCapital",
                "totalStockholdersEquity", "totalEquity",
                "totalDebt", "netDebt"
            ],
            "rename": {
                "date": "date",
                "symbol": "ticker",
                "fiscalYear": "fiscal_year",
                "period": "period",
                "filingDate": "filing_date", 
                "acceptedDate": "accepted_date",
                "cashAndCashEquivalents": "cash",
                "shortTermInvestments": "short_term_investments",
                "cashAndShortTermInvestments": "cash_and_short_term_investments",
                "netReceivables": "net_receivables",
                "inventory": "inventory",
                "totalCurrentAssets": "total_current_assets",
                "propertyPlantEquipmentNet": "ppe_net",
                "goodwill": "goodwill",
                "intangibleAssets": "intangible_assets",
                "longTermInvestments": "long_term_investments",
                "taxAssets": "tax_assets",
                "totalNonCurrentAssets": "total_non_current_assets",
                "totalAssets": "total_assets",
                "accountPayables": "accounts_payable",
                "accruedExpenses": "accrued_expenses",
                "shortTermDebt": "short_term_debt",
                "deferredRevenue": "deferred_revenue",
                "totalCurrentLiabilities": "total_current_liabilities",
                "longTermDebt": "long_term_debt",
                "totalNonCurrentLiabilities": "total_non_current_liabilities",
                "totalLiabilities": "total_liabilities",
                "retainedEarnings": "retained_earnings",
                "additionalPaidInCapital": "additional_paid_in_capital",
                "totalStockholdersEquity": "stockholders_equity",
                "totalEquity": "total_equity",
                "totalDebt": "total_debt",
                "netDebt": "net_debt"
            },
            "drop": [
                "reportedCurrency", "cik",
                "accountsReceivables", "otherReceivables",
                "prepaids", "otherCurrentAssets",
                "goodwillAndIntangibleAssets",
                "otherNonCurrentAssets", "otherAssets",
                "totalPayables", "otherPayables",
                "capitalLeaseObligationsCurrent", "taxPayables",
                "otherCurrentLiabilities",
                "capitalLeaseObligationsNonCurrent",
                "deferredRevenueNonCurrent",
                "deferredTaxLiabilitiesNonCurrent",
                "otherNonCurrentLiabilities",
                "otherLiabilities", "capitalLeaseObligations",
                "treasuryStock", "preferredStock", "commonStock",
                "accumulatedOtherComprehensiveIncomeLoss",
                "otherTotalStockholdersEquity",
                "minorityInterest",
                "totalLiabilitiesAndTotalEquity",
                "totalInvestments"
            ]
        },

        "cash-flow-statement.csv": {
            "primary_key": ["symbol", "date", "period"],
            "keep": [
                "date", "symbol", "fiscalYear", "period", "filingDate", "acceptedDate",
                "netIncome", "depreciationAndAmortization",
                "stockBasedCompensation", "deferredIncomeTax",
                "changeInWorkingCapital",
                "netCashProvidedByOperatingActivities",
                "investmentsInPropertyPlantAndEquipment",
                "acquisitionsNet",
                "purchasesOfInvestments", "salesMaturitiesOfInvestments",
                "netCashProvidedByInvestingActivities",
                "netDebtIssuance",
                "commonStockRepurchased", "netDividendsPaid",
                "netCashProvidedByFinancingActivities",
                "operatingCashFlow", "capitalExpenditure", "freeCashFlow",
                "incomeTaxesPaid", "interestPaid"
            ],
            "rename": {
                "date": "date",
                "symbol": "ticker",
                "fiscalYear": "fiscal_year",
                "period": "period",
                "filingDate": "filing_date", 
                "acceptedDate": "accepted_date",
                "netIncome": "net_income",
                "depreciationAndAmortization": "depreciation_amortization",
                "stockBasedCompensation": "stock_based_compensation",
                "deferredIncomeTax": "deferred_income_tax",
                "changeInWorkingCapital": "change_in_working_capital",
                "netCashProvidedByOperatingActivities": "cash_from_operations",
                "investmentsInPropertyPlantAndEquipment": "ppe_investments",
                "acquisitionsNet": "acquisitions_net",
                "purchasesOfInvestments": "purchases_of_investments",
                "salesMaturitiesOfInvestments": "sales_of_investments",
                "netCashProvidedByInvestingActivities": "cash_from_investing",
                "netDebtIssuance": "net_debt_issuance",
                "commonStockRepurchased": "stock_repurchased",
                "netDividendsPaid": "dividends_paid",
                "netCashProvidedByFinancingActivities": "cash_from_financing",
                "operatingCashFlow": "operating_cash_flow",
                "capitalExpenditure": "capex",
                "freeCashFlow": "free_cash_flow",
                "incomeTaxesPaid": "income_taxes_paid",
                "interestPaid": "interest_paid"
            },
            "drop": [
                "reportedCurrency", "cik",
                "accountsReceivables", "inventory", "accountsPayables",
                "otherWorkingCapital", "otherNonCashItems",
                "otherInvestingActivities",
                "longTermNetDebtIssuance", "shortTermNetDebtIssuance",
                "netStockIssuance", "netCommonStockIssuance",
                "commonStockIssuance", "netPreferredStockIssuance",
                "commonDividendsPaid", "preferredDividendsPaid",
                "otherFinancingActivities",
                "effectOfForexChangesOnCash", "netChangeInCash",
                "cashAtEndOfPeriod", "cashAtBeginningOfPeriod"
            ]
        },

    # ======================== GROWTH STATEMENTS ========================
    # PK: (symbol, date, period)

    "balance-sheet-statement-growth.csv": {
        "primary_key": ["symbol", "date", "period"],
        "keep": [
            "symbol", "date", "fiscalYear", "period",
            "growthTotalAssets", "growthTotalLiabilities",
            "growthTotalEquity", "growthTotalDebt", "growthNetDebt",
            "growthTotalCurrentAssets", "growthTotalCurrentLiabilities"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "fiscalYear": "fiscal_year",
            "period": "period",
            "growthTotalAssets": "growth_total_assets",
            "growthTotalLiabilities": "growth_total_liabilities",
            "growthTotalEquity": "growth_total_equity",
            "growthTotalDebt": "growth_total_debt",
            "growthNetDebt": "growth_net_debt",
            "growthTotalCurrentAssets": "growth_total_current_assets",
            "growthTotalCurrentLiabilities": "growth_total_current_liabilities"
        },
        "drop": [
            "reportedCurrency",
            "growthCashAndCashEquivalents", "growthShortTermInvestments",
            "growthCashAndShortTermInvestments", "growthNetReceivables",
            "growthInventory", "growthOtherCurrentAssets",
            "growthPropertyPlantEquipmentNet", "growthGoodwill",
            "growthIntangibleAssets", "growthGoodwillAndIntangibleAssets",
            "growthLongTermInvestments", "growthTaxAssets",
            "growthOtherNonCurrentAssets", "growthTotalNonCurrentAssets",
            "growthOtherAssets", "growthAccountPayables",
            "growthShortTermDebt", "growthTaxPayables",
            "growthDeferredRevenue", "growthOtherCurrentLiabilities",
            "growthLongTermDebt", "growthDeferredRevenueNonCurrent",
            "growthDeferredTaxLiabilitiesNonCurrent",
            "growthOtherNonCurrentLiabilities", "growthTotalNonCurrentLiabilities",
            "growthOtherLiabilities", "growthPreferredStock",
            "growthCommonStock", "growthRetainedEarnings",
            "growthAccumulatedOtherComprehensiveIncomeLoss",
            "growthOthertotalStockholdersEquity", "growthTotalStockholdersEquity",
            "growthMinorityInterest", "growthTotalLiabilitiesAndStockholdersEquity",
            "growthTotalInvestments", "growthAccountsReceivables",
            "growthOtherReceivables", "growthPrepaids",
            "growthTotalPayables", "growthOtherPayables",
            "growthAccruedExpenses", "growthCapitalLeaseObligationsCurrent",
            "growthAdditionalPaidInCapital", "growthTreasuryStock"
        ]
    },

    "cash-flow-statement-growth.csv": {
        "primary_key": ["symbol", "date", "period"],
        "keep": [
            "symbol", "date", "fiscalYear", "period",
            "growthOperatingCashFlow", "growthFreeCashFlow",
            "growthCapitalExpenditure", "growthNetChangeInCash",
            "growthDividendsPaid"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "fiscalYear": "fiscal_year",
            "period": "period",
            "growthOperatingCashFlow": "growth_operating_cash_flow",
            "growthFreeCashFlow": "growth_free_cash_flow",
            "growthCapitalExpenditure": "growth_capex",
            "growthNetChangeInCash": "growth_net_change_in_cash",
            "growthDividendsPaid": "growth_dividends_paid"
        },
        "drop": [
            "reportedCurrency",
            "growthNetIncome", "growthDepreciationAndAmortization",
            "growthDeferredIncomeTax", "growthStockBasedCompensation",
            "growthChangeInWorkingCapital", "growthAccountsReceivables",
            "growthInventory", "growthAccountsPayables",
            "growthOtherWorkingCapital", "growthOtherNonCashItems",
            "growthNetCashProvidedByOperatingActivites",
            "growthInvestmentsInPropertyPlantAndEquipment",
            "growthAcquisitionsNet", "growthPurchasesOfInvestments",
            "growthSalesMaturitiesOfInvestments", "growthOtherInvestingActivites",
            "growthNetCashUsedForInvestingActivites", "growthDebtRepayment",
            "growthCommonStockIssued", "growthCommonStockRepurchased",
            "growthOtherFinancingActivites",
            "growthNetCashUsedProvidedByFinancingActivities",
            "growthEffectOfForexChangesOnCash",
            "growthCashAtEndOfPeriod", "growthCashAtBeginningOfPeriod",
            "growthNetDebtIssuance", "growthLongTermNetDebtIssuance",
            "growthShortTermNetDebtIssuance", "growthNetStockIssuance",
            "growthPreferredDividendsPaid", "growthIncomeTaxesPaid",
            "growthInterestPaid"
        ]
    },

    "income-statement-growth.csv": {
        "primary_key": ["symbol", "date", "period"],
        "keep": [
            "symbol", "date", "fiscalYear", "period",
            "growthRevenue", "growthGrossProfit",
            "growthOperatingIncome", "growthNetIncome",
            "growthEBITDA", "growthEPS", "growthEPSDiluted"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "fiscalYear": "fiscal_year",
            "period": "period",
            "growthRevenue": "growth_revenue",
            "growthGrossProfit": "growth_gross_profit",
            "growthOperatingIncome": "growth_operating_income",
            "growthNetIncome": "growth_net_income",
            "growthEBITDA": "growth_ebitda",
            "growthEPS": "growth_eps",
            "growthEPSDiluted": "growth_eps_diluted"
        },
        "drop": [
            "reportedCurrency",
            "growthCostOfRevenue", "growthGrossProfitRatio",
            "growthResearchAndDevelopmentExpenses",
            "growthGeneralAndAdministrativeExpenses",
            "growthSellingAndMarketingExpenses", "growthOtherExpenses",
            "growthOperatingExpenses", "growthCostAndExpenses",
            "growthInterestIncome", "growthInterestExpense",
            "growthDepreciationAndAmortization", "growthEBIT",
            "growthIncomeBeforeTax", "growthIncomeTaxExpense",
            "growthWeightedAverageShsOut", "growthWeightedAverageShsOutDil",
            "growthNonOperatingIncomeExcludingInterest",
            "growthNetInterestIncome", "growthTotalOtherIncomeExpensesNet",
            "growthNetIncomeFromContinuingOperations",
            "growthOtherAdjustmentsToNetIncome", "growthNetIncomeDeductions"
        ]
    },

    # ======================== TIME-SERIES METRICS & RATIOS ========================
    # PK: (symbol, date, period)

    "key-metrics.csv": {
        "primary_key": ["symbol", "date", "period"],
        "keep": [
            "symbol", "date", "fiscalYear", "period",
            "marketCap", "enterpriseValue",
            "evToSales", "evToEBITDA", "evToFreeCashFlow",
            "netDebtToEBITDA", "currentRatio", "incomeQuality",
            "grahamNumber",
            "workingCapital", "investedCapital",
            "returnOnAssets", "returnOnEquity",
            "returnOnInvestedCapital", "returnOnCapitalEmployed",
            "earningsYield", "freeCashFlowYield",
            "researchAndDevelopementToRevenue",
            "stockBasedCompensationToRevenue",
            "capexToRevenue",
            "daysOfSalesOutstanding", "daysOfPayablesOutstanding",
            "daysOfInventoryOutstanding", "cashConversionCycle",
            "freeCashFlowToEquity", "freeCashFlowToFirm",
            "tangibleAssetValue", "netCurrentAssetValue"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "fiscalYear": "fiscal_year",
            "period": "period",
            "marketCap": "market_cap",
            "enterpriseValue": "enterprise_value",
            "evToSales": "ev_to_sales",
            "evToEBITDA": "ev_to_ebitda",
            "evToFreeCashFlow": "ev_to_fcf",
            "netDebtToEBITDA": "net_debt_to_ebitda",
            "currentRatio": "current_ratio",
            "incomeQuality": "income_quality",
            "grahamNumber": "graham_number",
            "workingCapital": "working_capital",
            "investedCapital": "invested_capital",
            "returnOnAssets": "roa",
            "returnOnEquity": "roe",
            "returnOnInvestedCapital": "roic",
            "returnOnCapitalEmployed": "roce",
            "earningsYield": "earnings_yield",
            "freeCashFlowYield": "fcf_yield",
            "researchAndDevelopementToRevenue": "rd_to_revenue",
            "stockBasedCompensationToRevenue": "sbc_to_revenue",
            "capexToRevenue": "capex_to_revenue",
            "daysOfSalesOutstanding": "days_sales_outstanding",
            "daysOfPayablesOutstanding": "days_payables_outstanding",
            "daysOfInventoryOutstanding": "days_inventory_outstanding",
            "cashConversionCycle": "cash_conversion_cycle",
            "freeCashFlowToEquity": "fcf_to_equity",
            "freeCashFlowToFirm": "fcf_to_firm",
            "tangibleAssetValue": "tangible_asset_value",
            "netCurrentAssetValue": "net_current_asset_value"
        },
        "drop": [
            "reportedCurrency",
            "evToOperatingCashFlow",
            "grahamNetNet",
            "taxBurden", "interestBurden",
            "operatingReturnOnAssets", "returnOnTangibleAssets",
            "capexToOperatingCashFlow", "capexToDepreciation",
            "salesGeneralAndAdministrativeToRevenue",
            "intangiblesToTotalAssets",
            "averageReceivables", "averagePayables", "averageInventory",
            "operatingCycle"
        ]
    },

    "ratios.csv": {
        "primary_key": ["symbol", "date", "period"],
        "keep": [
            "symbol", "date", "fiscalYear", "period",
            "grossProfitMargin", "ebitMargin", "ebitdaMargin",
            "operatingProfitMargin", "netProfitMargin",
            "receivablesTurnover", "payablesTurnover",
            "inventoryTurnover", "fixedAssetTurnover", "assetTurnover",
            "currentRatio", "quickRatio",
            "debtToEquityRatio", "debtToAssetsRatio",
            "financialLeverageRatio", "interestCoverageRatio",
            "priceToEarningsRatio", "priceToBookRatio",
            "priceToSalesRatio", "priceToFreeCashFlowRatio",
            "enterpriseValueMultiple",
            "operatingCashFlowSalesRatio",
            "freeCashFlowOperatingCashFlowRatio",
            "dividendPayoutRatio", "dividendYield",
            "effectiveTaxRate"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "fiscalYear": "fiscal_year",
            "period": "period",
            # Margins
            "grossProfitMargin": "gross_margin",
            "ebitMargin": "ebit_margin",
            "ebitdaMargin": "ebitda_margin",
            "operatingProfitMargin": "operating_margin",
            "netProfitMargin": "net_margin",
            # Turnover
            "receivablesTurnover": "receivables_turnover",
            "payablesTurnover": "payables_turnover",
            "inventoryTurnover": "inventory_turnover",
            "fixedAssetTurnover": "fixed_asset_turnover",
            "assetTurnover": "asset_turnover",
            # Liquidity
            "currentRatio": "current_ratio",
            "quickRatio": "quick_ratio",
            # Leverage
            "debtToEquityRatio": "debt_to_equity",
            "debtToAssetsRatio": "debt_to_assets",
            "financialLeverageRatio": "financial_leverage",
            "interestCoverageRatio": "interest_coverage",
            # Valuation
            "priceToEarningsRatio": "pe_ratio",
            "priceToBookRatio": "pb_ratio",
            "priceToSalesRatio": "ps_ratio",
            "priceToFreeCashFlowRatio": "p_to_fcf",
            "enterpriseValueMultiple": "ev_multiple",
            # Cash flow quality
            "operatingCashFlowSalesRatio": "ocf_to_sales",
            "freeCashFlowOperatingCashFlowRatio": "fcf_to_ocf",
            # Dividend
            "dividendPayoutRatio": "dividend_payout_ratio",
            "dividendYield": "dividend_yield",
            # Tax
            "effectiveTaxRate": "effective_tax_rate"
        },
        "drop": [
            "reportedCurrency",
            "pretaxProfitMargin",
            "continuousOperationsProfitMargin",
            "bottomLineProfitMargin",
            "debtToCapitalRatio", "longTermDebtToCapitalRatio",
            "solvencyRatio", "cashRatio",
            "priceToEarningsGrowthRatio",
            "forwardPriceToEarningsGrowthRatio",
            "priceToOperatingCashFlowRatio",
            "priceToFairValue", "debtToMarketCap",
            "workingCapitalTurnoverRatio",
            "operatingCashFlowRatio",
            "debtServiceCoverageRatio",
            "shortTermOperatingCashFlowCoverageRatio",
            "operatingCashFlowCoverageRatio",
            "capitalExpenditureCoverageRatio",
            "dividendPaidAndCapexCoverageRatio",
            "revenuePerShare", "netIncomePerShare",
            "interestDebtPerShare", "cashPerShare",
            "bookValuePerShare", "tangibleBookValuePerShare",
            "shareholdersEquityPerShare",
            "operatingCashFlowPerShare", "capexPerShare",
            "freeCashFlowPerShare",
            "netIncomePerEBT", "ebtPerEbit",
            "dividendYieldPercentage", "dividendPerShare"
        ]
    },

    "financial-growth.csv": {
        "primary_key": ["symbol", "date", "period"],
        "keep": [
            "symbol", "date", "fiscalYear", "period",
            "revenueGrowth", "grossProfitGrowth",
            "operatingIncomeGrowth", "netIncomeGrowth",
            "epsdilutedGrowth", "ebitdaGrowth",
            "operatingCashFlowGrowth", "freeCashFlowGrowth",
            "threeYRevenueGrowthPerShare",
            "fiveYRevenueGrowthPerShare",
            "tenYRevenueGrowthPerShare",
            "threeYNetIncomeGrowthPerShare",
            "fiveYNetIncomeGrowthPerShare",
            "tenYNetIncomeGrowthPerShare",
            "threeYOperatingCFGrowthPerShare",
            "fiveYOperatingCFGrowthPerShare",
            "tenYOperatingCFGrowthPerShare"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "fiscalYear": "fiscal_year",
            "period": "period",
            "revenueGrowth": "revenue_growth",
            "grossProfitGrowth": "gross_profit_growth",
            "operatingIncomeGrowth": "operating_income_growth",
            "netIncomeGrowth": "net_income_growth",
            "epsdilutedGrowth": "eps_diluted_growth",
            "ebitdaGrowth": "ebitda_growth",
            "operatingCashFlowGrowth": "operating_cf_growth",
            "freeCashFlowGrowth": "fcf_growth",
            "threeYRevenueGrowthPerShare": "revenue_cagr_3y",
            "fiveYRevenueGrowthPerShare": "revenue_cagr_5y",
            "tenYRevenueGrowthPerShare": "revenue_cagr_10y",
            "threeYNetIncomeGrowthPerShare": "net_income_cagr_3y",
            "fiveYNetIncomeGrowthPerShare": "net_income_cagr_5y",
            "tenYNetIncomeGrowthPerShare": "net_income_cagr_10y",
            "threeYOperatingCFGrowthPerShare": "operating_cf_cagr_3y",
            "fiveYOperatingCFGrowthPerShare": "operating_cf_cagr_5y",
            "tenYOperatingCFGrowthPerShare": "operating_cf_cagr_10y"
        },
        "drop": [
            "reportedCurrency",
            "ebitgrowth", "epsgrowth",
            "weightedAverageSharesGrowth",
            "weightedAverageSharesDilutedGrowth",
            "dividendsPerShareGrowth",
            "receivablesGrowth", "inventoryGrowth",
            "assetGrowth", "bookValueperShareGrowth",
            "debtGrowth", "rdexpenseGrowth", "sgaexpensesGrowth",
            "growthCapitalExpenditure",
            "tenYShareholdersEquityGrowthPerShare",
            "fiveYShareholdersEquityGrowthPerShare",
            "threeYShareholdersEquityGrowthPerShare",
            "tenYDividendperShareGrowthPerShare",
            "fiveYDividendperShareGrowthPerShare",
            "threeYDividendperShareGrowthPerShare",
            "tenYBottomLineNetIncomeGrowthPerShare",
            "fiveYBottomLineNetIncomeGrowthPerShare",
            "threeYBottomLineNetIncomeGrowthPerShare"
        ]
    },

    "enterprise-values.csv": {
        "primary_key": ["symbol", "date"],
        "keep": [
            "symbol", "date", "stockPrice", "numberOfShares",
            "marketCapitalization",
            "minusCashAndCashEquivalents", "addTotalDebt",
            "enterpriseValue"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "stockPrice": "stock_price",
            "numberOfShares": "shares_outstanding",
            "marketCapitalization": "market_cap",
            "minusCashAndCashEquivalents": "minus_cash",
            "addTotalDebt": "plus_total_debt",
            "enterpriseValue": "enterprise_value"
        },
        "drop": []
    },

    # ======================== EVENT / IRREGULAR TIME-SERIES ========================
    # PK: (symbol, date)

    "analyst-estimates.csv": {
        "primary_key": ["symbol", "date"],
        "keep": [
            "symbol", "date",
            "revenueAvg", "ebitdaAvg", "netIncomeAvg", "epsAvg",
            "numAnalystsRevenue", "numAnalystsEps"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "revenueAvg": "est_revenue_avg",
            "ebitdaAvg": "est_ebitda_avg",
            "netIncomeAvg": "est_net_income_avg",
            "epsAvg": "est_eps_avg",
            "numAnalystsRevenue": "num_analysts_revenue",
            "numAnalystsEps": "num_analysts_eps"
        },
        "drop": [
            "revenueLow", "revenueHigh",
            "ebitdaLow", "ebitdaHigh",
            "ebitLow", "ebitHigh", "ebitAvg",
            "netIncomeLow", "netIncomeHigh",
            "sgaExpenseLow", "sgaExpenseHigh", "sgaExpenseAvg",
            "epsHigh", "epsLow"
        ]
    },

    "dividends.csv": {
        "primary_key": ["symbol", "date"],
        "keep": [
            "symbol", "date",
            "adjDividend", "dividend", "yield", "frequency"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "adjDividend": "adj_dividend",
            "dividend": "dividend",
            "yield": "dividend_yield",
            "frequency": "frequency"
        },
        "drop": [
            "recordDate", "paymentDate", "declarationDate"
        ]
    },

    "ratings-historical.csv": {
        "primary_key": ["symbol", "date"],
        "keep": [
            "symbol", "date", "rating", "overallScore",
            "discountedCashFlowScore", "returnOnEquityScore",
            "returnOnAssetsScore", "debtToEquityScore",
            "priceToEarningsScore", "priceToBookScore"
        ],
        "rename": {
            "symbol": "ticker",
            "date": "date",
            "rating": "rating",
            "overallScore": "overall_score",
            "discountedCashFlowScore": "dcf_score",
            "returnOnEquityScore": "roe_score",
            "returnOnAssetsScore": "roa_score",
            "debtToEquityScore": "de_score",
            "priceToEarningsScore": "pe_score",
            "priceToBookScore": "pb_score"
        },
        "drop": []
    },
}

financial_mapping = {
    'balance-sheet-statement.csv': 'balance_sheet',
    'balance-sheet-statement-growth.csv': 'balance_sheet_growth',
    'cash-flow-statement.csv': 'cashflow',
    'cash-flow-statement-growth.csv': 'cashflow_growth',
    'profile.csv': 'companies',
    'discounted-cash-flow.csv': 'dcf',
    'levered-discounted-cash-flow.csv': 'dcf_levered',
    'dividends.csv': 'dividends',
    'analyst-estimates.csv': 'estimates',
    'enterprise-values.csv': 'ev',
    'financial-growth.csv': 'growth',
    'income-statement.csv': 'income_stmt',
    'income-statement-growth.csv': 'income_stmt_growth',
    'key-metrics.csv': 'metrics',
    'quote.csv': 'quotes',
    'ratings-historical.csv': 'ratings',
    'ratios.csv': 'ratios',
    'financial-scores.csv': 'scores',
}