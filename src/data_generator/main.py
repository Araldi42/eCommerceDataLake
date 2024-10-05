from transaction_generator import transactionGenerator
from client_generator import clientGenerator
from product_generator import productGenerator

def main():
    num_records = 1000
    client_gen = clientGenerator(num_records)
    product_gen = productGenerator(num_records)
    
    client_data = client_gen.generate()
    product_data = product_gen.generate()
    transaction_gen = transactionGenerator(num_records,
                                           [client['client_id'] for client in client_data],
                                           [product['product_id'] for product in product_data])
    transaction_data = transaction_gen.generate()
    print(transaction_data)

if __name__ == '__main__':
    main()
    