from entities.user import User
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username.strip()) <= 3:
            raise UserInputError("Selected username is not long enough")

        if re.match("^[a-z]+$", username):
            pass
        else:
            raise UserInputError("Selected username is in incorrect format")

        if len(password) <= 3:
            raise UserInputError("Selected password is not long enough")
        
        if any(char.isdigit() for char in password):
            pass
        else:
            raise UserInputError("Selected password must have both numbers and letters")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
