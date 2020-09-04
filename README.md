# SmartSteel

SmartSteel is a Django web application that list down the temperatures information.

#### Task Description
1. Create an application that transfers `task_data.csv` to a database
2. Create a _separate_ web application that is able to connect to this database
3. Serve the database data (from `task_data.csv`) in a _simple_ html format
4. On each GET request, log that the data was requested (in the same database)

## Installation

First clone the project into a directory.
```bash
   git clone git@github.com:asadiqbal08/SmartSteel.git
```
Create a virtual environment and activate it. Further [reading](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html) to virtual environment for mac.
```bash
   virtualenv venv
   source venv/bin/activate
```
Go into the project directory and install the requirements.
```bash 
   cd smartsteel/
   make requirements
```
Run migrations.
```bash
   make migrate
```
Run the `seed_data` management command that will transfers `task_data.csv` to database.
```bash 
   make seed_data
```
Lastly, Run the server command. visit `http://127.0.0.1:8000/`
```bash 
   make server
```
(OPTIONAL) For admin access. visit `http://127.0.0.1:8000/admin/`
```bash
   make superuser 
```

## External Libraries
- [Pandas](https://pypi.org/project/pandas/) python lib is used to load CSV data into data-frames that are easy and well organized to use.
- Customize the [django-db-logger](https://github.com/CiCiUi/django-db-logger) library for putting data in JSON format into model. 
- [bulk_update_or_create](https://pypi.org/project/django-bulk-update-or-create/)
  * For a batch of records:
     * SELECT all from database (based on the match_field parameter)
     * Update records in memory
     * Use bulk_update for those
     * Use INSERT/.create on each of the remaining
