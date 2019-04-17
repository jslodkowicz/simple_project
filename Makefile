.PHONY: test

deps:
	pip install -r requirements.txt
	pip install -r test_requirements.txt

run:
	PYTHONPATH=. FLASK_APP=weather flask run

test:
	python3 -m pytest test/test_fun.py
