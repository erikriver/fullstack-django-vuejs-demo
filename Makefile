.PHONY: backend requirements test-backend frontend test-frontend clean run all

###### Backend stuff

VENV=./venv/bin
REQUIREMENTS=$(VENV)/pip install -r backend/requirements.txt

backend:
	python3 -m venv venv
	$(VENV)/python -m pip install --upgrade pip setuptools
	$(REQUIREMENTS)
	$(VENV)/python backend/manage.py migrate
	$(VENV)/python backend/manage.py loaddata backend/project/fixtures/users.json

requirements:
	$(REQUIREMENTS)

test-backend:
	$(VENV)/flake8 backend/app.py
	$(VENV)/black backend/app.py
	$(VENV)/pytest backend/tests.py

###### Frontend stuff

frontend:
	cd ./frontend/ && \
	yarn && \
	yarn build && \
	mv ./build ../backend/client

test-frontend:
	cd ./frontend/ && \
	yarn && \
	yarn test

run:
	. $(VENV)/activate && \
	cd ./backend/ && \
	python manage.py runserver

clean:
	rm -rf venv && \
	rm backend/db.sqlite3

all: backend frontend run