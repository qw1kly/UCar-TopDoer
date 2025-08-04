from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker

from models.models import Base

class Connect:
    def open(self):
        engine = create_engine('sqlite:///reviews.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        self.session = Session()

    def close(self):
        self.session.close()


manager = Connect()
