# Azure Databricks - Banking Fraud Analytics

## Overview

This module implements the data processing layer of the Banking Fraud Analytics platform using Azure Databricks and Delta Lake.

The solution follows a Medallion Architecture (Bronze → Silver → Gold) to ingest, clean, transform, enrich, and prepare banking data for analytics.

Databricks processes customer, account, and transaction data using PySpark, Delta Live Tables (DLT), Auto Loader, CDC processing, and SCD Type 1/Type 2 implementation.

---

# Databricks Architecture
MySQL Source
|
|
Azure Data Factory
|
|
ADLS Gen2 Landing Zone
|
|
Azure Databricks
|
|
+----------------+
| Bronze Layer |
| Raw Ingestion |
+----------------+
|
|
+----------------+
| Silver Layer |
| Cleaning |
| Validation |
| Transformation|
+----------------+
|
|
+----------------+
| Gold Layer |
| SCD + Facts |
| Analytics |
+----------------+

---

# Databricks Components Used

| Component | Purpose |
|-----------|---------|
| Azure Databricks | Data processing platform |
| PySpark | Data transformation |
| Delta Lake | ACID transaction storage |
| Delta Live Tables | Managed ETL pipelines |
| Auto Loader | Incremental file ingestion |
| Structured Streaming | Real-time processing |
| Change Data Feed | Change tracking |
| MERGE | CDC upsert processing |

---

# Catalog and Schema Setup

## Foreign Catalog

Created connection to MySQL source using Databricks Foreign Catalog.
banking_foreign_catalog
|
|
bank_raji_schema
|
|
dim_customer
dim_account

---

# Medallion Architecture

## Bronze Layer

Purpose:

- Store raw source data
- Maintain ingestion history
- Support incremental loading


Tables:
banking_bronze.dim_customer_bronze

banking_bronze.bronze_dim_account

banking_bronze.transactions_bronze_tbl


Features:

- Incremental loading
- Watermark-based CDC
- Raw data preservation


Example:

```sql
INSERT INTO banking_bronze.dim_customer_bronze
SELECT *
FROM banking_foreign_catalog.bank_raji_schema.dim_customer
WHERE updated_at >
(
SELECT COALESCE(MAX(updated_at),'1900-01-01')
FROM banking_bronze.dim_customer_bronze
)
```

---

# Silver Layer

Purpose:

- Clean raw data
- Apply business rules
- Remove duplicates
- Standardize columns

Table:
banking_silver.dim_customer_silver

Transformations:
---Customer name masking
---KYC standardization
---Duplicate removal
---Data validation
---Transaction Silver

Table:
  banking_silver.transactions_silver_tbl

Transformations:

Timestamp conversion
--Watermarking
--Duplicate prevention
--Transaction status derivation
--Amount bucket creation

Example:
LOW
MEDIUM
HIGH
# Delta Live Tables (DLT)

## Account Silver Pipeline

DLT performs:
---Data quality validation
---Streaming ingestion
---Deduplication
---Standardization

Table:
banking_silver.dim_account_silver
Example:

```python
@dlt.expect_or_drop(
    "valid_account_id",
    "ACCOUNT_ID IS NOT NULL"
)
```

# Gold Layer

## Account SCD Type 1

Table:
banking_gold.dim_account_gold_scd1
Implementation:
dlt.apply_changes()

Features:
---Current state maintenance
---Latest record overwrite
---CDC processing

Configuration:
keys = ACCOUNT_ID

sequence_by = updated_at

stored_as_scd_type = 1

## Account SCD Type 2

Table:
banking_gold.dim_account_gold_scd2
Purpose:

Maintain historical account changes.

Features:
stored_as_scd_type = 2
Tracked Columns:
---TYPE
---BALANCE
---STATUS
---Customer SCD Processing

Tables:
 banking_gold.dim_customer_gold_scd1

banking_gold.dim_customer_gold_scd2

Implemented using:
--Delta MERGE
--Hash comparison
--CDC logic
## Transaction Streaming Pipeline

Notebook:
--3_Fact_Medallion_Realtime_Autoload

Sources:
ATM Transactions

Credit Card Stream
Processing:
Auto Loader
      |
      |
Bronze Streaming
      |
      |
Silver Streaming
      |
      |
Gold Fact Streaming

Features:
--CloudFiles ingestion
--Checkpoint management
--Watermarking
--Duplicate protection

banking_gold.fact_wide_transactions
Contains:
--Transaction details
--Customer attributes
--Account attributes
--Risk information

Account Transaction Aggregation:
 banking_gold.fact_account_transactions

Metrics:
--Transaction count
--Total amount
--Average amount
--Successful transactions

Databricks Notebooks
```text
Banking_Fraud_Analytics/

├── 0_First_Time_Run
├── 1_Notebook_Dim_Customer_Pyspark_CDC_SCD_CDF_Bronze_Silver_Gold
├── 1_Notebook_Dim_Account_CDC_Bronze
├── DLT_Account_Silver
├── DLT_Account_Gold_SCD1
├── DLT_Account_Gold_SCD2
├── 3_Fact_Medallion_Realtime_Autoload
├── 4_Update_banking_gold_fact_wide_transactions_post_dim_load
├── 5_Analytics_Notebook
├── 6_Validation_Notebook
└── 7_FACT_NOTEBOOK_BATCH_VERSION
```

# Integration

Databricks Gold layer data is consumed by:

- Azure Synapse Dedicated SQL Pool
- Power BI Dashboard

for fraud monitoring and risk analytics.

# Data Quality Checks

Implemented validations:

--Null key checks
--Duplicate removal
--Schema validation
--Transaction timestamp validation
--CDC watermark validation

Final Databricks Flow:
Source Data
    |
    ▼
Bronze Delta Tables
    |
    ▼
Silver Transformation
    |
    ▼
Gold Dimensions + Facts
    |
    ▼
Synapse Analytics
    |
    ▼
Power BI Dashboard

Key Achievements

✅ Built Medallion Architecture
✅ Implemented CDC processing
✅ Implemented SCD Type 1 & Type 2
✅ Built DLT pipelines
✅ Implemented Auto Loader streaming
✅ Created analytics-ready Gold datasets
