from utils.generator import Generator
import numpy as np
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

    def generate(self) -> list:
        ''''''
        data = []
        
        for i in range(self.__num_records):
            record = {}
            record['client_id'] = np.random.choice(self.__random_client_id)
            record['product_id'] = np.random.choice(self.__random_product_id)
            record['paymeny_method'] = np.random.choice(['credit_card', 'debit_card', 'pix'], p=[0.6, 0.3, 0.1])
            record['quantity'] = self.fake.random_int(min=1, max=5, p=[0.6, 0.2, 0.1, 0.05, 0.05])
            record['date'] = self.fake.date_this_year(before_today=True, after_today=False)
            data.append(record)

    