# Django Shortener

Basic URL shortener powered by Django Web Framework.

## Live Demo
https://django-shortener.herokuapp.com/

First launch may take a couple of seconds. Further interaction should be quicker.

## Usage
1. Enter URL on the main page and press Enter
1. Copy short URL from the result page
1. ???
1. Profit!

## Deployment on Heroku
There is more than one way to deploy this to Heroku. Feel free to deviate from the instructions if you know how to do it better.

1. Clone this repo to the local machine `git clone https://github.com/deniskasyanov/django-shortener`
1. Install Heroku CLI and log in to your Heroku account in shell ([instructions on Heroku website](https://devcenter.heroku.com/articles/heroku-cli))
1. Attach Heroku PostgreSQL addon using `heroku addons:add heroku-postgresql`. This will automatically set environment variable `DATABASE_URL`
1. Set up remaining environment variables according to the next subsection
1. Push the repo to Heroku: `git push heroku master`
1. Run database migrations with `heroku run python manage.py migrate`

#### Required Environment Variables  
* `ADMIN_URL_PATH`
  * Admin will be available at `https://<YOUR_PROJECT>.herokuapp.com/<ADMIN_URL_PATH>/`
* `DATABASE_URL`
  * Heroku will most likely set it up automatically. Should be set up manually in development environment though. Format is `postgres://<USER>:<PASSWORD>@<HOSTNAME>:<PORT>/<DATABASE_NAME>`. For example, I used something like  `postgres://user:password@localhost/django_shortener` for local development (port is omitted)
* `DEBUG`
  * Should contain `false` in production environment and `true` in development one
* `DJANGO_SETTINGS_MODULE`
  * `shortener.settings.production` for production and `shortener.settings.local` for development
* `SECRET_KEY`
  * It is probably a good idea to have different secret keys for development and production. See [SECRET_KEY section in Django Deployment Checklist](https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/#secret-key)

Environment variables can be set up in web interface (Project Setting -> Config Variables) or using Heroku CLI as follows:
```bash
heroku config:set <ENVIRONMENT_VARIABLE>=<VALUE>
```

There are convenience utility scripts in `local_env_vars/` for setting and unsetting environment variables in local environment. You need to change at least `DATABASE_URL` with your DB config, everything else should work even with default values. Run `. local_env_vars/set.sh` from project root to set up variables and `. local_env_vars/unset.sh` to unset them.

## Areas for improvement

* Static files are served with Python
  * Should not be a big problem since all public-facing pages use only Bootstrap hosted on CDN or inline 9-line JS  for one-click copying. If new features requiring custom static files are added, assets can be moved to S3 or similar service
* JS is inline
  * Well, it's only 9 lines. I don't plan to add new features, so I've decided not to alter settings and create additional nested folder structure just for one simple script.
* Features that can be added to enhance user experience and increase security:
  * Click counting
  * Rate limiting for anonymous users
  * As a result, user registration and authentication
  * API
