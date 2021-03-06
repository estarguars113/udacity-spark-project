import producer_server

TOPIC_NAME = 'police-service-calls'

def run_kafka_server():
    input_file = 'police-department-calls-for-service.json'

    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=TOPIC_NAME,
        bootstrap_servers="localhost:9092",
        client_id="consumer-1"
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
