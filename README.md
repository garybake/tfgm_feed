# Real time TFGM feed

Setup kafka
-----------
Set initial config files

**Windows**  
`bin\windows\zookeeper-server-start.bat config\zookeeper.properties`  
`bin\windows\kafka-server-start.bat config\server.properties`  

**Linux**  
`bin/zookeeper-server-start.sh config/zookeeper.properties`  
`bin/kafka-server-start.sh config/server.properties`  

**Create topic**  
`bin/kafka-topics.sh --create --topic metrolink --bootstrap-server localhost:9092`
`bin/kafka-topics.sh --list --zookeeper localhost:2181`

**Listen for messages**  
`bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic metrolink --from-beginning`

Setup Spark (local cluster)
-------------------
**Start the master**  
`./sbin/start-master.sh`

**Add a worker**  
`./sbin/start-slave.sh $(hostname):7077`

**Windows**
`bin\spark-class org.apache.spark.deploy.master.Master`  
`bin\spark-class org.apache.spark.deploy.worker.Worker spark://hostname:port`

**View the webui**  
http://localhost:8080/ 

**PySpark shell**  
`./bin/pyspark --master spark://$(hostname):7077`
