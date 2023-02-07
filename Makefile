install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
		black *.py

test:
	python -m pytest -vv --cov=app test_app.py

all: install format test