# Tweety API

> Built with Python and Django.

## Getting started

1. Create a `.env` file in the root directory `python_django` and fill the needed environment variables, check [.env.example](./.env.example) for reference.
2. Run `docker compose up` which will spin up 3 docker containers:
  
     1. Django application [http://0.0.0.0:8000](http://0.0.0.0:8000)
     2. PostgreSQL database (Available only through docker network (tweety))
     3. PGAdmin application [http://0.0.0.0:5050](http://0.0.0.0:5050)
