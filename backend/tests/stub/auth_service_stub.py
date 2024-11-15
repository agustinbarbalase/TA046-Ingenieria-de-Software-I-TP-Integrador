from domain.auth.auth_service_interface import AuthServiceInterface


class AuthServiceStub(AuthServiceInterface):

    def __init__(self, users: dict[str, str]):
        super().__init__()
        self.registered_users = users

    @classmethod
    def invalid_user_message_error(cls):
        return "Invalid user"

    @classmethod
    def invalid_password_message_error(cls):
        return "Invalid password"

    def autenticate_user(self, user_id: str, password: str):
        if not user_id in self.registered_users:
            raise Exception(self.invalid_user_message_error())
        elif self.registered_users[user_id] != password:
            raise Exception(self.invalid_password_message_error())
