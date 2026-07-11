import json
import random
import time
from datetime import datetime, timezone
from kafka import KafkaProducer

from producers.config import (
    PRODUCER_CONFIG,
    TOPIC_FAN_TWEETS,
    PSEUDO,
    MESSAGE,
    TWEET_INTERVAL_RANGE,
    SIMULATION_DURATION_SECONDS,   
)

def generate_fan_tweet():
    """Retourne un dictionnaire représentant un tweet aléatoire d'un utilisateur"""
    user = random.choice(PSEUDO)
    message = random.choice(MESSAGE)

    tweet = {
        "user_name": user,
        "message": message,
        "timestamp": datetime.now(timezone.utc).isoformat(),

    }
    return tweet

def run_tweet_producer():
    """Construit un KafkaProducer et envoie un tweet toutes les quelques secondes"""
    producer = KafkaProducer(
        **PRODUCER_CONFIG,
        value_serializer = lambda v: json.dumps(v).encode("utf-8"),
        key_serializer = lambda k: k.encode("utf-8"),

    )

    start = time.monotonic()
    
    try:
        while time.monotonic() - start < SIMULATION_DURATION_SECONDS:
            tweet = generate_fan_tweet()
            producer.send(TOPIC_FAN_TWEETS, key=tweet["user_name"], value=tweet)
            print(f"{tweet['user_name']} - {tweet['message']}")
            time.sleep(random.uniform(*TWEET_INTERVAL_RANGE))
    finally:
        producer.flush()
        producer.close()


if __name__ == '__main__':
    run_tweet_producer()