import pytest
from selenium import webdriver

import settings


@pytest.fixture(scope='session')
def driver(request):
    driver = webdriver.Chrome(executable_path=settings.CHROME_DRIVER_PATH)
    driver.implicitly_wait(10)
    driver.maximize_window()

    def close_driver():
        driver.quit()

    request.addfinalizer(close_driver)
    return driver


@pytest.fixture(scope='session')
def app(driver):
    from pages import login_page as LP
    from pages import home_page as HP
    from pages import tender_page as TP
    from pages import lot_form as LF
    from pages import item_form as IF
    from pages import feature_form as FF
    from pages import document_form as DF
    from pages import date_widget as DW

    class App:
        login_page = LP.LoginPage(driver)
        home_page = HP.HomePage(driver)
        select_procedure_modal = HP.SelectProcedureModal(driver)
        tender_page = TP.TenderPage(driver)
        lot_form = LF.LotForm(driver)
        item_form = IF.ItemForm(driver)
        feature_form = FF.FeatureForm(driver)
        document_form = DF.DocumentForm(driver)
        date_widget = DW.DateWidget(driver)

    return App


@pytest.fixture(scope='session')
def url():
    env = settings.ENV
    return settings.BASE_URL[env]


@pytest.fixture(scope='session')
def user():
    env = settings.ENV
    users = {
        'prod': settings.USERS_PROD,
        'stage': settings.USERS_STAGE,
        'dev23': settings.USERS_DEV23,
        'dev24': settings.USERS_DEV24
    }.get(env)

    class User:
        owner = users['owner']
        provider1 = users['provider1']
        provider2 = users['provider2']

    return User


@pytest.fixture(scope='session')
def file_path():
    file_path = settings.FILE_PATH
    return file_path
