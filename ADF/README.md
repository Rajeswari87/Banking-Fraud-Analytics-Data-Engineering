# Azure Data Factory - Banking Fraud Analytics

## Overview

This folder contains the Azure Data Factory (ADF) pipelines used in the Banking Fraud Analytics project.

Azure Data Factory orchestrates data ingestion from the source system into Azure Data Lake Storage Gen2, providing the raw data required for downstream processing in Azure Databricks.

---

## Components

- Azure Data Factory
- Linked Services
- Datasets
- Pipelines
- Copy Activity
- Lookup Activity
- Get Metadata Activity

---

## Source System

- MySQL Database

---

## Destination

- Azure Data Lake Storage Gen2 (ADLS Gen2)

---

## Pipeline

### PL_Ingest_CoreBanking

The pipeline performs the following tasks:

- Reads source data from MySQL
- Extracts Customer and Account data
- Loads raw data into ADLS Gen2
- Supports incremental data ingestion
- Prepares data for Azure Databricks processing

---

## Files

```text
ADF/

├── README.md
└── PL_Ingest_CoreBanking.json
```

---

## Data Flow

```text
MySQL Database
        |
        ▼
Azure Data Factory
        |
        ▼
Azure Data Lake Storage Gen2
        |
        ▼
Azure Databricks
```

---

## Features

- Automated data ingestion
- Pipeline orchestration
- Linked Services
- Dataset management
- Incremental data loading
- Cloud-based ETL

---

## Key Achievements

- Built an automated ingestion pipeline
- Loaded source data into ADLS Gen2
- Enabled downstream Databricks processing
- Integrated Azure Data Factory with Azure Data Lake Storage Gen2
