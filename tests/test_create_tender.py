import pytest
from utils import prepare_data, adapt_data
from pages import builder


@pytest.fixture(scope='module', autouse=True)
def owner_login(app, url, user):
    login = user.owner['login']
    password = user.owner['password']
    user_name = user.owner['user_name']
    app.login_page.go(url).autn(login, password)
    return user_name == app.home_page.get_user_name()


@pytest.mark.below
class TestCreateTenderBelow:

    data = prepare_data.tender_data('belowThreshold')
    data = adapt_data.TenderAdaptData(data)

    @pytest.mark.order1
    def test_owner_login(self, owner_login):
        assert owner_login is True

    @pytest.mark.order2
    def test_create_tender(self, app, file_path):
        tb = builder.TenderBuilder(app, self.data, file_path=file_path)
        tb.create_tender_below_multi()













