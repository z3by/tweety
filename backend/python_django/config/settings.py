from pathlib import Path

from environ import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()

ENV_FILE = env.str("DJANGO_ENV_FILE", default=".env.dev")

Env.read_env(str(BASE_DIR / ENV_FILE))

DEBUG = env.bool("DJANGO_DEBUG", default=False)

SECRET_KEY = env.str(
    "DJANGO_SECRET_KEY",
    default="insecure-q8u869lwn66$b%#_$^@b-jcm$%#f*hn0js8d*k3-lcs!$-7!ys",
)


ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third party apps
    "oauth2_provider",
    "rest_framework",
    "django_extensions",
    "debug_toolbar",
    "nplusone.ext.django",
    # Local apps
    "apps.api",
    "apps.users",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "nplusone.ext.django.NPlusOneMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {"default": env.db("DJANGO_DB_URL", default="sqlite:///db.sqlite3")}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"


MEDIA_ROOT = BASE_DIR / "uploads"
MEDIA_URL = "/uploads/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

INTERNAL_IPS = env.list("DJANGO_INTERNAL_IPS", default=["127.0.0.1"])

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


OAUTH2_SCOPES = {
    "openid": "OpenID Connect scope",
    "users": "Gives full read-write access to users",
    "users:read": "Gives read access to users",
    "users:write": "Gives write access to users.",
}

# WARNING: this RSA key is only for development, create your own key for production.
OIDC_RSA_PRIVATE_KEY_PATH = env.str("OIDC_RSA_PRIVATE_KEY_PATH", default=BASE_DIR / "oidc-dev.key")
with open(OIDC_RSA_PRIVATE_KEY_PATH) as oidc_key_file:
    OIDC_RSA_PRIVATE_KEY = oidc_key_file.read()

OAUTH2_PROVIDER = {
    "SCOPES": OAUTH2_SCOPES,
    "READ_SCOPE": "read",
    "WRITE_SCOPE": "write",
    "PKCE_REQUIRED": True,
    "OIDC_ENABLED": True,
    "OIDC_RSA_PRIVATE_KEY": OIDC_RSA_PRIVATE_KEY,
}

LOGIN_URL = "/api-auth/login/"
