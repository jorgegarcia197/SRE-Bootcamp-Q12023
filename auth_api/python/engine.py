from sqlmodel import SQLModel, create_engine, Session, select, Field
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()
SQL_URL = os.environ.get("SQL_URL")

# connect to a sql database in amazon aws
engine = create_engine(SQL_URL, echo=True)


# create a class to represent a table in the database (users)
class Users(SQLModel, table=True):
    username: Optional[str] = Field(None, primary_key=True)
    salt: str
    password: str
    role: str


def get_user_by_username(username: str) -> Users:
    with Session(engine) as session:
        statement = select(Users).where(Users.username == username)
        user = session.exec(statement).first()
        return user


print(get_user_by_username("admin"))
