# These functions need to be implemented
from engine import get_user_by_username
from jwt_bearer import create_jwt_token, decode_jwt
import hashlib

class Token:
    def generate_token(self, username, password):
        user = get_user_by_username(username)
        if user is None:
            return "Invalid username"
        else:
            # Validate password with salt
            if user.password == self.validate_password(password, user.salt):
                # Generate token
                return create_jwt_token(user.username,user.role)
            else:
                return "Invalid password"

    def validate_password(self, password, salt):
        concatted = password + salt
        hashed = hashlib.sha512(concatted.encode())
        return hashed.hexdigest()


class Restricted:
    def is_valid_user(self, username, role):
        queried_user = get_user_by_username(username)
        if queried_user.username == username and queried_user.role == role:
            return True
        else:
            return False

    def access_data(self, authorization):
        try:
            decoded_token = decode_jwt(authorization)
            # check if the role corresponds to any in the database
            if decoded_token and self.is_valid_user(
                decoded_token.get("username", None), decoded_token.get("role", None)
            ):
                return "You are under protected data"
            else:
                return "Invalid token"
        except:
            return "Invalid token"
