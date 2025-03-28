from pyspark.sql.functions import *
df = df.withColumn('Revenue', col('fare_amount').substr(0, 10).cast("float") + col('extra').substr(0, 5).cast("float") + col('tax').substr(0, 3).cast("float")) # Noncompliant
df = df.withColumn('High revenue', when(col('fare_amount').substr(0, 10).cast("float") > 100. and col('extra').substr(0, 5).cast("float") > 100. and col('tax').substr(0, 3).cast("float") < 50.)) # Noncompliant
df = df.filter(col('fare_amount').substr(0, 10).cast("float") > 100. and col('extra').substr(0, 5).cast("float") > 100. and col('tax').substr(0, 3).cast("float") < 50.) # Noncompliant

# Compliant Solution
df = df.withColumn('Revenue', col('fare_amount').substr(0, 10).cast("float") + col('extra').substr(0, 5).cast("float") + col('tax').substr(0, 3).cast("float"))
df = df.withColumn('High revenue', when(col('fare_amount').substr(0, 10).cast("float") > 100. and col('extra').substr(0, 5).cast("float") > 100. and col('tax').substr(0, 3).cast("float") < 50., True))        
    