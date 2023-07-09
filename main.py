from fastapi import FastAPI
from models.product import Product

app = FastAPI()

products = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 20,
        "stock": 10
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 40,
        "stock": 20
    }
]

@app.get("/")
def message():
    return "Hola Mundo!!"

@app.get("/products")
def get_products():
    return products

@app.get("/products/{id}")
def get_product(id: int):
    return list(filter(lambda item: item["id"] == id, products))

@app.get("/products/")
def get_products_by_stock(stock:int, price: float):
    return list(filter(lambda item: item["stock"] == stock and item["price"] == price, products))

#ruta para agregar datos, usa como parametro un product
@app.post("/products")
def create_product(product:Product):
    products.append(product)
    return products

#ruta para modificar datos
@app.put("/produtcts/{id}")
def update_product(id: int, product:Product):
    for index, item in enumerate(products):
        if item["id"] == id:
            products[index]['name'] = product.name
            products[index]['stock'] = product.stock
            products[index]['price'] = product.price
    return products  

#ruta para eliminar datos
@app.delete("/produtcts/{id}")
def delete_product(id: int):
    for item in products:
        if item["id"] == id:
            products.remove(item)
    return products        

    


