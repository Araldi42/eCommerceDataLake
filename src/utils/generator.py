from abc import ABC, abstractmethod

class Generator(ABC):
    
    def __init__(self, schema, num_records):
        self.__schema = schema
        self.__num_records = num_records

    @abstractmethod
    def generate(self) -> list:
        pass