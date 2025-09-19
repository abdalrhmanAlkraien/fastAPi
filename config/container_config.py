from dependency_injector import containers, providers

from models.base import Base
from service.book_service import BookService
from service.author_service import AuthorService
from service.category_service import CategoryService
from database.connection import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from repository.book_repository import BookRepository
from repository.author_repository import AuthorRepository
from repository.category_repository import CategoryRepository


class Container(containers.DeclarativeContainer):
    containers_config = containers.WiringConfiguration([
        ".controller",
        ".service",
        ".repository"
    ])

    config_file = providers.Configuration(yaml_files=["config.yml"])

    print(config_file.db.connection.string)

    engine = providers.Singleton(create_engine,
                                 "postgresql+psycopg2://admin:admin@localhost:5432/py_db",
                                 pool_pre_ping=True)

    sessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine()
    )

    Base.metadata.create_all(bind=engine())

    # db_session = providers.Factory(sessionLocal) // wrong way
    db_session = providers.Factory(sessionLocal) # correct way
    book_repository = providers.Factory(BookRepository, db_session)
    author_repository = providers.Factory(AuthorRepository, db_session)
    category_repository = providers.Factory(CategoryRepository, db_session)

    auth_service = providers.Singleton(AuthorService, author_repository)
    category_service = providers.Singleton(CategoryService, category_repository)
    book_service = providers.Singleton(BookService, book_repository)

