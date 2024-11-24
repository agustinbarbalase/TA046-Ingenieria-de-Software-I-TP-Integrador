from abc import abstractmethod


class AuthServiceInterface:
    """Initialization"""

    @abstractmethod
    def __init__(self, registered_users: dict[str, str]):
        pass

    """Error messages"""

    @abstractmethod
    def invalid_user_message_error(cls):
        pass

    @abstractmethod
    def invalid_password_message_error(cls):
        pass

    """Main protocol"""

    @abstractmethod
    def autenticate_user(self, user_id: str, password: str):
        pass
