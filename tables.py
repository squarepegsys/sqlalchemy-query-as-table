from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Table

Base = declarative_base()

# Association table for books and fans (many-to-many)
book_fan_association = Table(
    "book_fan_association",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id")),
    Column("fan_id", Integer, ForeignKey("fans.id")),
)


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    biography = Column(String(1000))

    # Relationships
    person = relationship("Person")
    books = relationship("Book", back_populates="author")


class Fan(Base):
    __tablename__ = "fans"

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("people.id"), nullable=False)
    favorite_genre = Column(String(50))

    # Relationships
    person = relationship("Person")
    favorite_books = relationship(
        "Book", secondary=book_fan_association, back_populates="fans"
    )


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    isbn = Column(String(13), unique=True)
    author_id = Column(Integer, ForeignKey("authors.id"))

    # Relationships
    author = relationship("Author", back_populates="books")
    fans = relationship(
        "Fan", secondary=book_fan_association, back_populates="favorite_books"
    )
