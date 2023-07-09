from fastapi import APIRouter
from models.product import Product

router = APIRouter()

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

@router.get("/products")
def get_products():
    return products

@router.get("/products/{id}")
def get_product(id: int):
    return list(filter(lambda item: item["id"] == id, products))

@router.get("/products/")
def get_products_by_stock(stock:int, price: float):
    return list(filter(lambda item: item["stock"] == stock and item["price"] == price, products))

#ruta para agregar datos, usa como parametro un product
@router.post("/products")
def create_product(product:Product):
    products.append(product)
    return products

#ruta para modificar datos
@router.put("/produtcts/{id}")
def update_product(id: int, product:Product):
    for index, item in enumerate(products):
        if item["id"] == id:
            products[index]['name'] = product.name
            products[index]['stock'] = product.stock
            products[index]['price'] = product.price
    return products  

#ruta para eliminar datos
@router.delete("/produtcts/{id}")
def delete_product(id: int):
    for item in products:
        if item["id"] == id:
            products.remove(item)
    return products        
