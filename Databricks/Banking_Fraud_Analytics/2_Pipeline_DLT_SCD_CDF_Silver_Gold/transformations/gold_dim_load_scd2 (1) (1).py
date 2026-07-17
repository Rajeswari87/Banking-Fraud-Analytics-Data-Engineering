import dlt

# ==========================================================
# GOLD LAYER : ACCOUNT SCD TYPE 2
# ==========================================================

# Create Gold Streaming Table
dlt.create_streaming_table(

    name = "dim_account_gold_scd2",

    comment = "Historical tracking of account data changes using SCD Type 2"

)

# Apply CDC Changes from Silver Layer
dlt.apply_changes(

    # Target Gold table
    target = "dim_account_gold_scd2",

    # Source Silver table
    source = "banking_silver.dim_account_silver",

    # Primary Key
    keys = ["ACCOUNT_ID"],

    # Latest update wins
    sequence_by = "updated_at",

    # Soft delete inactive accounts
    apply_as_deletes = "STATUS = 'INACTIVE'",

    # SCD Type 2
    stored_as_scd_type = 2,

    # Track history when these columns change
    track_history_column_list = [

        "TYPE",
        "BALANCE",
        "STATUS"

    ]

)