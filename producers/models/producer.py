"""Producer base-class providing common utilites and functionality"""
import logging
import time


from confluent_kafka import avro
from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroProducer

logger = logging.getLogger(__name__)

broker_url = "PLAINTEXT://localhost:9092"
schema_registry_url = "http://localhost:8081"

class Producer:
    """Defines and provides common functionality amongst Producers"""

    # Tracks existing topics across all Producer instances
    existing_topics = set([])

    def __init__(
        self,
        topic_name,
        key_schema,
        value_schema=None,
        num_partitions=1,
        num_replicas=1,
    ):
        """Initializes a Producer object with basic settings"""
        self.topic_name = topic_name
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.num_partitions = num_partitions
        self.num_replicas = num_replicas

        
        # broker config
        self.broker_properties = {
            "bootstrap.servers":broker_url,
            "schema.registry.url":schema_registry_url,
            "acks":"all",
            "min.insync.replicas":2,
            "message.send.max.retries":5,
            "enable.idempotence": True,
        }

        # If the topic does not already exist, try to create it
        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        # Configure the AvroProducer
        self.producer = AvroProducer({
                                     
            "bootstrap.servers":broker_url,
            "schema.registry.url":schema_registry_url},
            default_key_schema= self.key_schema, 
            default_value_schema= self.value_schema
         )
        

    def create_topic(self):
        """Creates the producer topic if it does not already exist"""
        
        client = AdminClient({"bootstrap.servers": broker_url})
        futures = client.create_topics(
            
        [
             NewTopic(
                 topic = self.topic_name,
                 num_partitions = self.num_partitions,
                 replication_factor = self.num_replicas,
                 config = {
                    "cleanup.policy": "compact",
                    "compression.type": "lz4",
                    "delete.retention.ms": 100,
                    "file.delete.delay.ms": 100
                 })])
            
        logger.info("topic creation kafka integration incomplete - skipping")
        

    def time_millis(self):
        return int(round(time.time() * 1000))

    def close(self):
        """Prepares the producer for exit by cleaning up the producer"""

        self.producer.flush()
        
        logger.info("producer close incomplete - skipping")

    def time_millis(self):
        """Use this function to get the key for Kafka Events"""
        return int(round(time.time() * 1000))
