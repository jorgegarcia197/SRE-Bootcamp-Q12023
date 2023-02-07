import unittest
from src.methods import Token, Restricted
from src.jwt_bearer import verify_jwt, create_jwt_token, decode_jwt


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()
        self.generated_token_no_admin = self.convert.generate_token(
            "noadmin", "noPow3r"
        )
        self.generated_token_admin = self.convert.generate_token("admin", "secret")
        self.generated_token_bob = self.convert.generate_token(
            "bob", "thisIsNotAPasswordBob"
        )

    def test_generate_token_admin(self):
        decoded = decode_jwt(self.generated_token_admin)
        print(self.generated_token_admin)
        self.assertEqual("admin", decoded.get("username", None))

    def test_access_data_admin(self):
        self.assertEqual(
            "You are under protected data",
            self.validate.access_data(self.generated_token_admin),
        ),

    def test_generate_token_no_admin(self):
        decoded = decode_jwt(self.generated_token_no_admin)
        self.assertEqual("noadmin", decoded.get("username", None))

    def test_generate_token_bob(self):
        decoded = decode_jwt(self.generated_token_bob)
        self.assertEqual("bob", decoded.get("username", None))

    def test_access_data_bob(self):
        self.assertEqual(
            "You are under protected data",
            self.validate.access_data(
                self.generated_token_bob,
            ),
        )

    def test_generate_invalid_token(self):
        self.assertEqual(
            "Invalid username",
            self.convert.generate_token("jorgegarcia197", "JorgeSerna"),
        )

    def test_invalid_token(self):
        self.assertEqual(
            "Invalid token",
            self.validate.access_data("ARandomToken"),
        )


if __name__ == "__main__":
    unittest.main()
