# producers/match_event_producer.py
from kafka import KafkaProducer
from datetime import datetime, timezone
import random

def generate_match_event(minute):
    """Retourne un dict representant un evenement de match aleatoire."""
    return {
        "player_id": f"P{random.randint(1, 4)}",
        "roll_value": random.randint(1, 6),
        "roll_type": random.choice(ROLL_TYPES),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    event = generate_match_event()
    print(event)

def run_match_producer():
    """Construit le KafkaProducer et boucle pour envoyer des evenements."""
    # <- a coder au mini-bloc 1.2