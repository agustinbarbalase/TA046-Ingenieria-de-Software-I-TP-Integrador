from domain.auth.auth_service_interface import AuthServiceInterface


class AuthServiceStub(AuthServiceInterface):
    """Initialization"""

    def __init__(self, registered_users: dict[str, str]):
        self.registered_users = registered_users

    @classmethod
    def with_users(cls, registered_users: dict[str, str]):
        return cls(registered_users)

    """Error messages"""

    @classmethod
    def invalid_user_message_error(cls):
        return "Invalid user"

    @classmethod
    def invalid_password_message_error(cls):
        return "Invalid password"

    """Main protocol"""

    def autenticate_user(self, user_id: str, password: str):
        if not user_id in self.registered_users:
            raise Exception(self.invalid_user_message_error())
        elif self.registered_users[user_id] != password:
            raise Exception(self.invalid_password_message_error())
