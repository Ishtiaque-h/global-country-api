# CodeFusion Country API Assignment
Read the specifications [here](https://workdrive.zohopublic.eu/file/j2a2g0216a20eacd84923aa639dae1710f712).

## Requirements
- Python 3.12 or above.
- PostgreSQL 14 or above.

## Getting started
First, Create a database in PostgreSQL.

Clone the repository from [GitHub](https://github.com/HqShiblu/CodeFusion-Country-API-Assignment).
Open the .sample_env file.
Enter the SECRET_KEY value and database credentials and then save it as **.env** file.

Create a virtual environment.
Use **python** in **Windows** and **python3** in **Linux**.
```
python -m venv country_api_venv
```

Move to Scripts (for **Windows**) or bin (for **Linux**) folder of the environment.
Then activate the environment.

Then, move to the location of the project where **manage.py** file is.
Install the required packages with 
```
pip install -r requirements.txt
```
Use **pip** in **Windows** and **pip3** in **Linux**.


Now, run
```
python manage.py migrate
```
to migrate the models to the database.

