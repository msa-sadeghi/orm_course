from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import User

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()


Session = sessionmaker(bind=engine)
session = Session()

# new_user = User(name="sara", family ="blala", email = "test@gmail.com")
# session.add(new_user)
# session.commit()

users = session.query(User.name)

for user in users:
    print(user)






# import sqlite3

# conn = sqlite3.connect("test.db")
# cursor = conn.cursor()

# def create_table(tb_name):
#     sqlcommand = f"""
#     CREATE TABLE IF NOT EXISTS {tb_name}(
#         id int primarykey AUTO_INCREMENT,
#         name TEXT NOT NULL,
#         family TEXT NOT NULL,
#         email TEXT 
#     )
#     """
#     cursor.execute(sqlcommand)
    
# if __name__ == "__main__":
#     while True:
#         user_input = int(input("enter 0 to exit or 1 to create table "))
#         if user_input == 1:
#             tb_name = input("enter the table name: ").lower()
#             create_table(tb_name)
#         elif user_input == 0:
#             break