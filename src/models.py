from flask_sqlalchemy import SQLAlchemy
#from random import randint

#db = SQLAlchemy()

class ArbolFamiliar:
    def __init__(self, apellido):
        self.apellido = apellido
        self.member = [
                        {
                        "id": 1,
                        "edad":90,
                        "apellido": self.apellido,
                        "nombre": "Juan",
                        "padres" : None,
                        "hijos" : [2,3,4]
                        },
                        {
                        "id": 2,
                        "edad":50,
                        "apellido": self.apellido,
                        "nombre": "Leonides",
                        "hijos" : None
                        },
                        {
                        "id": 3,
                        "edad":30,
                        "apellido": self.apellido,
                        "nombre": "Maria",
                        "hijos" : None
                        },
                        {
                        "id": 4,
                        "edad":30,
                        "apellido": self.apellido,
                        "nombre": "Pedro",
                        "hijos" : [5]
                        },
                        {
                        "id": 5,
                        "edad":15,
                        "apellido": self.apellido,
                        "nombre": "Pedro",
                        "hijos" : [6,7]
                        },
                        {
                        "id": 6,
                        "edad":2,
                        "apellido": self.apellido,
                        "nombre": "Nicola",
                        "hijos" : None
                        },
                        {
                        "id": 7,
                        "edad":2,
                        "apellido": self.apellido,
                        "nombre": "Valeria",
                        "hijos" : None
                        }
                        ]

def idMember(self,id):
    for i in self.member:
        if i["id"] == int(id):
            return i
    return None