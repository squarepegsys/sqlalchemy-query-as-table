from tables import *
from query import Fandom
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Create in-memory SQLite database
engine = create_engine("sqlite:///:memory:", echo=False)

# Create all tables
Base.metadata.create_all(engine)


# Sample data
def populate_database():
    with Session(engine) as session:
        # Create People
        p1 = Person(name="Stephen King", email="sking@example.com")
        p2 = Person(name="J.K. Rowling", email="jkr@example.com")
        p3 = Person(name="John Smith", email="john@example.com")
        p4 = Person(name="Jane Doe", email="jane@example.com")
        p5 = Person(name="Bob Wilson", email="bob@example.com")

        session.add_all([p1, p2, p3, p4, p5])
        session.flush()  # Flush to get IDs

        # Create Authors
        author1 = Author(person=p1, biography="Horror and supernatural fiction writer")
        author2 = Author(person=p2, biography="Fantasy fiction writer")

        session.add_all([author1, author2])
        session.flush()

        # Create Books
        book1 = Book(title="The Shining", isbn="9780307743657", author=author1)
        book2 = Book(title="The Stand", isbn="9780307743680", author=author1)
        book3 = Book(
            title="Harry Potter and the Philosopher's Stone",
            isbn="9780747532699",
            author=author2,
        )
        book4 = Book(
            title="Harry Potter and the Chamber of Secrets",
            isbn="9780747538486",
            author=author2,
        )

        session.add_all([book1, book2, book3, book4])
        session.flush()

        # Create Fans
        fan1 = Fan(person=p3, favorite_genre="Horror")
        fan2 = Fan(person=p4, favorite_genre="Fantasy")
        fan3 = Fan(person=p5, favorite_genre="Fantasy")

        # Add favorite books to fans
        fan1.favorite_books.extend([book1, book2])
        fan1.favorite_books.extend([book1, book3])
        fan2.favorite_books.extend([book3, book4])
        fan3.favorite_books.extend([book1, book3])

        session.add_all([fan1, fan2, fan3])

        # Commit all changes
        session.commit()
