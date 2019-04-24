PIP=venv/bin/pip

venv:
	python3.7 -m venv venv

deps:
	$(PIP) install -r requirements.txt

fresh-deps:
	$(PIP) install -r requirements/requirements.txt

freeze:
	$(PIP) freeze > requirements.txt
