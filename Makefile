.PHONY: setup setup-data down

###### Backend stuff

setup:
	docker-compose build
	docker-compose up -d

setup-data:
	docker-compose exec backend python manage.py loaddata project/fixtures/users.json
	docker-compose exec backend python manage.py get_places

down:
	docker-compose down;

test:
	docker-compose exec backend python manage.py test -v 2