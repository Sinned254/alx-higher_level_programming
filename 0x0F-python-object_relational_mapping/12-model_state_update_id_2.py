#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
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

    # Query the database for the state with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # Change the name of the state to New Mexico
    if state:
        state.name = 'New Mexico'
        session.commit()
    else:
        print('State not found')
