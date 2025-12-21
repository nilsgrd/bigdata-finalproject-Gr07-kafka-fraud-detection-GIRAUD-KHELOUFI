# Real-Time Banking Transaction Fraud Detection with Kafka

## Project Overview
This project is a technical Big Data project developed as part of the **Big Data Introduction** course.
The objective is to design and run a minimal **real-time fraud detection pipeline** using **Apache Kafka**.

The system simulates banking transactions that are streamed in real time. A Kafka consumer processes these events and applies simple fraud detection rules to identify suspicious transactions.

**Project type:** Technical Project (Option A)  
**Team:** Adam Kheloufi & Nils Giraud  
**Group:** GR07

## Chosen Tool: Apache Kafka

### Why we selected Kafka
We selected **Apache Kafka** because it is a core Big Data tool for **real-time event streaming**. Kafka is widely used to ingest and distribute continuous data flows with high throughput and low latency, which makes it suitable for use cases such as:
- banking transaction monitoring
- fraud detection and alerting
- log collection and real-time analytics
- streaming ETL pipelines

In our project, Kafka acts as the central **streaming backbone** between the transaction producer and the fraud detection consumer.

## Installation & Setup

### Prerequisites
- Docker Desktop (Windows)
- WSL2 (Ubuntu) (for running Linux commands on Windows)
- Git
  
### Run Kafka locally (Docker Compose)

```bash
git clone https://github.com/nilsgrd/bigdata-finalproject-Gr07-kafka-fraud-detection-GIRAUD-KHELOUFI.git
cd bigdata-finalproject-Gr07-kafka-fraud-detection-GIRAUD-KHELOUFI

docker compose up -d

docker compose ps
```

## Minimal Working Example (Kafka CLI)

```bash
# 1) Create (or list) the topic
docker exec -it real-time-fraud-kafka-kafka-1 bash -lc "kafka-topics --bootstrap-server localhost:9092 --list"
docker exec -it real-time-fraud-kafka-kafka-1 bash -lc "kafka-topics --bootstrap-server localhost:9092 --create --topic bank-transactions --partitions 1 --replication-factor 1"

# 2) Produce 3 sample events (CREATED / UPDATED / DELETED)
docker exec -i real-time-fraud-kafka-kafka-1 bash -lc "echo '{\"id\":10,\"user\":\"A\",\"amount\":120,\"event\":\"CREATED\"}' | kafka-console-producer --bootstrap-server localhost:9092 --topic bank-transactions"
docker exec -i real-time-fraud-kafka-kafka-1 bash -lc "echo '{\"id\":10,\"user\":\"A\",\"amount\":500,\"event\":\"UPDATED\"}' | kafka-console-producer --bootstrap-server localhost:9092 --topic bank-transactions"
docker exec -i real-time-fraud-kafka-kafka-1 bash -lc "echo '{\"id\":10,\"event\":\"DELETED\"}' | kafka-console-producer --bootstrap-server localhost:9092 --topic bank-transactions"

# 3) Consume from the beginning (run in another terminal)
docker exec -it real-time-fraud-kafka-kafka-1 bash -lc "kafka-console-consumer --bootstrap-server localhost:9092 --topic bank-transactions --from-beginning"


## Proof of Execution (Screenshots)

### Environment ready (WSL2 + Ubuntu)
![WSL Ubuntu installed](A2_wsl_ubuntu_installed.png)

### Docker installed and running
![Docker Desktop running](01_docker_desktop_open.png)

### Kafka started with Docker Compose
![Docker Compose up](docker_compose_up_ok_terminal.png)

### Kafka & Zookeeper running
![Kafka running (docker compose ps)](kafka_running_terminal.png)

### Kafka CLI producer / consumer working
![Execution proof](execution_proof.png)

### Sample input and output (project files)
**Sample input (transactions):**
![Sample transactions](sample_transactions.png)

**Sample output (fraud alerts):**
![Sample fraud alerts](sample_fraud_alerts.png)


