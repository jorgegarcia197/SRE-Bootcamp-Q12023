# These functions need to be implemented
from engine import get_user_by_username, Users, engine
import hashlib
import os
from jose import JWTError, jwt
from dotenv import load_dotenv

load_dotenv()

ALGORITHM = "HS256"
SECRET = os.environ.get("SECRET_KEY")


class Token:
    def generate_token(self, username, password):
        user = get_user_by_username(username)
        if user is None:
            return "Invalid username"
        else:
            # Validate password with salt
            if user.password == self.validate_password(password, user.salt):
                # Generate token
                return self.create_jwt_token(user.role)
            else:
                return "Invalid password"

    def validate_password(self, password, salt):
        concatted = password + salt
        hashed = hashlib.sha512(concatted.encode())
        print(f"hashed pass: {hashed.hexdigest()}")
        return hashed.hexdigest()

    def create_jwt_token(self, role):
        payload = {"role": role}
        token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
        return token


class Restricted:
    def access_data(self, authorization):
        return "test"
