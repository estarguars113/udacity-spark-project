# udacity-spark-project

# Initial Setup

## Kafka config

`
/usr/bin/kafka-topics  --create --zookeeper localhost:2181 --topic <topic_name> --partitions <num_partitions> --replication-factor <replication_factor>
`

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
/usr/bin/kafka-console-producer --broker-list localhost:9092 --topic <topic_name>
`

Once the data is loaded, you can consume it from the topic

`
/usr/bin/kafka-console-producer --broker-list localhost:9092 --topic police-service-calls
`