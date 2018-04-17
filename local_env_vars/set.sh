export DEBUG=true
export SECRET_KEY="super_secret_key"
export DATABASE_URL="postgres://DB_USER:DB_PASSWORD@localhost/DB_NAME"

export DJANGO_SETTINGS_MODULE=shortener.settings.local

export ADMIN_URL_PATH=admin
echo 'Environment variables are set up'
