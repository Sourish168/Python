from pydantic import BaseModel

# TODO: Create Product Model with id, name, price, in_stock

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

input_data = {
    "id": 1134423412025,
    "name": "POCO M5 5G Smartphone",
    "price": 9499,
    "in_stock": 0
}

product = Product(**input_data)
print(product)