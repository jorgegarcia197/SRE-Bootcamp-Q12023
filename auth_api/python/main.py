from fastapi import FastAPI,Form
from methods import Token, Restricted


app = FastAPI()

login = Token()
protected = Restricted()

@app.get("/")
def url_root():
    return "OK"


@app.get("/_health")
def url_health():
    return "OK"

@app.post("/login")
def url_login(username: str= Form(), password: str= Form()):
    res = {
        "data": login.generate_token(username, password)
    }
    return res


@app.get("/protected")
def url_protected(auth_token: str):
    res = {
        "data": protected.access_data(auth_token)
    }
    return res


