"""
Configuration partagée pour les producteurs Kafka du projet
World Cup 2026 Live Analytics & Fan Engagement Platform.
"""

KAFKA_BOOTSTRAP_SERVERS = "localhost: 9092"

TOPIC_MATCH_EVENTS = "match_events"
TOPIC_FAN_TWEETS = "fan_events"

MATCH_ID = "WC2026-FRA-BRA-001"
HOME_TEAM = "France"
AWAY_TEAM = "Brésil"

TEAMS = {HOME_TEAM: [
    {"player_id": "FRA01", "player_name": "K. Mbappe"},
    {"player_id": "FRA01", "player_name": "V. Junior"},
    {"player_id": "FRA01", "player_name": "N. Kanté"},
    {"player_id": "FRA01", "player_name": "B. Matuidi"},
    {"player_id": "FRA01", "player_name": "O. Dembélé"}
],
         
          AWAY_TEAM: [
    {"player_id": "BRA09", "name": "K. Oliveira"},
    {"player_id": "BRA10", "name": "R. Santos"},
    {"player_id": "BRA07", "name": "G. Almeida"},
    {"player_id": "BRA11", "name": "V. Costa"},
    {"player_id": "BRA08", "name": "D. Pereira"},        
    
          ] }

EVENT_TYPES = ["pass", "shot", "foul", "yellow_card", "goal", "red_card"]
EVENT_WEIGHTS = [55, 18, 14, 7, 4, 2] # passes fréquentes, buts rares

EVENT_INTERVAL_RANGE = (2.0, 6.0) # secondes entre deux événements envoyés
MATCH_DURATION_MINUTES = 90
