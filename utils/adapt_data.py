from utils import text_hundler as TH


class TenderAdaptData:

    def __init__(self, data):
        self.data = data

    @property
    def title(self):
        return self.data['title']

    @property
    def description(self):
        return self.data['description']

    def lot_title(self, index):
        return self.data['lots'][index]['title']

    def lot_description(self, index):
        return self.data['lots'][index]['description']

    def lot_value_amount(self, index):
        return str(self.data['lots'][index]['value']['amount'])

    def lot_minimalstep_amount(self, index):
        return str(self.data['lots'][index]['minimalStep']['amount'])

    def item_description(self, index):
        return self.data['items'][index]['description']

    def item_quantity(self, index):
        return str(self.data['items'][index]['quantity'])

    def unit_name(self, index):
        return self.data['items'][index]['unit']['name']

    def cpv_id(self, index):
        return self.data['items'][index]['classification']['id']

    def period(self, period, date):
        date = self.data[period][date]
        return {
            'date': TH.get_date(date),
            'hour': TH.get_hour(date),
            'minutes': TH.get_minutes(date)
        }

    def period_delivery(self, index, date):
        date = self.data['items'][index]['deliveryDate'][date]
        return {
            'date': TH.get_date(date),
            'hour': TH.get_hour(date),
            'minutes': TH.get_minutes(date)
        }

    def delivery_address(self, index, value):
        return self.data['items'][index]['deliveryAddress'][value]
