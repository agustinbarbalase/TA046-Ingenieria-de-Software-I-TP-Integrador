import sys
import json

from datetime import datetime, timedelta
from flask import Flask, request
from typing import *

from flask_cors import CORS

from utils.clock.clock import Clock
from domain.my_books_app import MyBooksApp
from domain.rest_interface import RestInterface
from domain.auth.auth_service import AuthService
from domain.shopping_history_book import ShopingHistoryBook
from domain.postnet.postnet import Postnet


class TusLibrosWebServer:
    def __init__(
        self, user_session_time: int, catalog: dict[str, str], users: dict[str, str]
    ):
        self.flask_app = Flask(__name__)
        CORS(
            self.flask_app, origins=["http://localhost:3000"], supports_credentials=True
        )

        self.auth = AuthService.with_users(users)
        self.shopping_history = ShopingHistoryBook.new()
        self.postnet = Postnet.new()
        self.clock = Clock.with_time_now()

        self.app = MyBooksApp.with_dependencies(
            catalog,
            self.auth,
            self.clock,
            user_session_time,
            self.shopping_history,
            self.postnet,
        )
        self.rest_interface = RestInterface.with_app(self.app)

        @self.flask_app.route("/createCart", methods=["GET"])
        def create_cart():
            response = self.rest_interface.create_cart(request.args.to_dict())
            return response.body, response.status_code

        @self.flask_app.route("/listCart", methods=["GET"])
        def list_cart():
            response = self.rest_interface.list_cart(request.args.to_dict())
            return response.body, response.status_code

        @self.flask_app.route("/addToCart", methods=["GET"])
        def add_to_cart():
            response = self.rest_interface.add_to_cart(request.args.to_dict())
            return response.body, response.status_code

        @self.flask_app.route("/checkOutCart", methods=["GET"])
        def check_out_cart():
            response = self.rest_interface.checkout(request.args.to_dict())
            return response.body, response.status_code

        @self.flask_app.route("/listPurchases", methods=["GET"])
        def list_purchases():
            response = self.rest_interface.list_purchases(request.args.to_dict())
            return response.body, response.status_code

    def listening_on(self, port: int):
        self.flask_app.run(port=port)


def open_json_file(file_path: str, closure):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return closure(data)
    except FileNotFoundError as err:
        raise Exception(f"The file {file_path} does not exist.")
    except json.JSONDecodeError as err:
        raise Exception("The file is not a valid JSON.")
    except Exception as e:
        raise Exception(e)


if __name__ == "__main__":
    try:
        if len(sys.argv) != 5:
            raise Exception(
                "Abstent params: For run program needs:\n"
                "    <port>: The number of port to raise app\n"
                "    <user_session_time>: The time in seconds for duration of session\n"
                "    <catalog_file_path>: The path where is saved the catalog.\n"
                "    The format is a JSON with a list with dict. The dict have:\n"
                '    "isbn" and "price"\n'
                "    <users_file_path>: The path where is saved the users.\n"
                "    The format is a JSON with a list with dict. The dict have:\n"
                '    "user_id" and "passoword"\n'
            )

        port, user_session_time, catalog_file_path, users_file_path = (
            int(sys.argv[1]),
            int(sys.argv[2]),
            sys.argv[3],
            sys.argv[4],
        )

        def closure_for_catalog(catalog_file):
            catalog: dict[str, str] = {}
            for book in catalog_file:
                catalog[book["isbn"]] = book["price"]
            return catalog

        def closure_for_users(users_file):
            users: dict[str, str] = {}
            for user in users_file:
                users[user["user_id"]] = user["password"]
            return users

        catalog = open_json_file(catalog_file_path, closure_for_catalog)
        users = open_json_file(users_file_path, closure_for_users)

        server = TusLibrosWebServer(user_session_time, catalog, users)
        server.listening_on(port)
    except Exception as err:
        print(f"{err}")
