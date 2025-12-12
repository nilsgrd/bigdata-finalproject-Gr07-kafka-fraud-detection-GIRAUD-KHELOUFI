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

