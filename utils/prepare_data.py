import json
import random

import settings
from utils import date_time as DT

env = settings.ENV


def tender_data(procedure):
    data_file = settings.DATA_FILE.format(file_name='tender.json')
    with open(data_file) as f:
        data = json.load(f)
    # title, description
    data['title'] = '[auto] Tender {}: {}'.format(
        procedure, DT.date_now_format('%Y-%m-%d %H:%M'))
    data['description'] = 'Description'
    # periods
    if procedure == 'belowThreshold' and env in ['dev23', 'dev24']:
        data['enquiryPeriod']['endDate'] = DT.create_date(minutes=5)
        data['tenderPeriod']['startDate'] = DT.create_date(minutes=6)
        data['tenderPeriod']['endDate'] = DT.create_date(minutes=20)
    elif procedure == 'belowThreshold' and env in ['prod', 'stage']:
        data['enquiryPeriod']['endDate'] = DT.create_date(minutes=60 * 24 + 5)
        data['tenderPeriod']['startDate'] = DT.create_date(minutes=60 * 24 + 6)
        data['tenderPeriod']['endDate'] = DT.create_date(minutes=60 * (24 * 2) + 7)
    else:
        del data['enquiryPeriod']
    for i in range(len(data['items'])):
        data['items'][i]['description'] = 'Items {}: description'.format(str(i + 1))
        delivery_date = data['items'][i]['deliveryDate']
        delivery_date['startDate'] = DT.create_date(days=10)
        delivery_date['endDate'] = DT.create_date(days=15)
    # amounts
    value_amount = 0
    minimal_step_amount = 0
    for l in range(len(data['lots'])):
        data['lots'][l]['title'] = 'Lot {}: title'.format(str(l + 1))
        data['lots'][l]['description'] = 'Lot {}: description'.format(str(l + 1))
        # value amount
        lot_value = data['lots'][l]['value']
        lot_value['amount'] = round(random.uniform(1000, 10000.9), 1)
        value_amount += lot_value['amount']
        data['value']['amount'] = float('{:.2f}'.format(value_amount))
        # minimal step amount
        lot_step = data['lots'][l]['minimalStep']
        lot_step['amount'] = round(lot_value['amount'] * 0.01, 1)
        minimal_step_amount += lot_step['amount']
        data['minimalStep']['amount'] = float('{:.2f}'.format(minimal_step_amount))
    return data



