#!/usr/bin/env python3

from fill_db import populate_database, engine
from query import Fandom

from sqlalchemy.orm import Session

if __name__ == "__main__":
    populate_database()

    print("All the Fans")
    with Session(engine) as session:
        for x in session.query(Fandom).all():
            print(x.fan_name, x.author_name, x.title)

    print("\nFans who favorited Stephen King")
    with Session(engine) as session:
        for x in (
            session.query(Fandom).filter(Fandom.author_name == "Stephen King").all()
        ):
            print(x.fan_name, x.author_name, x.title)
