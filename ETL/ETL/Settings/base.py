DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]


PROJECT_APP = [
    'core',
]


THIRD_PARTY_APP = [
    'rest_framework',
    'rest_framework.authtoken',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    
    'drf_yasg',
    'imagekit',
    'versatileimagefield',
    
    'crispy_forms',
    'django_extensions',
    'django_filters',
    'import_export',
    'corsheaders',
    'debug_toolbar',
    
    'health_check',  
    'health_check.db',
    'health_check.cache',
    'health_check.storage'
]


INSTALLED_APPS =  PROJECT_APP + DJANGO_APPS + THIRD_PARTY_APP

AUTH_USER_MODEL = 'core.User'

LANGUAGE_CODE = "en-us"

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True