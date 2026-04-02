<div align="center">

# QuantFinance-Databases

**A centralized financial data warehouse for quantitative research and algorithmic trading**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

*Aggregating equity fundamentals, market data, and macroeconomic indicators across U.S. equities into a unified, queryable data warehouse.*

---

</div>

## Overview

**QuantFinance-Databases** is a systematic financial data infrastructure that ingests, cleans, and stores multi-source financial data into a MySQL data warehouse containerized with Docker. It serves as the foundational data layer for quantitative research, factor modeling, and algorithmic trading strategies.

The pipeline aggregates data from **5 financial APIs** — FMP, SEC EDGAR, Polygon, yfinance, and FRED — providing comprehensive coverage of equity fundamentals, historical price data, and macroeconomic indicators for U.S. equities.

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA SOURCES                                │
│  ┌─────────┐ ┌───────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐  │
│  │   FMP   │ │ SEC EDGAR │ │ Polygon │ │ yfinance │ │   FRED   │  │
│  └────┬────┘ └─────┬─────┘ └────┬────┘ └─────┬────┘ └────┬─────┘  │
│       │             │            │             │            │        │
│       ▼             ▼            ▼             ▼            ▼        │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                     FETCHERS (Python ETL)                    │   │
│  │          API clients  ·  rate limiting  ·  pagination        │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                     CLEANERS (Transform)                     │   │
│  │      normalization  ·  type casting  ·  deduplication        │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
│                             │                                       │
│                             ▼                                       │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │              MySQL DATA WAREHOUSE (Docker)                   │   │
│  │   equities · financials · prices · macro · SEC filings       │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Coverage

| Domain | Source | Data Type |
|---|---|---|
| **Equity Fundamentals** | FMP API | Income statements, balance sheets, cash flow statements, key metrics, company profiles |
| **SEC Filings** | SEC EDGAR | 10-K, 10-Q filings and structured financial data |
| **Market Data** | Polygon, yfinance | Historical OHLCV price data, splits, dividends |
| **Macroeconomic Indicators** | FRED API | GDP, CPI, unemployment, interest rates, yield curves |

## Project Structure

```
QuantFinance-Databases/
├── fetchers/           # API client modules for each data source
├── cleaners/           # Data transformation and normalization scripts
├── config/             # Database connection settings and API configurations
├── data/               # Local data staging directory
├── test/               # Test notebooks and validation scripts
├── finance-db.sql      # MySQL schema definition
├── pyproject.toml      # Package configuration
└── requirement.txt     # Python dependencies
```

## Getting Started

### Prerequisites

- **Python 3.10+**
- **Docker** (for MySQL container)
- API keys for: [FMP](https://financialmodelingprep.com/), [FRED](https://fred.stlouisfed.org/docs/api/api_key.html)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TrungNguyen-ybidh/QuantFinance-Databases.git
   cd QuantFinance-Databases
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root:
   ```env
   FMP_api=your_fmp_api_key
   FRED_api=your_fred_api_key
   ```

4. **Start the MySQL container**
   ```bash
   docker run -d --name finance-db \
     -e MYSQL_ROOT_PASSWORD=yourpassword \
     -e MYSQL_DATABASE=finance_db \
     -p 3306:3306 \
     mysql:8.0
   ```

5. **Initialize the database schema**
   ```bash
   mysql -h 127.0.0.1 -u root -p finance_db < finance-db.sql
   ```

6. **Run the ETL pipeline**

   Use the fetcher modules to ingest data and the cleaner modules to transform it into the warehouse.

## Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **Database** | MySQL 8.0 |
| **ORM / DB Access** | SQLAlchemy, PyMySQL |
| **Containerization** | Docker |
| **Data Processing** | pandas, NumPy, PyArrow |
| **Visualization** | matplotlib, seaborn |
| **API Clients** | requests, httpx, yfinance, fredapi, edgartools |
| **Config Management** | python-dotenv |

## Key Dependencies

Core libraries powering the pipeline:

- `SQLAlchemy` — Database ORM and connection management
- `pandas` / `PyArrow` — High-performance data manipulation
- `yfinance` — Yahoo Finance market data
- `fredapi` — Federal Reserve Economic Data
- `edgartools` — SEC EDGAR filings parser
- `httpx` / `requests` — Async and sync HTTP clients for API calls
- `python-dotenv` — Environment variable management

## Roadmap

- [ ] Add Docker Compose for one-command deployment
- [ ] Implement incremental data loading (upsert logic)
- [ ] Add Airflow/Prefect orchestration for scheduled ETL runs
- [ ] Expand coverage to ETFs and options data
- [ ] Build a REST API layer for querying the warehouse

## Contributing

Contributions are welcome. Please open an issue to discuss proposed changes before submitting a pull request.

## License

This project is open source. See the repository for license details.

---

<div align="center">

**Built for quantitative research and algorithmic trading.**

</div>
