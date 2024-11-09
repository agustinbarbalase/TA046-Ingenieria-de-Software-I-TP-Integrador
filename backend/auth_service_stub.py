from backend.auth_service_interface import AuthServiceInterface


class AuthServiceMock(AuthServiceInterface):

    def __init__(self):
        super().__init__()
        self.registered_users = {"Nacho": "12345", "Agus": "54321"}

    def autenticate_user(self, user: str, password: str):
        if not user in self.registered_users:
            return False
        return password is not self.registered_users[user]
