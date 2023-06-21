#!/usr/bin/python3
"""
<<<<<<< HEAD
This script prints the first State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == argv[4]).first()
    if state is not None:
        print('{0}'.format(state.id))
    else:
        print("Not found")
=======
9-model_state_filter_a module
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
>>>>>>> 6bc38d55d7c11b5ed20573d6bc2e4a1916c0b68d
