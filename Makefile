.PHONY: install test format lint all

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest -vv --cov=lib

format:	
	black ./*.py

lint:
	ruff check ./*.py
		
all: install lint test format
