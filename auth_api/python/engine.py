from sqlmodel import SQLModel, create_engine, Session, select
from typing import Optional
from sqlmodel import Field

# connect to a sql database in amazon aws
engine = create_engine()


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
