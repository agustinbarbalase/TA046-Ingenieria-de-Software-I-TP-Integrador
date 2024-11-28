from abc import abstractmethod


class AuthServiceInterface:
    """Error messages - class"""

    @abstractmethod
    def invalid_user_message_error(cls):
        pass

    @abstractmethod
    def invalid_password_message_error(cls):
        pass

    """Initialization"""

    @abstractmethod
    def __init__(self, registered_users: dict[str, str]):
        pass

    """Main protocol"""

    @abstractmethod
    def autenticate_user(self, user_id: str, password: str):
        pass
