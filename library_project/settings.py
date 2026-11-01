"""
تنظیمات اصلی پروژه کتابخانه (library_project)
فاز اول: تمرکز روی کاتالوگ و نمایش کتاب‌ها
"""

from pathlib import Path

# مسیر اصلی پروژه
BASE_DIR = Path(__file__).resolve().parent.parent

# کلید امنیتی جنگو
SECRET_KEY = 'django-insecure-m&!*^y@z8i4&r@k-17q_@l5m2^8f9(0x#@7b=4n5v!c'

# در حالت توسعه True است
DEBUG = True

ALLOWED_HOSTS = ['*']

# اپلیکیشن‌های فعال پروژه
INSTALLED_APPS = [
    # برنامه‌های پیش‌فرض جنگو
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # برنامه‌های خودمان
    'catalog',       # اپلیکیشن کاتالوگ (فاز اول)
    'accounts',      # اپلیکیشن اعضا و کاربران (فاز دوم)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'library_project.urls'

# تنظیمات قالب‌ها (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # آدرس پوشه کدهای HTML
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

WSGI_APPLICATION = 'library_project.wsgi.application'

# تنظیمات اتصال به دیتابیس PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'library_db',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# اعتبارسنجی رمز عبور
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

# تنظیمات زبان و زمان
LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True

# تنظیمات فایل‌های استاتیک (CSS و تصاویر)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# مسیر انتقال پس از ورود و خروج کاربر
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'




