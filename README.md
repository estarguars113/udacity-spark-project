# udacity-spark-project

# Initial Setup

## Kafka config

`
/usr/bin/kafka-topics  --create --zookeeper localhost:2181 --topic <topic_name> --partitions <num_partitions> --replication-factor <replication_factor>
`

In my specific case I created the topic with a replication factor of 1 and 3 partitions

To check if the topic was correctly created

`
/usr/bin/kafka-topics  --list --zookeeper localhost:2181
`

Describe topic created

`
/usr/bin/kafka-topics --describe --zookeeper localhost:2181 --topic <topic_name>
`

In case of error in the creation of the topic
`
/usr/bin/kafka-topics  --zookeeper localhost:2181 --delete --topic <topic_name>
`

## Interact with the topic

First data production, kafka producer

`
python kafka_server.py
`

Once the data is loaded, you can consume it from the topic

`
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] --conf spark.ui.port=3000 data_stream.py
`

## Pyspark setup

Considerations:

* The input file is 108M in size, so it's not that big, however, we're applying a grouping and aggregation operation

**How did changing values on the SparkSession property parameters affect the throughput and latency of the data?**

First based on the number of partitions I started changing the number of executors and the amount of memory available for each one of those, so finally, I came up with

`
    .config("spark.executor.memory", "3g") \
    .config("spark.executor.cores", 2) \
    .config("spark.cores.max", 6) \
`

Resulting in 3 executors each one with 3 gigabites of memory for processing

**What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?**

In my case was changing the parallelism and the partitions shuffle

`
.config("spark.sql.shuffle.partitions", 3) \
.config("spark.default.parallelism", 200) \
`

I started with around 10 rows processed by second and by changing these two values I triple this value(screenshots attached)