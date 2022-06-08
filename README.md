# big-data-processing-hw6
Six Homework for the UCU Big Data Processing course.

Results are stored in results.pdf and also in Screenshots folder 

## Usage:
```
bash run-cluster.sh
bash create-topic.sh
bash build-run.sh
bash shutdown-cluster.sh
```
## NOTE: 
if you want to check the topic messages via consumer execute:
```
docker run -it --rm --network kafka-network -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest kafka-console-consumer.sh --bootstrap-server kafka-server:9092 --topic tweets
```
In the separate termianl before running build-run and after creating a topic.
