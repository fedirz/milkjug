import pytest

def test_route_that_returns_text(app, client):
    @app.route("/text")
    def text_handler():
        return "Hello World!"
    
    assert client.get("http://localhost:8000/text").text == "Hello World!"

def test_route_that_returns_json(app, client):
    @app.route("/json")
    def json_handler():
        return {"messsage": "Hello World!"}
    
    assert client.get("http://localhost:8000/json").json == {"messsage": "Hello World!"}

def test_route_that_returns_array(app, client):
    @app.route("/array")
    def array_handler():
        return ["Hello World!"]
    
    assert client.get("http://localhost:8000/array").json == ["Hello World!"]

def test_route_with_query_param(app, client):
    @app.route("/query")
    def query_handler(param):
        return param
    
    assert client.get("http://localhost:8000/query?param=Hello World!").text == "Hello World!"

def test_route_with_path_params(app, client):
    @app.route("/path/{param}")
    def path_handler(param):
        return param
    
    assert client.get("http://localhost:8000/path/Hello%20World!").text == "Hello World!"

def test_route_with_path_and_query_params(app, client):
    @app.route("/path_and_query/{path_aparam}")
    def path_and_query_handler(path_aparam, query_param):
        return path_aparam + query_param
    
    assert client.get("http://localhost:8000/path_and_query/Hello%20?query_param=World!").text == "Hello World!"

def test_adding_existing_route_throws_exception(app, client):
    @app.route("/")
    def index_handler_1(): pass

    with pytest.raises(Exception):
        @app.route("/")
        def index_handler_2(): pass

def test_html_template_rendering(app, client):
    @app.route("/html")
    def handler_that_renderes_an_html_template():
        return app.template('index.html', {"title": "Hello", "message": "World!"})
    
    response = client.get("http://localhost:8000/html")
    #assert "text/html" in response.headers["Content-Type"]
    assert "Hello" in response.text 
    assert "World!" in response.text 