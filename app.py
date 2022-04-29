from milkjug.api import Api
from milkjug.middleware import Middleware

app = Api()

@app.route("/text")
def text_handler():
    return "Hello World!"

@app.route("/json")
def json_handler():
    return {"message": "Hello World!"}

@app.route("/products")
def route_with_query_parameters_handler(id):
    return id

@app.route("/products/{id}")
def route_with_path_parameters_handler(id):
    return id

@app.route("/sales/{product_template_id}")
def route_with_path_and_query_parameters_handler(product_template_id, id):
    return f"{product_template_id} {id}"

class SecretMiddleware(Middleware):
    def modify_request(self, environ):
        environ["SECRET"] = "Classified"
        return environ

app.add_middleware(SecretMiddleware)