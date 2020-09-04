superuser: ## create super user to access django admin panel e.g. localhost:8000/admin
	./manage.py createsuperuser

requirements: ## install development environment requirements
	pip install -r requirements.in --exists-action w

migrate: ## run local development server
	./manage.py migrate

server: ## run local development server
	./manage.py runserver

seed_data: ## execute the seed_data management command with given .csv file.
	./manage.py seed_data --csvfile "task_data.csv"
