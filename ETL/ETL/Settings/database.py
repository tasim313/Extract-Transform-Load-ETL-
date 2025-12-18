import os
from .auth import BASE_DIR
import environ

env = environ.Env(
    ENVIRONMENT=(str, "development")
)

# Read .env
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

ENVIRONMENT = env("ENVIRONMENT").lower()

if ENVIRONMENT == "development":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, f"{env('DEV_DB_NAME', default='test')}.sqlite3"),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env("PROD_DB_NAME"),
            'USER': env("PROD_DB_USER"),
            'PASSWORD': env("PROD_DB_PASSWORD"),
            'HOST': env("PROD_DB_HOST"),
            'PORT': env.int("PROD_DB_PORT", 5432),
        }
    }

print(f"ENVIRONMENT={ENVIRONMENT}, DATABASE={DATABASES['default']['NAME']}")