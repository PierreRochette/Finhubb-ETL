# Initialize Database

- In your Postgres, create database `finnhub_datas`. 
- Create a `.env` file and fill it with the expected informations (cf. `.env.example`)

- Initialise a python virtual env : `python -m venv venv`
- Run `source venv/bin/activate`
- Run `pip install -r requirements.txt`
- Run `python init.py` : if nothing outputed, check if the table has been created. It is supposed to have worked. 

# Create a service to execute the script

- Please refer to my notion documentation about creating a timer service

- `cat /etc/systemd/system/finnhub.service`
- `cat /etc/systemd/system/finnhub.timer`
- `sudo systemctl daemon-reload`
- `sudo systemctl enable --now finnhub.timer`
- `systemctl status finnhub.timer`
- `sudo systemctl start finnhub.service`

# First days 

I noticed that the same price appears three time for each ticker. Only the fourth one looks different. So i changed the time on my VPS (with `timedatectl`) to make it the same as Paris time. Then I changed the timer script to launch the code each days between Monday and Friday, one time per hour, between 16h and 22h (which corresponds to the paris time from opening and closing of NASDAQ market). 

# Flask Application


