PYTHON = python
PIP = pip3
FLASK_APP = ai-atc:latest

init:
	$(PIP) install --upgrade -r requirements.txt

lint:
	autopep8 --in-place --recursive application/*
	$(PYTHON) -m pylint application/*

build:
	docker build -t $(FLASK_APP) .

test:
	python -m pytest --no-header -v -o log_cli=true

run:
	flask --debug run --host=0.0.0.0 --port=5001