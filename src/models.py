import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50))
    email = Column(String(100), nullable=False)

class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    descripcion = Column(String(250), nullable=False)
    imagen = Column(String(250), nullable=False)
    usuario = relationship(Usuario)

class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_publicacion = Column(Integer, ForeignKey('publicacion.id'))
    usuario = relationship(Usuario)
    publicacion = relationship(Publicacion)

class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_publicacion = Column(Integer, ForeignKey('publicacion.id'))
    comentatio = Column(String(250), nullable=False)
    usuario = relationship(Usuario)
    publicacion = relationship(Publicacion)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
