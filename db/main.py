from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column
from sqlalchemy import Integer, String, DATETIME, TEXT
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine_url = "sqlite:///db//test.db"
engine = create_engine(engine_url, echo=True)


class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(TEXT)
    picture = Column(String(8182))  # Chrome 網址長度上限
    category = Column(String(100))
    youtube = Column(String(8182))  # Chrome 網址長度上限
    slideshare = Column(String(8182))  # Chrome 網址長度上限
    publish_time = Column(DATETIME)
    update_time = Column(DATETIME)


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()

    return session


if __name__ == '__main__':
    drop_table()
    create_table()