# producers/match_event_producer.py
import json
import random
import time
from datetime import datetime, timezone
from kafka import KafkaProducer 

from producers.config import (
    KAFKA_BOOTSTRAP_SERVERS,
    TOPIC_MATCH_EVENTS,
    MATCH_ID,
    HOME_TEAM,
    AWAY_TEAM,
    TEAMS,
    EVENT_TYPES,
    EVENT_INTERVAL_RANGE,
    MATCH_DURATION_MINUTES,
    EVENT_WEIGHTS,
    SIMULATION_DURATION_SECONDS,
)

def generate_match_event(minute):
    """Retourne un dictionnaire représentant un événement de match aléatoire."""
    team = random.choice([HOME_TEAM, AWAY_TEAM])
    player = random.choice(TEAMS[team])
    event_type = random.choices(EVENT_TYPES, weights = EVENT_WEIGHTS, k=1)[0]

    event = {
        "match_id": MATCH_ID,
        "minute": minute,
        "event_type": event_type,
        "team": team,
        "player_id": player["player_id"],
        "player_name": player["player_name"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return event

def run_match_producer():
    """Construit un KafkaProducer et envoie un événement toutes les quelques secondes jusqu'à la fin du match simulé """
    producer = KafkaProducer(
        bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS,
        value_serializer = lambda v: json.dumps(v).encode("utf-8"),
        key_serializer = lambda k: k.encode("utf-8"),
    )
    
    start = time.monotonic()

    while time.monotonic() - start < SIMULATION_DURATION_SECONDS:
        elapsed = time.monotonic() - start
        proportion = elapsed / SIMULATION_DURATION_SECONDS
        minute = int(proportion * MATCH_DURATION_MINUTES)
    
        event = generate_match_event(minute)
        producer.send(TOPIC_MATCH_EVENTS, key = event["match_id"], value=event)
        print(f"[{event['minute']}] {event['event_type']} - {event['team']} - {event['player_name']}")
        time.sleep(random.uniform(*EVENT_INTERVAL_RANGE))

    producer.flush()
    producer.close()

if __name__ == "__main__":
    run_match_producer()

