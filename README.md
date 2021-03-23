# CV-website
Simple Flask server and website for a resume with a contact form

This is a simple Flask webapp with a minimal backend to serve a website with a form and relay the form's responses to Telegram.
Configuration files are prepared for deploying on Heroku, though the app can (probably) be configured for any WSGI deployment.

An instance can be found running at https://ttpk.fi/cv/

### Running the app
The app depends on Flask and python-telegram-bot, while the deployment depends on Gunicorn. The app can be debugged by running 
`python3 wsgi.py` (for no debug flag enabled) and `python app/main.py` (for the Flask debug flag enabled). 

The app must be configured either via the `config.ini` file placed in the `app/` directory or via setting the RECIP_TOKEN and SENDER_TOKEN environment variables on the system. A simple config is as follows:
```ini
[secrets]
recipient_id = ; recipient chatid goes here
sender_token = ; bot token goes here
```
The INI method is preferrable when deploying on a server with multiple services running, but the environment variable route is preferred when deploying through github.

Deploying to Heroku can be done by cloning the repository and pushing it to a Dyno instance. You can also fork the repository, and set a Heroku Dyno or other instance to fetch it from Github when changes are made.

### License

The backend and frontend are completely free and open to anyone, but I retain the right for the page content myself.
