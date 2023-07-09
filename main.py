from fastapi import FastAPI
from routers.product import router as product_router  

app = FastAPI()

@app.get("/")
def message():
    return "Hola Mundo!!"

#codigo para importar todas las rutas de la carpeta routes
app.include_router(product_router)



    


