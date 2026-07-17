# Power BI Dashboard - Banking Fraud Analytics

## Overview

This folder contains the Power BI dashboard developed for the Banking Fraud Analytics platform.

The dashboard provides fraud monitoring, customer risk analysis, transaction insights, and business-level analytics using data from the Azure Synapse Analytics Gold layer.

---

## Dashboard Features

### Fraud Overview
- Total Transactions KPI
- Fraud Transactions
- High Risk Customers
- Transaction Volume Analysis

### Transaction Analysis
- Transaction Trend Analysis
- Transaction Status Analysis
- Amount Bucket Analysis
- Merchant Category Analysis

### Customer Risk Analysis
- Customer Risk Score Analysis
- KYC Status Monitoring
- High Risk Customer Identification

### Synapse MV Analytics
- Materialized View based analytics
- Aggregated fraud metrics
- Performance optimized reporting

---

## Data Source

Power BI connects with:

- Azure Synapse Dedicated SQL Pool
- Gold Layer Tables
- Materialized View (`mv_fraud_aggregates`)

---

## Files

```text
PowerBI/

├── README.md
└── Banking_Fraud_Dashboard.pbix
```
## Project Flow
Azure Databricks Gold Layer
          |
          ▼
Azure Synapse Analytics
          |
          ▼
Power BI Dashboard
## Dashboard Pages:
Fraud Overview
Transaction Analysis
Customer Risk Analysis
Synapse MV Analytics

## Key Insights:
Monitors overall transaction activity
Identifies high-risk customers
Analyzes fraud patterns
Provides transaction and merchant insights
Supports fraud investigation decisions
