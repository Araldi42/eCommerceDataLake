import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.generator import Generator
from datetime import datetime, timedelta
import numpy as np
import random
from faker import Faker

class transactionGenerator(Generator):
    ''''''
    def __init__(self, num_records: int, client_id: list, product_id :list) -> None:
        self.__schema = {'client_id',
                         'product_id',
                         'payment_method',
                         'quantity',
                         'date',}
        self.__num_records = num_records
        self.__random_client_id = client_id
        self.__random_product_id = product_id
        self.fake = Faker('pt_BR')
    
    def set_num_records(self, num_records : int) -> None:
        self.__num_records = num_records

    def get_schema(self) -> dict:
        return self.__schema
    
    def get_num_records(self) -> int:
        return self.__num_records

    def generate_random_date(self, start_date: str, end_date: str) -> datetime:
        '''Generate a random date between start_date and end_date'''
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M')
        end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M')
        start = datetime.timestamp(start_date)
        end = datetime.timestamp(end_date)
        random_second = random.randint(0, int(end - start))
        return (start_date + timedelta(seconds=random_second)).strftime('%Y-%m-%d %H:%M')

    def generate(self) -> list:
        ''''''
        data = []
        
        for _ in range(self.__num_records):
            record = {}
            record['client_id'] = random.choice(self.__random_client_id)
            record['product_id'] = random.choice(self.__random_product_id)
            record['paymeny_method'] = random.choice(['credit_card', 'debit_card', 'pix'])
            record['quantity'] = self.fake.random_int(min=1, max=5)
            record['date'] = self.generate_random_date('2023-01-01 00:00', datetime.now().strftime('%Y-%m-%d %H:%M'))
            data.append(record)
        return data

    