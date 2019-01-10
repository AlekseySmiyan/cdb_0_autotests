import pytest
from utils import prepare_data, adapt_data, text_hundler, date_time
from pages import builder


@pytest.fixture(scope='module', autouse=True)
def owner_login(app, url, user):
    login = user.owner['login']
    password = user.owner['password']
    user_name = user.owner['user_name']
    app.login_page.go(url).autn(login, password)
    return user_name == app.home_page.get_user_name()


def pytest_namespace():
    return {'tender_id': None}


def index_lot(val):
    return 'index lot: {}'.format(val)


def index_item(val):
    return 'index item: {}'.format(val)


@pytest.mark.below
class TestCreateTenderBelow():
    data = prepare_data.tender_data('belowThreshold')
    data = adapt_data.TenderAdaptData(data)

    @pytest.fixture(scope='function', params=[0, 1], ids=index_lot)
    def lot_index(self, request):
        return request.param

    @pytest.fixture(scope='function', params=[0, 1, 2], ids=index_item)
    def item_index(self, request):
        return request.param

    @pytest.mark.order1
    def test_owner_login(self, owner_login):
        assert owner_login is True

    @pytest.mark.order2
    def test_create_tender(self, app, file_path):
        tb = builder.TenderBuilder(app, self.data, file_path=file_path)
        tb.create_tender_below_multi()
        pytest.tender_id = app.tender_page.tender_id
        assert bool(pytest.tender_id) is True

    @pytest.mark.order3
    def test_search_tender(self, app):
        list_tenders = app.home_page.search_tender(pytest.tender_id)
        assert len(list_tenders) == 1

    @pytest.mark.order4
    def test_view_tender_id(self, app):
        app.home_page.go_tender(pytest.tender_id)
        actual = app.tender_page.tender_id
        expected = pytest.tender_id
        assert actual == expected

    @pytest.mark.order5
    def test_view_tender_title(self, app):
        actual = app.tender_page.tender_title
        expected = '[ТЕСТУВАННЯ] ' + self.data.title()
        assert actual == expected

    @pytest.mark.order6
    def test_view_tender_description(self, app):
        actual = app.tender_page.tender_description
        expected = self.data.description()
        assert actual == expected

    @pytest.mark.order7
    def test_view_tender_value_amount(self, app):
        actual = float(app.tender_page.tender_value_amount)
        expected = self.data.value_amount()
        assert actual == expected

    @pytest.mark.order8
    def test_view_quantity_lots(self, app):
        assert len(app.tender_page.list_lots) == 2

    @pytest.mark.order9
    def test_view_lot_title(self, app, lot_index):
        actual = app.tender_page.lot_title(lot_index)
        expected = self.data.lot_title(lot_index)
        assert actual == expected

    @pytest.mark.order10
    def test_view_lot_description(self, app, lot_index):
        actual = app.tender_page.lot_description(lot_index)
        expected = self.data.lot_description(lot_index)
        assert actual == expected

    @pytest.mark.order11
    def test_view_lot_value_amount(self, app, lot_index):
        actual = float(app.tender_page.lot_value_amount(lot_index))
        expected = float(self.data.lot_value_amount(lot_index))
        assert actual == expected

    @pytest.mark.order12
    def test_view_lot_minimalstep_amount(self, app, lot_index):
        value = app.tender_page.lot_minimalstep_amount(lot_index)
        actual = float(text_hundler.get_minimalstep_value(value))
        expected = float(self.data.lot_minimalstep_amount(lot_index))
        assert actual == expected

    @pytest.mark.parametrize('lot, items_quantity', [(0, 2), (1, 1)])
    @pytest.mark.order13
    def test_view_quantity_items_in_lot(self, app, lot, items_quantity):
        actual = len(app.tender_page.list_lot_items(lot))
        expected = items_quantity
        assert actual == expected

    @pytest.mark.order14
    def test_view_item_description(self, app, item_index):
        actual = app.tender_page.item_description(item_index)
        expected = self.data.item_description(item_index)
        assert actual == expected

    @pytest.mark.order15
    def test_view_item_quantity(self, app, item_index):
        actual = app.tender_page.item_quantity(item_index)
        expected = self.data.item_quantity(item_index)
        assert actual == expected

    @pytest.mark.order16
    def test_view_item_unit_name(self, app, item_index):
        actual = app.tender_page.item_unit_name(item_index)
        expected = self.data.unit_name(item_index)
        assert actual == expected

    @pytest.mark.order17
    def test_view_item_cpv_id(self, app, item_index):
        actual = text_hundler.get_cpv_id(app.tender_page.item_cpv(item_index))
        expected = self.data.cpv_id(item_index)
        assert actual == expected

    @pytest.mark.order18
    def test_view_full_delivery_address(self, app, item_index):
        actual = app.tender_page.full_delivery_address(item_index)
        expected = self.data.full_delivery_address(item_index)
        assert actual == expected

    @pytest.mark.parametrize('period', ['start', 'end'])
    @pytest.mark.order19
    def test_view_delivery_date(self, app, item_index, period):
        date = app.tender_page.delivery_date(item_index, period)
        actual = date_time.adapt_date(date, '%Y-%m-%d %H:%M')
        expected = self.data.date_delivery(item_index, period)
        assert actual == expected

