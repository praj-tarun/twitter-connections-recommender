import json
import time
import random
from kafka import KafkaProducer
from faker import Faker

# Initialize Faker for generating synthetic data
fake = Faker()

def generate_synthetic_tweet():
    """
    Generate a synthetic tweet JSON structure.
    """
    tweet = {
        "tweet_id": str(fake.random_number(digits=19, fix_len=True)),  # 19-digit tweet ID as string
        "timestamp": fake.iso8601(),  # ISO 8601 formatted timestamp
        "text": fake.sentence(nb_words=12) + " " + " ".join("#" + fake.word() for _ in range(random.randint(0, 3))),
        "hashtags": [fake.word() for _ in range(random.randint(0, 3))],
        "mentions": ["@" + fake.user_name() for _ in range(random.randint(0, 2))],
        "language": random.choice(["en", "es", "fr", "de", "it"]),
        "engagement": {
            "retweet_count": random.randint(0, 100),
            "like_count": random.randint(0, 200)
        },
        "user": {
            "user_id": str(fake.random_number(digits=8, fix_len=True)),  # 8-digit user ID as string
            "screen_name": fake.user_name(),
            "description": fake.text(max_nb_chars=50),
            "followers_count": random.randint(50, 10000),
            "following_count": random.randint(20, 500),
            "verified": random.choice([True, False]),
            "account_creation": fake.iso8601()
        }
    }
    return tweet

def main():
    # Configure the Kafka producer
    producer = KafkaProducer(
        bootstrap_servers='127.0.0.1:9092',  # Replace with your Kafka broker address if different
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        #metadata_timeout_ms=120000 
    )

    topic = "twitter_data"

    print("Starting synthetic tweet production...")

    # Produce messages continuously
    try:
        while True:
            tweet_data = generate_synthetic_tweet()
            producer.send(topic, tweet_data)
            print(f"Produced tweet: {tweet_data['tweet_id']} - {tweet_data['text']}")
            time.sleep(1)  # Adjust the sleep time as needed for your ingestion rate
    except KeyboardInterrupt:
        print("Stopping producer...")
    finally:
        producer.flush()
        producer.close()

if __name__ == "__main__":
    main()
