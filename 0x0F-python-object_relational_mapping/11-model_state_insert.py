#!/usr/bin/python3
"""
<<<<<<< HEAD
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print('{0}'.format(new_state.id))
    session.close()`
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
    session.add(State(name='Louisiana'))
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()
    print("{}".format(new_state.id))
    session.close()
>>>>>>> 6bc38d55d7c11b5ed20573d6bc2e4a1916c0b68d
