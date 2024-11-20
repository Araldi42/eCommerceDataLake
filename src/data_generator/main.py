from fastapi import FastAPI
from transaction_generator import transactionGenerator
from client_generator import clientGenerator
from product_generator import productGenerator

app = FastAPI()

@app.get("/clients")
def generate_clients(num_records: int):
    client_gen = clientGenerator(num_records)
    client_data = client_gen.generate()
    return client_data

@app.get("/products")
def generate_products(num_records: int):
    product_gen = productGenerator(num_records)
    product_data = product_gen.generate()
    return product_data

@app.get("/transactions")
def generate_transactions(num_records: int, client_ids: list, product_ids: list):
    transaction_gen = transactionGenerator(num_records, client_ids, product_ids)
    transaction_data = transaction_gen.generate()
    return transaction_data

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
