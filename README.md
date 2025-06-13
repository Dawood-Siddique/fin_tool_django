# Created the project by
- uv init .
- uv add django
- uv run django-admin startproject fin_django .


# Adding tailwindcss
https://django-tailwind.readthedocs.io/en/latest/installation.html

- uv add 'django-tailwind[reload]'
- add 'tailwind' to INSTALLLED_APPS
- uv run manage.py tailwind init or COMMENT 'theme' if already added to setting.py
- add theme & django_browser_reload to INSTALLED_APPS OR uncomment 'theme'
- TAILWIND_APP_NAME = 'theme'
- uv run manage.py tailwind install
- add django middleware to MIDDLEWARE
- uv run manage.py tailwind start

# Adding migrations
- uv run manage.py makemigrations
- uv run manage.py migrate

# Add data to EU model
- uv run data data_inserter.py
