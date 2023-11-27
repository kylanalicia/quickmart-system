from sqlalchemy import create_engine
from db import Base

def my_commands():
    # Your custom commands or application logic here
    pass

if __name__ == '__main__':
    engine = create_engine()
    Base.metadata.create_all(engine)
    my_commands()
