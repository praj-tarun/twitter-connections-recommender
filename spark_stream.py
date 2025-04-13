from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("TwitterStreamProcessor") \
    .master("local[*]") \
    .getOrCreate()

# Read data from Kafka topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "twitter_data") \
    .load()

# Convert binary 'value' column to String
tweets_df = df.selectExpr("CAST(value AS STRING) as tweet_json")

# Write stream to console (for testing)
query = tweets_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
