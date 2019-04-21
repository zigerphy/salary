"""
Django settings for sh_salary project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5*@tnl045(i63vofxpnd@owb7j270!f_zl(9u=2v65hgtu#x5o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'basic',
    'payroll',
    'login',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sh_salary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sh_salary.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'payroll_salary',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        # 'TEST': {
        #     'NAME': 'school_salary_test',
        #     'CHARSET': 'utf8',
        #     'COLLATION': 'utf8_general_ci',
        # },
        # 'OPTIONS': {
        #     'charset': 'utf8mb4',
        #     'init_command': 'SET default_storage_engine=INNODB',
        # },
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# qiniu_config = {
#     'AK': 'tG86zAtcQTDOtwN1aQGBa4-6ULkvKCcV7azRAcHE',
#     'SK': 'EuUIXfgs1SA1TjDHtRrDLhWl8rnPIWB6zP-mTDmH',
#     'BUCKET_NAME': 'tp',
#     'DOMAIN': 'https://tp.qiniu.shuhe.biz/'
# }
QINIU = {
    'access_key': 'SDbdxmtksVbzc6iZHh0YDX6yFbxIMegm_yqP0wqu',
    'secret_key': 'cqhR4eMnt_-M0l2NpiBEE02RB9guJxRl_0H3000G',
    'bucket_name': 'liushuihao',
    'domain': 'http://powqxdxux.bkt.clouddn.com'
}


WORK_WEIXIN_CONFIG = {
    'corpid': 'wwa0cf2e58e87c0d10',
    'corpsecret': 'IwYnhNoC4tWnD6v8oUhNkB1N5AanAsJEieU2FqL9xIE',
    'agentid': '1000046',
    'redirect_uri': 'payroll/confirm_login'
}
BASE_URL = 'www.baidu.com'
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}