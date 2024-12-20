import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTALLED_APPS = [
    'rest_framework',
    'corsheaders',
    'api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Add this
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'sahil',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

CORS_ALLOW_ALL_ORIGINS = True  # For testing only, restrict in production
# Add Razorpay Keys
RAZORPAY_API_KEY = "rzp_test_xVdiKSkwDJsHoU"
RAZORPAY_API_SECRET = "meg0URAK25C4SX8efWZCnWGR"

DEBUG = True  # Set to False in production
ROOT_URLCONF = 'backend.urls'
ALLOWED_HOSTS = ['localhost', '127.0.0.1'] 
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

SECRET_KEY = 'django-insecure-your-secret-key-here'  # Replace with a secure key in production

# Optional but recommended for development:
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
] 

