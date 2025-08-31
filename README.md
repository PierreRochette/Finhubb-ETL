# Initialize Database

- In your Postgres, create database `finnhub_datas`. 
- Create a `.env` file and fill it with the expected informations (cf. `.env.example`)

- Initialise a python virtual env : `python -m venv venv`
- Run `source venv/bin/activate`
- Run `pip install -r requirements.txt`
- Run `python init.py` : if nothing outputed, check if the table has been created. It is supposed to have worked. 