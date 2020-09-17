import json
import time
import os
import sys

from kafka import KafkaProducer

from websource.tfgm import Tfgm

SUBS_KEY = os.getenv("TFGM_SUBS_KEY")
DELAY_SECONDS = 1


def get_latest_departures():
    tfgm = Tfgm(SUBS_KEY)
    departures = tfgm.get_departures()
    return departures


def send_departures_to_queue(producer, topic, departures):
    for departure in departures:
        message = json.dumps(departure).encode('utf-8')
        producer.send(topic, message)
        time.sleep(DELAY_SECONDS)


def do_producer():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    topic = "metrolink"

    departures = get_latest_departures()
    send_departures_to_queue(producer, topic, departures)


if __name__ == '__main__':
    if SUBS_KEY is None:
        print("TFGM_SUBS_KEY env variable not set")
        sys.exit(-1)

    for i in range(10):
        print(f'*** Loop {i}')
        do_producer()
