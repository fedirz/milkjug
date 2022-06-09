# milkjug
MilkJug - WSGI Web-Framework
# Installation
`pip install milkjug`
# Usage
```
from milkjug.api import Api

app = Api()

products = [
  {"id": 0, "name": "T-Shirt", "price": 15},
  {"id": 1, "name": "Sneakers", "price": 129}
]

@app.get("/products")
def products():
  return products
 
@app.get("/products/{id}")
def products(id):
  return [products[i] for i in range(len(products)) if i == int(id)][0]
```
