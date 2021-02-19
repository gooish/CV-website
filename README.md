# CV-website
Simple Flask server and website for a resume with a contact form

This is a simple Flask webapp with a minimal backend to serve a website with a form and relay the form's responses to Telegram.
Configuration files are prepared for deploying on Heroku, though the app can (probably) be configured for any WSGI deployment.

## Running the app
The app depends on Flask and python-telegram-bot, while the deployment depends on Gunicorn. The app can be debugged by running 
`python3 wsgi.py` (for no debug flag enabled) and `python app/main.py` (for the Flask debug flag enabled). 

The app must be configured via the `config.ini` file placed in the `app/` directory. A simple config is as follows:
```ini
[secrets]
recipient_id = ; recipient chatid goes here
sender_token = ; bot token goes here
```

Deploying to Heroku can be done by cloning the repository and pushing it to a Dyno instance
