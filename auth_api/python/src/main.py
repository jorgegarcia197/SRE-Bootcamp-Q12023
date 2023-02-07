from fastapi import FastAPI, Form, Depends
from src.methods import Token, Restricted
from src.jwt_bearer import JWTBearer

app = FastAPI()

login = Token()
protected = Restricted()


@app.get("/", tags=["root"])
def url_root():
    return "OK"


@app.get("/_health", tags=["health"])
def url_health():
    return "OK"


@app.post("/login", tags=["login"])
def url_login(username: str = Form(), password: str = Form()):
    res = {"data": login.generate_token(username, password)}
    return res


@app.get("/protected", dependencies=[Depends(JWTBearer())], tags=["protected"])
def url_protected(authorization: str = Depends(JWTBearer())):
    res = {"data": protected.access_data(authorization)}
    return res
