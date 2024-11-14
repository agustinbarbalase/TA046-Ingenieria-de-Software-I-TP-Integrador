from abc import abstractmethod


class AuthServiceInterface:

    @abstractmethod
    def autenticate_user(self, user_id: str, password: str):
        pass

    @abstractmethod
    def invalid_user_message_error(self):
        pass

    @abstractmethod
    def invalid_password_message_error(self):
        pass
