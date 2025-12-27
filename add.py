# from dns.e164 import query

from JWTtoken import verify_token
from db import get_db
# from main import Entry

class Userd():
    def __init__(self):
        self.db = get_db()
    def add(self, data):
        ok=data.token
        yes=verify_token(ok)

        if data.email==yes['email']:
            query = "insert into details (name,course,college,number) values(%s,%s,%s,%s)"
            values =(data.name,data.course,data.college,data.number)
            cursor = self.db.cursor()
            cursor.execute(query,values)
            self.db.commit()
            self.db.close()
            cursor.close()
            return {"status":"success","message":values}
        else:
            return {"status":"error","message":"Invalid Token", 'yes' : yes}
    # def add(self, data: Entry):
    #     ok = data.token
    #     yes = verify_token(ok)
    #
    #     print("DECODED TOKEN =", yes)
    #
    #     # Validate token result
    #     if not yes or "email" not in yes:
    #         return {"status": "error", "Message": "Invalid token"}
    #
    #     # Match token email with user email
    #     if data.email != yes["email"]:
    #         return {"status": "error", "Message": "Email does not match token"}
    #
    #     # Insert into DB
    #     query = "INSERT INTO details (name, course, college, number) VALUES (%s, %s, %s, %s)"
    #     values = (data.name, data.course, data.college, data.number)
    #
    #     cursor = self.db.cursor()
    #     cursor.execute(query, values)
    #     self.db.commit()
    #     cursor.close()
    #
    #     return {"status": "success", "Message": values}




