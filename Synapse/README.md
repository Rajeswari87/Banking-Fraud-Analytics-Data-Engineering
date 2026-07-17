# Azure Synapse Analytics - Banking Fraud Analytics

## Overview

This folder contains the Azure Synapse Analytics SQL scripts used in the Banking Fraud Analytics project.

Azure Synapse Dedicated SQL Pool is used to store Gold layer data from Azure Databricks and provide a high-performance analytical layer for Power BI reporting.

---

## Components

- Azure Synapse Dedicated SQL Pool
- SQL Tables
- Materialized View
- Analytics Queries

---

## Database Objects

### Dimension Tables

- dim_customer_gold_scd1
- dim_customer_gold_scd2
- dim_account_gold_scd1
- dim_account_gold_scd2

### Fact Tables

- fact_wide_transactions
- fact_account_transactions

### Materialized View

- mv_fraud_aggregates

---

## Materialized View

The materialized view aggregates transaction data by merchant category and customer risk score to improve reporting performance.

**Materialized View:**

- mv_fraud_aggregates

---

## Data Source

Azure Synapse receives data from:

- Azure Databricks Gold Layer
- Delta Lake Gold Tables

---

## Files

```text
Synapse/

├── README.md
└── Synapse_SQL_Scripts.sql
```
## Data Flow

```text
Azure Databricks Gold Layer
          |
          ▼
Azure Synapse Dedicated SQL Pool
          |
          ▼
Materialized Views
          |
          ▼
Power BI Dashboard
```

---

## Features

- Dedicated SQL Pool
- Gold Layer Data Warehouse
- Fact and Dimension Modeling
- Materialized View Optimization
- Analytics-ready Data Model
- High-performance SQL Queries

---

## Key Achievements

- Created analytical data warehouse
- Loaded Gold layer tables into Synapse
- Built fact and dimension tables
- Created materialized views for optimized reporting
- Enabled Power BI reporting using Synapse
