# TODO currently runs from spark console (spark 3.0.1)
# pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.6

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "metrolink") \
  .load()

df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

df.writeStream\
   .format("console")\
   .start()
