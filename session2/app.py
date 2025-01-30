from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Role
from config import Config


engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)

session = Session()

Base.metadata.create_all(engine)


def create_user(name, email, role_id):
    new_user = User(name=name, email=email, role_id=role_id)
    session.add(new_user)
    session.commit()
    print(f"User {name} added successfuly")
    
def get_user(user_id):
    user = session.query(User).filter(User.id == user_id).first() 
    if user:
        print(f"User found :{user.name}, {user.email}")  
    else:
        print("User not found") 
        
def update_user(user_id, name=None, email = None, role_id=None) :
    user = session.query(User).filter(User.id == user_id).first() 
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        if role_id:
            user.role_id = role_id 
            
        session.commit()  
        print(f"User {user_id} Updated") 
    else:
        print("User not found")
        
def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first() 
    if user:
        session.delete(user)
        session.commit()
        print(f"User {user_id} deleted")
    else:
        print("User not found") 
        
def list_users():
    users = session.query(User).all()  
    for user in users:
        print(user.name)   
if __name__ == "__main__":
    # create_user("sara", "sara@example.com", 1)
    # create_user("samin", "samin@example.com", 2)
    # create_user("artin", "artin@example.com", 1)
    # get_user(1)
    # update_user(1, name="samin")
    # delete_user(1)
    list_users()