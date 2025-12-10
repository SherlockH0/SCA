.PHONY: install 
install:
	uv install

.PHONY: migrate
migrate: 
	uv run src/manage.py migrate

.PHONY: migrations 
migrations: 
	uv run src/manage.py makemigrations
	
.PHONY: runserver
runserver:
	uv run src/manage.py runserver

.PHONY: superuser
superuser:
	uv run src/manage.py createsuperuser

.PHONY: shell
shell:
	uv run src/manage.py shell

.PHONY: update
update: install migrate ;
