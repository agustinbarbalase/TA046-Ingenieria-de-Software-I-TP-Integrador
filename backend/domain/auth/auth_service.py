from domain.auth.auth_service_interface import AuthServiceInterface


class AuthService(AuthServiceInterface):

    def __init__(self):
        super().__init__()

    def autenticate_user(self, user: str, password: str):
        return False
