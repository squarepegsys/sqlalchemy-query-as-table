from tables import *
from sqlalchemy import select
from sqlalchemy.orm import aliased

FanPerson = aliased(Person, name="fan_person")
AuthorPerson = aliased(Person, name="author_person")

fandom_q = (
    select(
        Book.id,
        Fan.id,
        FanPerson.name.label("fan_name"),
        Book.title,
        AuthorPerson.name.label("author_name"),
    )
    .select_from(Fan)  # explicitly say where to start
    .join(FanPerson, Fan.person_id == FanPerson.id)  # Join to fan's person details
    .join(Fan.favorite_books)  # Join to books
    .join(Book.author)  # Join to author
    .join(
        AuthorPerson, Author.person_id == AuthorPerson.id
    )  # Join to author's person details
    .subquery()
)


class Fandom(Base):
    __table__ = fandom_q
    __mapper_args__ = {
        "primary_key": [Book.id, Fan.id]
    }  # using Book.id and Fan.id as the primary ensures we see all the rows
