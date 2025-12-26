from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# import bcrypt
from add import Userd
from updateput import UpdatePut
from login import Login
from emailequal import Equal
from view import View
from delete import Delete
from create import Create
from update import Update


# hashed_pw = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())

class User(BaseModel):
    email: str
    password:int
class Entry(BaseModel):
    name: str
    course:str
    college:str
    number:int
    token:str
    email:str
class Entr(BaseModel):
    id: int
    name: str
    course:str
    college:str
    number:int
    token:str



class Email(BaseModel):
    email: str
    token:str

class EmailOnly(BaseModel):
    email: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers =["*"]
)
# @app.post("/")
# def root(data: User):
#     db = get_db()
#     query = "INSERT INTO mail (mail,password) VALUES (%s,%s)"
#     values=(data.email,data.password)
#     cursor = db.cursor()
#     cursor.execute(query,values)
#     db.commit()
#     cursor.close()
#     db.close()
#     return {"status": "success","message":values}

@app.post("/")
def login(data: User):
   datalogin=Login()
   return datalogin.login(data)

@app.post("/entry")
def entry(data: Entry):
    dataconnect=Userd()
    return dataconnect.add(data)
    # return data


@app.put("/update")
def details(data: User):
    updatedata=UpdatePut()
    return updatedata.update(data)

@app.post("/equal")
def equal(data: EmailOnly):
    dataequal=Equal()
    return dataequal.equal(data)

@app.post("/view")
def view(data : Email):
    dataview=View()
    return dataview.view(data)

@app.delete("/delete/{idd}")
def delete(idd):
    datadelete=Delete()
    return datadelete.delete(idd)

@app.post("/create")
def create(data: User):
    datacreate=Create()
    return datacreate.create(data)

@app.put("/update_input")
def update(data: Entr):
    dataupdate=Update()
    return dataupdate.update(data)


# class User():
#   def __init__(self):
#       self.db = get_db()
#   def red(self,data):
#       query = "INSERT INTO mail (email,password) VALUES (%s,%s)"
#       values=(data.email,data.password)
#       cursor = self.db.cursor()
#       cursor.execute(query,values)
#       self.db.commit()
#       cursor.close()
#       self.db.close()
#       return {"status": "success","message":values}
# @app.get("/")
# async def root(data:User):
#     return {"message": "Hello World", "data": data}
#
# @app.get("/user")
# def insertr():
#     db=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="mail"
#     )
#     query="insert into mail (mail,password) values (%s,%s)"
#     values=('parasu@gmail.com',522)
#     cursor=db.cursor()
#     cursor.execute(query,values)
#     db.commit()
#     cursor.close()
#     db.close()
#     return {"message":"success","get":values}
# async def root(data: User):
#     db = get_db()
#     cursor = db.cursor()
#     try:
#         hashed_pw = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())
#         query = "INSERT INTO mail (email, password) VALUES (%s, %s)"
#         values = (data.email, hashed_pw)
#         cursor.execute(query, values)
#         db.commit()
#         return {"status": "success", "message": "User inserted"}
#     except Exception as e:
#         db.rollback()
#         return {"status": "error", "message": str(e)}
#     finally:
#         cursor.close()
#         db.close()