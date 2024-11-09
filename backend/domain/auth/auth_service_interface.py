from abc import abstractmethod


class AuthServiceInterface:

    @abstractmethod
    def autenticate_user(self, user: str, password: str) -> bool:
        pass
