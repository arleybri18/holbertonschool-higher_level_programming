#!/usr/bin/python3
""" Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    name_state = session.query(State).filter(State.name == 'Louisiana').first()
    if not name_state:
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        session.refresh(new_state)
        print(new_state.id)
    session.close()
