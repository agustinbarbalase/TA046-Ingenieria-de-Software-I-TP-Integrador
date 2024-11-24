from datetime import datetime
import sys
from flask import Flask, request
from typing import *

from flask_cors import CORS

from domain.my_books_app import MyBooksApp
from domain.rest_interface import RestInterface
from domain.auth.auth_service import AuthService


class TusLibrosWebServer:
    def __init__(self):
        self.flask_app = Flask(__name__)
        self.auth = AuthService.with_users({})
        self.catalog = {
            "9780137314942": "π",  # π = 3.14159
            "9780321278654": "e",  # e = 2.71828
            "9780201710915": "φ",  # φ = 1.61803
            "9780321125217": "γ",  # γ = 0.57721
            "9780735619654": "c",  # c = 299,792,458 m/s
            "9780321146533": "g",  # g = 9.80665 m/s²
        }
        self.app = MyBooksApp.with_catalog_and_auth(self.catalog, self.auth)
        self.rest_interface = RestInterface.with_app(self.app)
        CORS(
            self.flask_app, origins=["http://localhost:3000"], supports_credentials=True
        )

        @self.flask_app.route("/createCart", methods=["GET"])
        def create_cart():
            response = self.rest_interface.create_cart(
                request.args.to_dict(), datetime.now()
            )
            return response.body, response.status_code

        @self.flask_app.route("/listCart", methods=["GET"])
        def list_cart():
            response = self.rest_interface.list_cart(
                request.args.to_dict(), datetime.now()
            )
            return response.body, response.status_code

        @self.flask_app.route("/addToCart", methods=["GET"])
        def add_to_cart():
            response = self.rest_interface.add_to_cart(
                request.args.to_dict(), datetime.now()
            )
            return response.body, response.status_code

        @self.flask_app.route("/checkOutCart", methods=["GET"])
        def check_out_cart():
            response = self.rest_interface.checkout(
                request.args.to_dict(), datetime.now()
            )
            return response.body, response.status_code

    def listening_on(self, port: int):
        self.flask_app.run(port=port)


if __name__ == "__main__":
    port = int(sys.argv[1])
    server = TusLibrosWebServer()
    server.listening_on(port)
