# Simulates fraud detection logic

print("Kafka Consumer started (simulation)")

def is_fraud(transaction):
    return transaction["amount"] > 3000

print("Fraud rule: amount > 3000")
