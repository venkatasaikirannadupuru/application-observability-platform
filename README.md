# Application Observability Platform

A containerized FastAPI application monitored using Prometheus and Grafana. This project demonstrates API health checks, request metrics, latency monitoring, and alerting for HTTP 5xx errors.

## Architecture

FastAPI Application → Prometheus → Grafana

- **FastAPI:** Provides the Shopping API.
- **Docker:** Packages the application into a container.
- **Docker Compose:** Runs the API, Prometheus, and Grafana together.
- **Prometheus:** Scrapes application metrics every 5 seconds.
- **Grafana:** Visualizes request counts, API latency, and server errors.
- **Grafana Alerting:** Evaluates a rule for HTTP 5xx errors.

## Features

- API endpoints: `/`, `/health`, `/products`, and `/error`
- Prometheus metrics exposed at `/metrics`
- Grafana dashboard for product requests, latency, and server errors
- Alert rule for HTTP 5xx errors
- Persistent Grafana storage using a Docker named volume
- SMTP configuration through environment variables; email delivery depends on network access

## Prerequisites

- Docker Desktop
- Docker Compose
- Git

## Project Structure

```text
application-observability-platform/
├── app/
│   └── main.py
├── monitoring/
│   └── prometheus.yml
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md