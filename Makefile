# Makefile for swagger petstore api automation

.PHONY: help install test clean

help:
	@echo "Available commands:"
	@echo "  make install             - Install dependencies"
	@echo "  make test                - Run api tests"
	@echo "  make clean               - Clean project"
	@echo "  make report              - ope report.html in browser"

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

