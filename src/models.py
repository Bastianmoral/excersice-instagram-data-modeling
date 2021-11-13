import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
#ForeignKey('Follower.User_from_id'), ForeignKey('Follower.User_to_id'), ForeignKey('Comment.Id'), ForeignKey('Post.Id'),
#POR BUENA PRACTICA PONER LOS NOMBRES DE LAS TABLAS EN PLURAL Y en minusculas  su contenido
class Users(Base):
    __tablename__ = "Users"
    Id = Column(Integer, primary_key=True)
    Username = Column(String(250))
    First_name = Column(String(250))
    Last_name = Column(String(250))
    follower = Column(Integer, ForeignKey('Follower.User_form_id'))

class Followers(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    User_from_id = Column(Integer, primary_key=True,)
    User_to_id = Column(Integer, ForeignKey('Users.Id'))

class Posts(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.Id'), nullable= False)

class Comments(Base):
    __tablename__ = "Comment"
    Id = Column(Integer, primary_key=True)
    Comment_text = Column(String(500))
    Author_id = Column(Integer)
    Post_id = Column(Integer)

class Medias(Base):
    __tablename__= 'Media'
    Id = Column(Integer, primary_key=True)
    Type = Column(Enum)
    Url = Column(String(250))
    Post_id = Column(Integer)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e