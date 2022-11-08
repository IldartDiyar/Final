from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

db = 'postgresql://postgres:postgres@localhost:5432/Final'

Base = declarative_base()


class ShoppingList(Base):
    __tablename__ = 'users_shopping'
    foodList = Column(String(80), unique=True,
                      nullable=False, primary_key=True)
    username = Column(String(80),
                      nullable=False)

    def __repr__(self):
        return f"<Title: {self.foodList}>"


class User(Base):
    __tablename__ = 'users'
    username = Column(String(80), unique=True,
                      nullable=False, primary_key=True)
    password = Column(String(80),
                      nullable=False)

    def __repr__(self):
        return f"<Title: {self.username}>"


class DatabaseM():
    def __init__(self):
        self.engine = create_engine(db, echo=True, future=True)
        Base.metadata.create_all(self.engine)

        # User

    def get_by_pass(self, username, password):
        with Session(self.engine) as session:
            data = session.query(User).filter(
                User.username == username, User.password == password).first()
            if data:
                return True
            return False

    def add_new_User(self, username, password):
        try:
            with Session(self.engine) as session:
                new_user = User(username=username, password=password)
                print(new_user)
                session.add(new_user)
                session.commit()
                return True
        except:
            return False
         # Food

    def get_all_food(self, username):
        with Session(self.engine) as session:
            foods = session.query(ShoppingList).filter(
                ShoppingList.username == username).all()
            return foods

    def add_new(self, new_food, username):
        try:
            with Session(self.engine) as session:
                food = ShoppingList(foodList=new_food, username=username)
                session.add(food)
                session.commit()
                return True
        except:
            return False

    def update(self, olditem, newitem, username):
        try:
            with Session(self.engine) as session:
                food = session.query(ShoppingList).filter(
                    ShoppingList.foodList == olditem, ShoppingList.username == username).first()
                print(food, "here output")
                food.foodList = newitem
                session.commit()
                return True
        except:
            return False

    def delete(self, username, item):
        print("Delete")
        try:
            with Session(self.engine) as session:
                food = session.query(ShoppingList).filter(
                    ShoppingList.foodList == item, ShoppingList.username == username).first()
                print(food)
                session.delete(food)
                session.commit()
            return True
        except:
            return False
