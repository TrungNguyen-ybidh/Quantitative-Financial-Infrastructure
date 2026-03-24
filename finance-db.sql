-- MySQL dump 10.13  Distrib 9.6.0, for macos26.2 (arm64)
--
-- Host: 127.0.0.1    Database: finance_db
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `analyst_ratings`
--

DROP TABLE IF EXISTS `analyst_ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analyst_ratings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cik` int NOT NULL,
  `ticker` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `firm` varchar(100) DEFAULT NULL,
  `analyst` varchar(100) DEFAULT NULL,
  `rating` varchar(50) DEFAULT NULL,
  `previous_rating` varchar(50) DEFAULT NULL,
  `action` enum('init','upgrade','downgrade','maintain','reiterate') DEFAULT NULL,
  `price_target` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cik` (`cik`),
  CONSTRAINT `analyst_ratings_ibfk_1` FOREIGN KEY (`cik`) REFERENCES `companies` (`cik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analyst_ratings`
--

LOCK TABLES `analyst_ratings` WRITE;
/*!40000 ALTER TABLE `analyst_ratings` DISABLE KEYS */;
/*!40000 ALTER TABLE `analyst_ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `balance_sheet`
--

DROP TABLE IF EXISTS `balance_sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `balance_sheet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cik` int NOT NULL,
  `ticker` varchar(10) NOT NULL,
  `period_date` date NOT NULL,
  `period_type` enum('annual','quarterly') NOT NULL,
  `cash` bigint DEFAULT NULL,
  `short_term_investment` bigint DEFAULT NULL,
  `total_current_asset` bigint DEFAULT NULL,
  `total_assets` bigint DEFAULT NULL,
  `total_current_liabilities` bigint DEFAULT NULL,
  `total_liabilities` bigint DEFAULT NULL,
  `total_equity` bigint DEFAULT NULL,
  `total_debt` bigint DEFAULT NULL,
  `net_debt` bigint DEFAULT NULL,
  `retained_earnings` bigint DEFAULT NULL,
  `fiscal_year` varchar(10) DEFAULT NULL,
  `goodwill` bigint DEFAULT NULL,
  `intangible_assets` bigint DEFAULT NULL,
  `ppe_net` bigint DEFAULT NULL,
  `long_term_debt` bigint DEFAULT NULL,
  `short_term_debt` bigint DEFAULT NULL,
  `stockholders_equity` bigint DEFAULT NULL,
  `accounts_payable` bigint DEFAULT NULL,
  `inventory` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cik` (`cik`),
  CONSTRAINT `balance_sheet_ibfk_1` FOREIGN KEY (`cik`) REFERENCES `companies` (`cik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `balance_sheet`
--

LOCK TABLES `balance_sheet` WRITE;
/*!40000 ALTER TABLE `balance_sheet` DISABLE KEYS */;
/*!40000 ALTER TABLE `balance_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cash_flow`
--

DROP TABLE IF EXISTS `cash_flow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cash_flow` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cik` int NOT NULL,
  `ticker` varchar(10) NOT NULL,
  `period_date` date NOT NULL,
  `period_type` enum('annual','quarterly') DEFAULT NULL,
  `operating_cash_flow` bigint DEFAULT NULL,
  `investing_cash_flow` bigint DEFAULT NULL,
  `financing_cash_flow` bigint DEFAULT NULL,
  `free_cash_flow` bigint DEFAULT NULL,
  `capex` bigint DEFAULT NULL,
  `dividends_paid` bigint DEFAULT NULL,
  `net_change_in_cash` bigint DEFAULT NULL,
  `fiscal_year` varchar(10) DEFAULT NULL,
  `net_income` bigint DEFAULT NULL,
  `depreciation_amortization` bigint DEFAULT NULL,
  `stock_based_compensation` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cik` (`cik`),
  CONSTRAINT `cash_flow_ibfk_1` FOREIGN KEY (`cik`) REFERENCES `companies` (`cik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cash_flow`
--

LOCK TABLES `cash_flow` WRITE;
/*!40000 ALTER TABLE `cash_flow` DISABLE KEYS */;
/*!40000 ALTER TABLE `cash_flow` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companies` (
  `cik` int NOT NULL,
  `ticker` varchar(10) NOT NULL,
  `name` varchar(255) NOT NULL,
  `sector` varchar(100) DEFAULT NULL,
  `industry` varchar(150) DEFAULT NULL,
  `exchange` varchar(20) DEFAULT NULL,
  `country` varchar(50) DEFAULT 'US',
  `currency` varchar(10) DEFAULT 'USD',
  `market_cap` bigint DEFAULT NULL,
  `ipo_date` date DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_etf` tinyint(1) DEFAULT '0',
  `is_adr` tinyint(1) DEFAULT '0',
  `is_fund` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`cik`),
  UNIQUE KEY `ticker` (`ticker`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `country_id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `iso_code` char(3) NOT NULL,
  `name` varchar(100) NOT NULL,
  `region` varchar(50) DEFAULT NULL,
  `currency` char(3) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`country_id`),
  UNIQUE KEY `iso_code` (`iso_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cpi`
--

DROP TABLE IF EXISTS `cpi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cpi` (
  `cpi_id` int unsigned NOT NULL AUTO_INCREMENT,
  `country_id` smallint unsigned NOT NULL,
  `date` date NOT NULL,
  `cpi_headline` decimal(10,4) DEFAULT NULL,
  `core_cpi` decimal(10,4) DEFAULT NULL,
  `cpi_food` decimal(10,4) DEFAULT NULL,
  `cpi_energy` decimal(10,4) DEFAULT NULL,
  `pce_headline` decimal(10,4) DEFAULT NULL,
  `core_pce` decimal(10,4) DEFAULT NULL,
  `cpi_headline_yoy` decimal(8,4) DEFAULT NULL,
  `cpi_headline_mom` decimal(8,4) DEFAULT NULL,
  `core_cpi_yoy` decimal(8,4) DEFAULT NULL,
  `core_cpi_mom` decimal(8,4) DEFAULT NULL,
  PRIMARY KEY (`cpi_id`),
  UNIQUE KEY `uq_country_date` (`country_id`,`date`),
  CONSTRAINT `cpi_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cpi`
--

LOCK TABLES `cpi` WRITE;
/*!40000 ALTER TABLE `cpi` DISABLE KEYS */;
/*!40000 ALTER TABLE `cpi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dividends`
--

DROP TABLE IF EXISTS `dividends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dividends` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cik` int NOT NULL,
  `ticker` varchar(10) NOT NULL,
  `ex_date` date NOT NULL,
  `payment_date` date DEFAULT NULL,
  `record_date` date DEFAULT NULL,
  `declaration_date` date DEFAULT NULL,
  `amount` decimal(10,4) DEFAULT NULL,
  `frequency` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cik` (`cik`),
  CONSTRAINT `dividends_ibfk_1` FOREIGN KEY (`cik`) REFERENCES `companies` (`cik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dividends`
--

LOCK TABLES `dividends` WRITE;
/*!40000 ALTER TABLE `dividends` DISABLE KEYS */;
/*!40000 ALTER TABLE `dividends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `financial_ratios`
--

DROP TABLE IF EXISTS `financial_ratios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `financial_ratios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cik` int NOT NULL,
  `ticker` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `beta` decimal(6,4) DEFAULT NULL,
  `pe_ratio` decimal(10,4) DEFAULT NULL,
  `pb_ratio` decimal(10,4) DEFAULT NULL,
  `ps_ratio` decimal(10,4) DEFAULT NULL,
  `ev_ebitda` decimal(10,4) DEFAULT NULL,
  `ev_revenue` decimal(10,4) DEFAULT NULL,
  `roe` decimal(10,4) DEFAULT NULL,
  `roa` decimal(10,4) DEFAULT NULL,
  `debt_to_equity` decimal(10,4) DEFAULT NULL,
  `current_ratio` decimal(10,4) DEFAULT NULL,
  `gross_margin` decimal(10,4) DEFAULT NULL,
  `net_margin` decimal(10,4) DEFAULT NULL,
  `asset_turnover` decimal(10,4) DEFAULT NULL,
  `interest_coverage` decimal(10,4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cik` (`cik`),
  CONSTRAINT `financial_ratios_ibfk_1` FOREIGN KEY (`cik`) REFERENCES `companies` (`cik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `financial_ratios`
--

LOCK TABLES `financial_ratios` WRITE;
/*!40000 ALTER TABLE `financial_ratios` DISABLE KEYS */;
/*!40000 ALTER TABLE `financial_ratios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gdp`
--

DROP TABLE IF EXISTS `gdp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gdp` (
  `gdp_id` int unsigned NOT NULL AUTO_INCREMENT,
  `country_id` smallint unsigned NOT NULL,
  `date` date NOT NULL,
  `nominal_gdp` decimal(20,4) DEFAULT NULL,
  `real_gdp` decimal(20,4) DEFAULT NULL,
  `gdp_price_deflator` decimal(10,4) DEFAULT NULL,
  `nominal_gdp_per_capita` decimal(14,4) DEFAULT NULL,
  `real_gdp_per_capita` decimal(14,4) DEFAULT NULL,
  `real_potential_gdp` decimal(20,4) DEFAULT NULL,
  `real_gdp_growth_rate` decimal(8,4) DEFAULT NULL,
  PRIMARY KEY (`gdp_id`),
  UNIQUE KEY `uq_country_date` (`country_id`,`date`),
  CONSTRAINT `gdp_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gdp`
--

LOCK TABLES `gdp` WRITE;
/*!40000 ALTER TABLE `gdp` DISABLE KEYS */;
/*!40000 ALTER TABLE `gdp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `income_statement`
--

DROP TABLE IF EXISTS `income_statement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `income_statement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cik` int NOT NULL,
  `ticker` varchar(10) NOT NULL,
  `period_date` date NOT NULL,
  `period_type` enum('annual','quarterly') DEFAULT NULL,
  `revenue` bigint DEFAULT NULL,
  `cost_of_revenue` bigint DEFAULT NULL,
  `gross_profit` bigint DEFAULT NULL,
  `operating_expense` bigint DEFAULT NULL,
  `operating_income` bigint DEFAULT NULL,
  `net_income` bigint DEFAULT NULL,
  `ebitda` bigint DEFAULT NULL,
  `eps` decimal(10,4) DEFAULT NULL,
  `shares_outstanding` bigint DEFAULT NULL,
  `fiscal_year` varchar(10) DEFAULT NULL,
  `depreciation_amortization` bigint DEFAULT NULL,
  `income_tax_expense` bigint DEFAULT NULL,
  `income_before_tax` bigint DEFAULT NULL,
  `interest_expense` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cik` (`cik`),
  CONSTRAINT `income_statement_ibfk_1` FOREIGN KEY (`cik`) REFERENCES `companies` (`cik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `income_statement`
--

LOCK TABLES `income_statement` WRITE;
/*!40000 ALTER TABLE `income_statement` DISABLE KEYS */;
/*!40000 ALTER TABLE `income_statement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `macro_indicators`
--

DROP TABLE IF EXISTS `macro_indicators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `macro_indicators` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `indicator` varchar(100) NOT NULL,
  `value` decimal(20,6) DEFAULT NULL,
  `country` varchar(50) DEFAULT 'US',
  `source` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_indicator_date` (`indicator`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `macro_indicators`
--

LOCK TABLES `macro_indicators` WRITE;
/*!40000 ALTER TABLE `macro_indicators` DISABLE KEYS */;
/*!40000 ALTER TABLE `macro_indicators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `price_daily`
--

DROP TABLE IF EXISTS `price_daily`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `price_daily` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cik` int NOT NULL,
  `ticker` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `open` decimal(15,4) DEFAULT NULL,
  `high` decimal(15,4) DEFAULT NULL,
  `low` decimal(15,4) DEFAULT NULL,
  `close` decimal(15,4) DEFAULT NULL,
  `adj_close` decimal(15,4) DEFAULT NULL,
  `volume` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_ticker_date` (`ticker`,`date`),
  KEY `cik` (`cik`),
  CONSTRAINT `price_daily_ibfk_1` FOREIGN KEY (`cik`) REFERENCES `companies` (`cik`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `price_daily`
--

LOCK TABLES `price_daily` WRITE;
/*!40000 ALTER TABLE `price_daily` DISABLE KEYS */;
/*!40000 ALTER TABLE `price_daily` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-24 14:14:30
