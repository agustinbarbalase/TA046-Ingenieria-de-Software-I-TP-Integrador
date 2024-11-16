import sys
from flask import Flask, request
from typing import *

from flask_cors import CORS

from domain.my_books_app import MyBooksApp
from domain.rest_interface import RestInterface


class TusLibrosWebServer:
    def __init__(self):
        self.flask_app = Flask(__name__)
        self.app = MyBooksApp(set(["Hola"]))
        self.rest_interface = RestInterface(self.app)
        CORS(
            self.flask_app, origins=["http://localhost:3000"], supports_credentials=True
        )

        @self.flask_app.route("/createCart", methods=["GET"])
        def create_cart():
            response = self.rest_interface.create_cart(request.args.to_dict())
            return response.body, response.status_code

        @self.flask_app.route("/listCart", methods=["GET"])
        def list_cart():
            params = request.args.to_dict()
            response = self.rest_interface.list_cart(params["userId"])
            return response.body

        @self.flask_app.route("/addToCart", methods=["GET"])
        def add_to_cart():
            params = request.args.to_dict()
            response = self.rest_interface.add_to_cart(
                params["userId"], params["bookIsbn"], params["bookQuantity"]
            )
            return response.body

    def listening_on(self, port: int):
        self.flask_app.run(port=port)


if __name__ == "__main__":
    port = int(sys.argv[1])
    server = TusLibrosWebServer()
    server.listening_on(port)
