# Simulates sending banking transactions to Kafka

import json
import time

print("Kafka Producer started (simulation)")

transactions = [
    {"id": 1, "user": "A", "amount": 120},
    {"id": 2, "user": "B", "amount": 4200},
    {"id": 3, "user": "C", "amount": 75},
]

for tx in transactions:
    print("Sending transaction:", tx)
    time.sleep(1)
