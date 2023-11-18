#!/usr/bin/python3
"""
Python script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Set up connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the database for all states with a name containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete all states with a name containing the letter 'a'
    for state in states:
        session.delete(state)

    # Commit the session to the database
    session.commit()
