# Created the project by
- uv init .
- uv add django
- uv run django-admin startproject fin_django .


# Adding tailwindcss
https://django-tailwind.readthedocs.io/en/latest/installation.html

- uv add install 'django-tailwind[reload]'
- add 'tailwind' to INSTALLLED_APPS
- uv run manage.py tailwind init
- add theme & django_browser_reload to INSTALLED_APPS
- TAILWIND_APP_NAME = 'theme'
- uv run manage.py tailwind install
- add django middleware to MIDDLEWARE
- uv run manage.py tailwind start