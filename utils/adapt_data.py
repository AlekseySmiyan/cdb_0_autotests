from utils import date_time


class TenderAdaptData:

    def __init__(self, data):
        self.data = data

    def title(self):
        return self.data['title']

    def description(self):
        return self.data['description']

    def lot_title(self, index):
        return self.data['lots'][index]['title']

    def lot_description(self, index):
        return self.data['lots'][index]['description']

    def value_amount(self):
        return self.data['value']['amount']

    def minimalstep_amoumt(self):
        return self.data['minimalStep']['amount']

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
        value = self.data[period][date]
        return {
            'date': date_time.adapt_date(value, '%Y-%m-%d'),
            'hour': date_time.adapt_date(value, '%H'),
            'minutes': date_time.adapt_date(value, '%M')
        }

    def period_delivery(self, index, date):
        value = self.data['items'][index]['deliveryDate'][date]
        return {
            'date': date_time.adapt_date(value, '%Y-%m-%d'),
            'hour': date_time.adapt_date(value, '%H'),
            'minutes': date_time.adapt_date(value, '%M')
        }

    def date_delivery(self, index, period):
        date_delivery = self.data['items'][index]['deliveryDate']['{}Date'.format(period)]
        return date_time.adapt_date(date_delivery, '%Y-%m-%d %H:%M')

    def delivery_address(self, index, value):
        return self.data['items'][index]['deliveryAddress'][value]

    def full_delivery_address(self, index):
        keys = ['postalCode', 'countryName', 'region', 'locality', 'streetAddress']
        list_values = []
        for key in keys:
            list_values.append(self.data['items'][index]['deliveryAddress'][key] + ',')
        full_address = ' '.join(list_values)
        return full_address

    def feature(self, index, value):
        return self.data['features'][index][value]

    def options(self, index):
        return self.data['features'][index]['enum']

    def option(self, index_feature, index_option, value):
        return self.data['features'][index_feature]['enum'][index_option][value]


