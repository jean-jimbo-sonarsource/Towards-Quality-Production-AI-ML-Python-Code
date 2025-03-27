# Joining DataFrames without specifying the 'how' parameter
df1 = spark.createDataFrame([(1, 'Alice'), (2, 'Bob')], ["id", "name"])
df2 = spark.createDataFrame([(1, 'HR'), (2, 'Finance')], ["id", "department"])

# Non-compliant: 'how' parameter is not specified
joined_df = df1.join(df2, on="id")

