# Azure Data Factory - Banking Fraud Analytics

## Overview

This folder contains the Azure Data Factory (ADF) pipeline used in the Banking Fraud Analytics project.

Azure Data Factory orchestrates data ingestion from the source system into Azure Data Lake Storage Gen2 (ADLS Gen2), providing raw data for downstream processing in Azure Databricks.

---

## Components

- Azure Data Factory
- Linked Services
- Datasets
- Pipelines
- Lookup Activity
- Copy Data Activity

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
- Uses Lookup Activity to retrieve metadata or configuration
- Copies source data to ADLS Gen2 using Copy Data Activity
- Prepares raw data for Azure Databricks processing

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

- Pipeline orchestration
- Lookup Activity
- Copy Data Activity
- Automated data ingestion
- Cloud-based ETL workflow

---

## Key Achievements

- Built an automated data ingestion pipeline
- Loaded source data into ADLS Gen2
- Integrated Azure Data Factory with Azure Data Lake Storage Gen2
- Enabled downstream Databricks processing
