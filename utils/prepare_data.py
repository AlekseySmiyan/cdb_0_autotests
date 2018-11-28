import json
import faker
import random
import settings

from utils import date_time as DT


def tender_data(procedure):
    data_file = settings.DATA_FILE.format(file_name='tender.json')
    with open(data_file) as f:
        data = json.load(f)
    # title, description
    data['title'] = '[auto] Tender {}: {}'.format(
        procedure, DT.date_now_format('%Y-%m-%d %H:%M'))
    data['description'] = faker.Faker().text()
    # periods
    if procedure == 'belowThreshold':
        data['enquiryPeriod']['endDate'] = DT.create_date(minutes=5)
        data['tenderPeriod']['startDate'] = DT.create_date(minutes=6)
        data['tenderPeriod']['endDate'] = DT.create_date(minutes=11)
    else:
        del data['enquiryPeriod']
    for i in range(len(data['items'])):
        data['items'][i]['description'] = 'Items {}: description'.format(str(i + 1))
        delivery_date = data['items'][i]['deliveryDate']
        delivery_date['startDate'] = DT.create_date(days=10)
        delivery_date['endDate'] = DT.create_date(days=15)
    # amounts
    for l in range(len(data['lots'])):
        data['lots'][l]['title'] = 'Lot {}: title'.format(str(l + 1))
        data['lots'][l]['description'] = 'Lot {}: description'.format(str(l + 1))
        lot_value = data['lots'][l]['value']
        lot_value['amount'] = random.randint(15000, 30000)
        data['value']['amount'] += lot_value['amount']
        lot_step = data['lots'][l]['minimalStep']
        lot_step['amount'] = int(lot_value['amount'] * 0.01)
        data['minimalStep']['amount'] += lot_step['amount']
    return data






