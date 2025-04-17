from faker import Faker

fake = Faker()

def generate_tweet():
    return {
        "tweet_id": str(fake.random_number(digits=10)),
        "user": fake.user_name(),
        "text": fake.sentence(nb_words=8),
    }
