import os

# base dir project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# drivers path
DRIVERS_DIR = os.path.join(BASE_DIR, 'drivers')
CHROME_DRIVER_PATH = os.path.join(DRIVERS_DIR, 'chromedriver')
FIREFOX_DRIVER_PATH = os.path.join(DRIVERS_DIR, 'geckodriver')

# data dir
DATA_DIR = os.path.join(BASE_DIR, 'data')
DATA_FILE = os.path.join(DATA_DIR, '{file_name}')

# files dir
TEST_FILES_DIR = os.path.join(BASE_DIR, 'test_files')
FILE_PATH = os.path.join(TEST_FILES_DIR, '{file_name}')

# environ
ENV = os.environ['ENV']

# urls
BASE_URL = {
    'prod': '***',
    'stage': '***',
    'dev23': '***',
    'dev24': '***'
}

# users
USERS_PROD = {}
USERS_STAGE = {}
USERS_DEV23 = {}
USERS_DEV24 = {
    'owner': {
        'login': '***',
        'password': '***',
        'user_name': '***'
    },
    'provider1': {
        'login': '***',
        'password': '***',
        'user_name': '***'
    },
    'provider2': {
        'login': '***',
        'password': '***',
        'user_name': '***'
    }
}

try:
    from local_settings import *
except ImportError:
    pass


