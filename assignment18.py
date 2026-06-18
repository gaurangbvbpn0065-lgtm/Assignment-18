from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("PartitionExample") \
    .getOrCreate()

# Generate a DataFrame with 5 million records
df = spark.range(5000000)

# Display the initial number of partitions
print("Initial number of partitions:", df.rdd.getNumPartitions())

# Increase the number of partitions to 12
df_repartitioned = df.repartition(12)

# Display the number of partitions after repartition
print("Number of partitions after repartition(12):",
      df_repartitioned.rdd.getNumPartitions())

# Reduce the number of partitions to 3
df_coalesced = df_repartitioned.coalesce(3)

# Display the number of partitions after coalesce
print("Number of partitions after coalesce(3):",
      df_coalesced.rdd.getNumPartitions())

# Display a few records
df_coalesced.show(10)

# Stop the Spark Session
spark.stop()