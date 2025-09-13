# fastAPi
FastApi app for practice

Here is our first API practice, in this application we will run server, and handle some query with database

the library will find here, 

1- FastApi library to create API
2- Python 3.x
3- Postgres Sql
4- SQLAlchemy 
5- Pydantic for validation
6- uvicorn[standard] to expose port and access from outside and the standered for install extra plugin like Http tools
7- asynpg for postgrs driver
8- alembic for migration database


### Create enviroment for project
`python3 -m venv env_name`

For active env from source code
`source env_name/bin/activate`


### install dependencies 
`pip install -r requirements.txt`
and for verify 
`pip list`


#### Run migration 
- `pip install alembic` (or put it in the requirement db)
- alembic init alembic
Edit alembic.ini and env.py to point to your DATABASE_URL, and now:

- alembic revision --autogenerate -m "init"
- alembic upgrade head

## to run the application 
`uvicorn main:app --reload`