"""
Configuration partagée pour les producteurs Kafka du projet
World Cup 2026 Live Analytics & Fan Engagement Platform.
"""
import os
from dotenv import load_dotenv


load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
CONFLUENT_API_KEY = os.getenv("CONFLUENT_API_KEY")
CONFLUENT_API_SECRET = os.getenv("CONFLUENT_API_SECRET")

PRODUCER_CONFIG = {"bootstrap_servers": KAFKA_BOOTSTRAP_SERVERS}

if CONFLUENT_API_KEY and CONFLUENT_API_SECRET:
    PRODUCER_CONFIG.update({
        "security_protocol": "SASL_SSL",
        "sasl_mechanism": "PLAIN",
        "sasl_plain_username": CONFLUENT_API_KEY,
        "sasl_plain_password": CONFLUENT_API_SECRET,
    })

SIMULATION_DURATION_SECONDS = 60

# Constantes du producer match event
TOPIC_MATCH_EVENTS = "match-events"

MATCH_ID = "WC2026-FRA-BRA-001"
HOME_TEAM = "France"
AWAY_TEAM = "Brésil"

TEAMS = {HOME_TEAM: [
    {"player_id": "FRA01", "player_name": "K. Mbappe"},
    {"player_id": "FRA02", "player_name": "S. Umtiti"},
    {"player_id": "FRA03", "player_name": "N. Kanté"},
    {"player_id": "FRA04", "player_name": "B. Matuidi"},
    {"player_id": "FRA05", "player_name": "O. Dembélé"}
],
         
          AWAY_TEAM: [
    {"player_id": "BRA09", "player_name": "K. Oliveira"},
    {"player_id": "BRA10", "player_name": "R. Santos"},
    {"player_id": "BRA07", "player_name": "G. Almeida"},
    {"player_id": "BRA11", "player_name": "V. Costa"},
    {"player_id": "BRA08", "player_name": "V. Junior"},        
    
          ] }

EVENT_TYPES = ["pass", "shot", "foul", "yellow_card", "goal", "red_card"]
EVENT_WEIGHTS = [55, 18, 14, 7, 4, 2] # passes fréquentes, buts rares

EVENT_INTERVAL_RANGE = (2.0, 6.0) # secondes entre deux événements envoyés
MATCH_DURATION_MINUTES = 90


# Constantes du producer fan_tweet
TOPIC_FAN_TWEETS = "fan-tweets"

PSEUDO = ["@fandefoot", "@estrella", "@farii", "@vieillebranche", "@coooolll", "@13mai", "@lubiel", "@arikemie", "@luciole", "@verdugo", "@fariqueen", "@dorial", "@primeone"]

MESSAGE = ["Ils ont vendu le match","Oh nonnnnnn", "GOAAALLLLLLL", "Alleeeez les bleus", "Mais ils font quoi purée !", "Mais y'a penalty là", "Penaltyyyyy", "COUP FRANC !", "Il faut centrer là", "FAIS LA PASSE !", "Ils jouent pas collectif là", "Arbitre PENALTY !", "AAAAAHHHH", "BUUUUUUT", "Pitié pas ça !", "Popolopopopopo", "OUIIIIIIII", "Alller Ousmane !", "Aller MBAPPE !", "Wesh il est hyper rapide", "Mais qu'est-ce qu'ils sont nuls", "PITIEEEEEE", "Et de deux !", "Le gardien il est archi nul wesh", "AAAAAAHHHHHH", "ICI C'EST PARIIIISSS", "Bravo les gars", "Bien joué", "C'est injuste, y'a pas pénalty", "FAUUUTE, arbitre y'a faute", "FAUUUTEEEE mais y'a FAUTE là"]

TWEET_INTERVAL_RANGE = (0.5, 2.5)