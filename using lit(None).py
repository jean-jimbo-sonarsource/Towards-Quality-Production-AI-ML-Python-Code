from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

spark = SparkSession.builder.appName("Example").getOrCreate()

data = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie")
]

df = spark.createDataFrame(data, ["id", "name"])

df_with_empty_column = df.withColumn("middle_name", lit('')) # Noncompliant: usage of lit('') to represen