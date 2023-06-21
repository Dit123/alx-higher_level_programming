#!/usr/bin/python3
<<<<<<< HEAD
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    cal_state = State(name='California')
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)

    session.add(cal_state)
=======
"""adds the State object “California”
with the City “San Francisco”
to the database hbtn_0e_100_usa"""

if __name__ == "__main__":

    import sys
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_city = City(name='San Francisco')
    new = State(name='California')
    new.cities.append(new_city)
    session.add_all([new, new_city])
>>>>>>> 6bc38d55d7c11b5ed20573d6bc2e4a1916c0b68d
    session.commit()
    session.close()
