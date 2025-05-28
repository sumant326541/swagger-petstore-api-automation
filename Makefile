# Makefile for swagger petstore api automation
PYTHON_VERSION = 3.13.3
VENV_DIR = .venv

.PHONY: help all install test clean report \
	docker-build docker-up docker-test docker-stop docker-start docker-clean docker-logs

help:
	@echo "Available commands:"
	@echo "  make help                - Show this help message"
	@echo "  make all                 - Install python dependencies and set up environment"
	@echo "  make install             - Install only dependencies"
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


all:
	brew update
	brew install pyenv || true
	export PYENV_ROOT="$$HOME/.pyenv"; \
	export PATH="$$PYENV_ROOT/bin:$$PATH"; \
	eval "$$(pyenv init --path)"; \
	eval "$$(pyenv init -)"; \
	pyenv install -s $(PYTHON_VERSION); \
	pyenv global $(PYTHON_VERSION); \
	python3 -m venv $(VENV_DIR); \
	. $(VENV_DIR)/bin/activate; \
	pip install -r requirements.txt; \
	python --version

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

