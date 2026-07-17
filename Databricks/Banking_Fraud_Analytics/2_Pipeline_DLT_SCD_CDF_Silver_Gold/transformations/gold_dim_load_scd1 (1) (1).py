import dlt

# ==========================================================
# GOLD LAYER : ACCOUNT SCD TYPE 1
# ==========================================================

# 1. Create Gold Streaming Table
dlt.create_streaming_table(

    name = "dim_account_gold_scd1",

    comment = "Current account master data using SCD Type 1",

    table_properties = {
        "delta.enableChangeDataFeed": "true"
    }

)

# 2. Apply CDC Changes from Silver Layer
dlt.apply_changes(

    # Target Gold table
    target = "dim_account_gold_scd1",

    # Source Silver table
    source = "banking_silver.dim_account_silver",

    # Primary Key
    keys = ["ACCOUNT_ID"],

    # Latest updated record wins
    sequence_by = "updated_at",

    # Delete inactive accounts
    apply_as_deletes = "STATUS = 'INACTIVE'",

    # SCD Type 1
    stored_as_scd_type = 1

)