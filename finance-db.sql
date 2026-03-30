-- ============================================================================
-- finance_db — Full Schema
-- ============================================================================

-- Drop all tables (children first)
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS dividends;
DROP TABLE IF EXISTS estimates;
DROP TABLE IF EXISTS ev;
DROP TABLE IF EXISTS growth;
DROP TABLE IF EXISTS ratios;
DROP TABLE IF EXISTS metrics;
DROP TABLE IF EXISTS income_stmt_growth;
DROP TABLE IF EXISTS cashflow_growth;
DROP TABLE IF EXISTS balance_sheet_growth;
DROP TABLE IF EXISTS cashflow;
DROP TABLE IF EXISTS balance_sheet;
DROP TABLE IF EXISTS income_stmt;
DROP TABLE IF EXISTS dcf_levered;
DROP TABLE IF EXISTS dcf;
DROP TABLE IF EXISTS scores;
DROP TABLE IF EXISTS quotes;
DROP TABLE IF EXISTS companies;

-- ============================================================================
-- COMPANIES (parent table — populate first)
-- source: profile.csv
-- ============================================================================
CREATE TABLE companies (
    ticker                VARCHAR(10) NOT NULL,
    company_name          VARCHAR(255),
    price                 DECIMAL(15,4),
    market_cap            BIGINT,
    beta                  DECIMAL(8,4),
    sector                VARCHAR(100),
    industry              VARCHAR(150),
    country               VARCHAR(50),
    cik                   INT,
    isin                  VARCHAR(20),
    cusip                 VARCHAR(20),
    exchange              VARCHAR(20),
    ceo                   VARCHAR(100),
    full_time_employees   INT,
    ipo_date              DATE,
    description           TEXT,
    PRIMARY KEY (ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- QUOTES (snapshot)
-- source: quote.csv
-- ============================================================================
CREATE TABLE quotes (
    ticker                VARCHAR(10) NOT NULL,
    name                  VARCHAR(255),
    price                 DECIMAL(15,4),
    market_cap            BIGINT,
    year_high             DECIMAL(15,4),
    year_low              DECIMAL(15,4),
    price_avg_50          DECIMAL(15,4),
    price_avg_200         DECIMAL(15,4),
    volume                BIGINT,
    PRIMARY KEY (ticker),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- SCORES (snapshot)
-- source: financial-scores.csv
-- ============================================================================
CREATE TABLE scores (
    ticker                VARCHAR(10) NOT NULL,
    altman_z_score        DECIMAL(10,4),
    piotroski_score       INT,
    working_capital       BIGINT,
    total_assets          BIGINT,
    retained_earnings     BIGINT,
    ebit                  BIGINT,
    market_cap            BIGINT,
    total_liabilities     BIGINT,
    revenue               BIGINT,
    PRIMARY KEY (ticker),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- DCF (time-series)
-- source: discounted-cash-flow.csv
-- ============================================================================
CREATE TABLE dcf (
    ticker                VARCHAR(10) NOT NULL,
    date                  DATE NOT NULL,
    dcf                   DECIMAL(15,4),
    stock_price           DECIMAL(15,4),
    PRIMARY KEY (ticker, date),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- DCF_LEVERED (time-series)
-- source: levered-discounted-cash-flow.csv
-- ============================================================================
CREATE TABLE dcf_levered (
    ticker                VARCHAR(10) NOT NULL,
    date                  DATE NOT NULL,
    levered_dcf           DECIMAL(15,4),
    stock_price           DECIMAL(15,4),
    PRIMARY KEY (ticker, date),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- INCOME_STMT (time-series)
-- source: income-statement.csv
-- ============================================================================
CREATE TABLE income_stmt (
    ticker                      VARCHAR(10) NOT NULL,
    date                        DATE NOT NULL,
    fiscal_year                 VARCHAR(10),
    period                      VARCHAR(10) NOT NULL,
    revenue                     BIGINT,
    cost_of_revenue             BIGINT,
    gross_profit                BIGINT,
    rd_expenses                 BIGINT,
    sga_expenses                BIGINT,
    operating_expenses          BIGINT,
    operating_income            BIGINT,
    interest_income             BIGINT,
    interest_expense            BIGINT,
    depreciation_amortization   BIGINT,
    ebitda                      BIGINT,
    ebit                        BIGINT,
    income_before_tax           BIGINT,
    income_tax_expense          BIGINT,
    net_income                  BIGINT,
    eps                         DECIMAL(10,4),
    eps_diluted                 DECIMAL(10,4),
    shares_outstanding          BIGINT,
    shares_outstanding_diluted  BIGINT,
    PRIMARY KEY (ticker, date, period),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- BALANCE_SHEET (time-series)
-- source: balance-sheet-statement.csv
-- ============================================================================
CREATE TABLE balance_sheet (
    ticker                       VARCHAR(10) NOT NULL,
    date                         DATE NOT NULL,
    fiscal_year                  VARCHAR(10),
    period                       VARCHAR(10) NOT NULL,
    cash                         BIGINT,
    short_term_investments       BIGINT,
    cash_and_short_term_investments BIGINT,
    net_receivables              BIGINT,
    inventory                    BIGINT,
    total_current_assets         BIGINT,
    ppe_net                      BIGINT,
    goodwill                     BIGINT,
    intangible_assets            BIGINT,
    long_term_investments        BIGINT,
    tax_assets                   BIGINT,
    total_non_current_assets     BIGINT,
    total_assets                 BIGINT,
    accounts_payable             BIGINT,
    accrued_expenses             BIGINT,
    short_term_debt              BIGINT,
    deferred_revenue             BIGINT,
    total_current_liabilities    BIGINT,
    long_term_debt               BIGINT,
    total_non_current_liabilities BIGINT,
    total_liabilities            BIGINT,
    retained_earnings            BIGINT,
    additional_paid_in_capital   BIGINT,
    stockholders_equity          BIGINT,
    total_equity                 BIGINT,
    total_debt                   BIGINT,
    net_debt                     BIGINT,
    PRIMARY KEY (ticker, date, period),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- CASHFLOW (time-series)
-- source: cash-flow-statement.csv
-- ============================================================================
CREATE TABLE cashflow (
    ticker                      VARCHAR(10) NOT NULL,
    date                        DATE NOT NULL,
    fiscal_year                 VARCHAR(10),
    period                      VARCHAR(10) NOT NULL,
    net_income                  BIGINT,
    depreciation_amortization   BIGINT,
    stock_based_compensation    BIGINT,
    deferred_income_tax         BIGINT,
    change_in_working_capital   BIGINT,
    cash_from_operations        BIGINT,
    ppe_investments             BIGINT,
    acquisitions_net            BIGINT,
    purchases_of_investments    BIGINT,
    sales_of_investments        BIGINT,
    cash_from_investing         BIGINT,
    net_debt_issuance           BIGINT,
    stock_repurchased           BIGINT,
    dividends_paid              BIGINT,
    cash_from_financing         BIGINT,
    operating_cash_flow         BIGINT,
    capex                       BIGINT,
    free_cash_flow              BIGINT,
    income_taxes_paid           BIGINT,
    interest_paid               BIGINT,
    PRIMARY KEY (ticker, date, period),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- BALANCE_SHEET_GROWTH (time-series)
-- source: balance-sheet-statement-growth.csv
-- ============================================================================
CREATE TABLE balance_sheet_growth (
    ticker                          VARCHAR(10) NOT NULL,
    date                            DATE NOT NULL,
    fiscal_year                     VARCHAR(10),
    period                          VARCHAR(10) NOT NULL,
    growth_total_assets             DECIMAL(12,6),
    growth_total_liabilities        DECIMAL(12,6),
    growth_total_equity             DECIMAL(12,6),
    growth_total_debt               DECIMAL(12,6),
    growth_net_debt                 DECIMAL(12,6),
    growth_total_current_assets     DECIMAL(12,6),
    growth_total_current_liabilities DECIMAL(12,6),
    PRIMARY KEY (ticker, date, period),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- CASHFLOW_GROWTH (time-series)
-- source: cash-flow-statement-growth.csv
-- ============================================================================
CREATE TABLE cashflow_growth (
    ticker                          VARCHAR(10) NOT NULL,
    date                            DATE NOT NULL,
    fiscal_year                     VARCHAR(10),
    period                          VARCHAR(10) NOT NULL,
    growth_operating_cash_flow      DECIMAL(12,6),
    growth_free_cash_flow           DECIMAL(12,6),
    growth_capex                    DECIMAL(12,6),
    growth_net_change_in_cash       DECIMAL(12,6),
    growth_dividends_paid           DECIMAL(12,6),
    PRIMARY KEY (ticker, date, period),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- INCOME_STMT_GROWTH (time-series)
-- source: income-statement-growth.csv
-- ============================================================================
CREATE TABLE income_stmt_growth (
    ticker                          VARCHAR(10) NOT NULL,
    date                            DATE NOT NULL,
    fiscal_year                     VARCHAR(10),
    period                          VARCHAR(10) NOT NULL,
    growth_revenue                  DECIMAL(12,6),
    growth_gross_profit             DECIMAL(12,6),
    growth_operating_income         DECIMAL(12,6),
    growth_net_income               DECIMAL(12,6),
    growth_ebitda                   DECIMAL(12,6),
    growth_eps                      DECIMAL(12,6),
    growth_eps_diluted              DECIMAL(12,6),
    PRIMARY KEY (ticker, date, period),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- METRICS (time-series)
-- source: key-metrics.csv
-- ============================================================================
CREATE TABLE metrics (
    ticker                      VARCHAR(10) NOT NULL,
    date                        DATE NOT NULL,
    fiscal_year                 VARCHAR(10),
    period                      VARCHAR(10) NOT NULL,
    market_cap                  BIGINT,
    enterprise_value            BIGINT,
    ev_to_sales                 DECIMAL(10,4),
    ev_to_ebitda                DECIMAL(10,4),
    ev_to_fcf                   DECIMAL(10,4),
    net_debt_to_ebitda          DECIMAL(10,4),
    current_ratio               DECIMAL(10,4),
    income_quality              DECIMAL(10,4),
    graham_number               DECIMAL(15,4),
    working_capital             BIGINT,
    invested_capital            BIGINT,
    roa                         DECIMAL(10,6),
    roe                         DECIMAL(10,6),
    roic                        DECIMAL(10,6),
    roce                        DECIMAL(10,6),
    earnings_yield              DECIMAL(10,6),
    fcf_yield                   DECIMAL(10,6),
    rd_to_revenue               DECIMAL(10,6),
    sbc_to_revenue              DECIMAL(10,6),
    capex_to_revenue            DECIMAL(10,6),
    days_sales_outstanding      DECIMAL(10,4),
    days_payables_outstanding   DECIMAL(10,4),
    days_inventory_outstanding  DECIMAL(10,4),
    cash_conversion_cycle       DECIMAL(10,4),
    fcf_to_equity               BIGINT,
    fcf_to_firm                 BIGINT,
    tangible_asset_value        BIGINT,
    net_current_asset_value     BIGINT,
    PRIMARY KEY (ticker, date, period),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- RATIOS (time-series)
-- source: ratios.csv
-- ============================================================================
CREATE TABLE ratios (
    ticker                      VARCHAR(10) NOT NULL,
    date                        DATE NOT NULL,
    fiscal_year                 VARCHAR(10),
    period                      VARCHAR(10) NOT NULL,
    -- Margins
    gross_margin                DECIMAL(10,6),
    ebit_margin                 DECIMAL(10,6),
    ebitda_margin               DECIMAL(10,6),
    operating_margin            DECIMAL(10,6),
    net_margin                  DECIMAL(10,6),
    -- Turnover
    receivables_turnover        DECIMAL(10,4),
    payables_turnover           DECIMAL(10,4),
    inventory_turnover          DECIMAL(10,4),
    fixed_asset_turnover        DECIMAL(10,4),
    asset_turnover              DECIMAL(10,4),
    -- Liquidity
    current_ratio               DECIMAL(10,4),
    quick_ratio                 DECIMAL(10,4),
    -- Leverage
    debt_to_equity              DECIMAL(10,4),
    debt_to_assets              DECIMAL(10,4),
    financial_leverage          DECIMAL(10,4),
    interest_coverage           DECIMAL(10,4),
    -- Valuation
    pe_ratio                    DECIMAL(10,4),
    pb_ratio                    DECIMAL(10,4),
    ps_ratio                    DECIMAL(10,4),
    p_to_fcf                    DECIMAL(10,4),
    ev_multiple                 DECIMAL(10,4),
    -- Cash flow quality
    ocf_to_sales                DECIMAL(10,6),
    fcf_to_ocf                  DECIMAL(10,6),
    -- Dividend
    dividend_payout_ratio       DECIMAL(10,6),
    dividend_yield              DECIMAL(10,6),
    -- Tax
    effective_tax_rate          DECIMAL(10,6),
    PRIMARY KEY (ticker, date, period),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- GROWTH (time-series)
-- source: financial-growth.csv
-- ============================================================================
CREATE TABLE growth (
    ticker                      VARCHAR(10) NOT NULL,
    date                        DATE NOT NULL,
    fiscal_year                 VARCHAR(10),
    period                      VARCHAR(10) NOT NULL,
    revenue_growth              DECIMAL(12,6),
    gross_profit_growth         DECIMAL(12,6),
    operating_income_growth     DECIMAL(12,6),
    net_income_growth           DECIMAL(12,6),
    eps_diluted_growth          DECIMAL(12,6),
    ebitda_growth               DECIMAL(12,6),
    operating_cf_growth         DECIMAL(12,6),
    fcf_growth                  DECIMAL(12,6),
    -- Multi-year CAGRs
    revenue_cagr_3y             DECIMAL(12,6),
    revenue_cagr_5y             DECIMAL(12,6),
    revenue_cagr_10y            DECIMAL(12,6),
    net_income_cagr_3y          DECIMAL(12,6),
    net_income_cagr_5y          DECIMAL(12,6),
    net_income_cagr_10y         DECIMAL(12,6),
    operating_cf_cagr_3y        DECIMAL(12,6),
    operating_cf_cagr_5y        DECIMAL(12,6),
    operating_cf_cagr_10y       DECIMAL(12,6),
    PRIMARY KEY (ticker, date, period),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- EV (time-series)
-- source: enterprise-values.csv
-- ============================================================================
CREATE TABLE ev (
    ticker                      VARCHAR(10) NOT NULL,
    date                        DATE NOT NULL,
    stock_price                 DECIMAL(15,4),
    shares_outstanding          BIGINT,
    market_cap                  BIGINT,
    minus_cash                  BIGINT,
    plus_total_debt             BIGINT,
    enterprise_value            BIGINT,
    PRIMARY KEY (ticker, date),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- ESTIMATES (event time-series)
-- source: analyst-estimates.csv
-- ============================================================================
CREATE TABLE estimates (
    ticker                      VARCHAR(10) NOT NULL,
    date                        DATE NOT NULL,
    est_revenue_avg             BIGINT,
    est_ebitda_avg              BIGINT,
    est_net_income_avg          BIGINT,
    est_eps_avg                 DECIMAL(10,4),
    num_analysts_revenue        INT,
    num_analysts_eps            INT,
    PRIMARY KEY (ticker, date),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- DIVIDENDS (event time-series)
-- source: dividends.csv
-- ============================================================================
CREATE TABLE dividends (
    ticker                      VARCHAR(10) NOT NULL,
    date                        DATE NOT NULL,
    adj_dividend                DECIMAL(10,4),
    dividend                    DECIMAL(10,4),
    dividend_yield              DECIMAL(10,6),
    frequency                   VARCHAR(20),
    PRIMARY KEY (ticker, date),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================================
-- RATINGS (event time-series)
-- source: ratings-historical.csv
-- ============================================================================
CREATE TABLE ratings (
    ticker                      VARCHAR(10) NOT NULL,
    date                        DATE NOT NULL,
    rating                      VARCHAR(10),
    overall_score               INT,
    dcf_score                   INT,
    roe_score                   INT,
    roa_score                   INT,
    de_score                    INT,
    pe_score                    INT,
    pb_score                    INT,
    PRIMARY KEY (ticker, date),
    FOREIGN KEY (ticker) REFERENCES companies(ticker)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


ALTER TABLE companies MODIFY beta DECIMAL(20,10);
ALTER TABLE scores MODIFY altman_z_score DECIMAL(20,10);

-- Widen all DECIMAL columns that are overflowing
ALTER TABLE metrics MODIFY roa DECIMAL(20,10);
ALTER TABLE metrics MODIFY roe DECIMAL(20,10);
ALTER TABLE metrics MODIFY roic DECIMAL(20,10);
ALTER TABLE metrics MODIFY roce DECIMAL(20,10);
ALTER TABLE metrics MODIFY earnings_yield DECIMAL(20,10);
ALTER TABLE metrics MODIFY fcf_yield DECIMAL(20,10);
ALTER TABLE metrics MODIFY rd_to_revenue DECIMAL(20,10);
ALTER TABLE metrics MODIFY sbc_to_revenue DECIMAL(20,10);
ALTER TABLE metrics MODIFY capex_to_revenue DECIMAL(20,10);
ALTER TABLE metrics MODIFY ev_to_sales DECIMAL(20,10);
ALTER TABLE metrics MODIFY ev_to_ebitda DECIMAL(20,10);
ALTER TABLE metrics MODIFY ev_to_fcf DECIMAL(20,10);

ALTER TABLE ratios MODIFY gross_margin DECIMAL(20,10);
ALTER TABLE ratios MODIFY ebit_margin DECIMAL(20,10);
ALTER TABLE ratios MODIFY ebitda_margin DECIMAL(20,10);
ALTER TABLE ratios MODIFY operating_margin DECIMAL(20,10);
ALTER TABLE ratios MODIFY net_margin DECIMAL(20,10);
ALTER TABLE ratios MODIFY ocf_to_sales DECIMAL(20,10);
ALTER TABLE ratios MODIFY fcf_to_ocf DECIMAL(20,10);
ALTER TABLE ratios MODIFY dividend_payout_ratio DECIMAL(20,10);
ALTER TABLE ratios MODIFY dividend_yield DECIMAL(20,10);
ALTER TABLE ratios MODIFY effective_tax_rate DECIMAL(20,10);

ALTER TABLE growth MODIFY revenue_cagr_3y DECIMAL(20,10);
ALTER TABLE growth MODIFY revenue_cagr_5y DECIMAL(20,10);
ALTER TABLE growth MODIFY revenue_cagr_10y DECIMAL(20,10);
ALTER TABLE growth MODIFY net_income_cagr_3y DECIMAL(20,10);
ALTER TABLE growth MODIFY net_income_cagr_5y DECIMAL(20,10);
ALTER TABLE growth MODIFY net_income_cagr_10y DECIMAL(20,10);
ALTER TABLE growth MODIFY operating_cf_cagr_3y DECIMAL(20,10);
ALTER TABLE growth MODIFY operating_cf_cagr_5y DECIMAL(20,10);
ALTER TABLE growth MODIFY operating_cf_cagr_10y DECIMAL(20,10);
ALTER TABLE growth MODIFY revenue_growth DECIMAL(20,10);
ALTER TABLE growth MODIFY operating_income_growth DECIMAL(20,10);
ALTER TABLE growth MODIFY net_income_growth DECIMAL(20,10);
ALTER TABLE growth MODIFY operating_cf_growth DECIMAL(20,10);
ALTER TABLE growth MODIFY fcf_growth DECIMAL(20,10);

ALTER TABLE ev MODIFY stock_price DECIMAL(20,10);

ALTER TABLE estimates MODIFY est_eps_avg DECIMAL(20,10);

ALTER TABLE dividends MODIFY dividend_yield DECIMAL(20,10);