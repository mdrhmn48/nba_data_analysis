from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Test") \
    .getOrCreate()

print(spark.version)
