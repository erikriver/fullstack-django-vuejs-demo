.PHONY: setup setup-data run down test

###### Backend stuff

setup:
	docker-compose build
	docker-compose up -d

setup-data:
	@echo "If it shows an error, you must wait for 'make setup' to finish"
	docker-compose exec backend python manage.py loaddata project/fixtures/users.json
	docker-compose exec backend python manage.py get_places
	docker-compose stop

run:
	docker-compose stop
	docker-compose up -d

down:
	docker-compose down;

test:
	docker-compose exec backend python manage.py test -v 2