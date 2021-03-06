build:
	docker-compose build
up:
	docker-compose up
test:
	docker-compose run app sh -c "python manage.py test"
shell:
	docker-compose run app sh -c "python manage.py shell_plus"
psql:
	docker exec -it django-rest-recipes-api_db_1 psql -U postgres
dj_mm:
	docker-compose run app sh -c "python manage.py makemigrations; python manage.py migrate"
