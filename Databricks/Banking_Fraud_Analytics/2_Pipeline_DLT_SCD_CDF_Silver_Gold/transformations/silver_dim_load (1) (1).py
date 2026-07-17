import dlt
from pyspark.sql.functions import col, upper, trim, when, current_timestamp

@dlt.table(
    name="dim_account_silver",
    comment="Cleaned and standardized account data"
)
@dlt.expect_or_drop(
    "valid_account_id",
    "ACCOUNT_ID IS NOT NULL"
)
def load_account_silver():

    return (
        spark.readStream.table("banking_bronze.bronze_dim_account")

        .withWatermark("updated_at", "1 day")

        .dropDuplicates(["ACCOUNT_ID", "updated_at"])

        .withColumn("TYPE", upper(trim(col("TYPE"))))
        .withColumn("STATUS", upper(trim(col("STATUS"))))
        .withColumn(
            "BALANCE",
            when(col("BALANCE").isNull(), 0).otherwise(col("BALANCE"))
        )
        .withColumn("silver_load_time", current_timestamp())
    )