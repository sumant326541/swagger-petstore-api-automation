# Makefile for swagger petstore api automation

.PHONY: help install test clean

help:
	@echo "Available commands:"
	@echo "  make install             - Install dependencies"
	@echo "  make test                - Run api tests"
	@echo "  make clean               - Clean project"
	@echo "  make report              - ope report.html in browser"
	@echo "  make docker-build        - Build docker image"
	@echo "  make docker-up           - Start all services in detached mode"
	@echo "  make docker-test         - Run tests in docker container"
	@echo "  make docker-stop         - Stop all services"
	@echo "  make docker-start        - Start all services"
	@echo "  make docker-clean        - Stop all services and remove containers"
	@echo "  make docker-logs		  - Show logs of all services"


install:
	pip3 install -r requirements.txt

test:
	sh -c 'pytest tests --html=report.html -s'

report:
	@echo "Opening report.html in browser..."
	open report.html || start report.html

clean:
	rm -rf .pytest_cache/
	rm -rf report.html
	rm -rf assets/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Docker solutions
docker-build:
	docker compose build

docker-up:
	docker compose up -d

docker-test:
	docker compose run test_app

docker-stop:
	docker compose stop

docker-start:
	docker compose start

docker-clean:
	docker compose down --remove-orphans

docker-logs:
	docker compose logs

