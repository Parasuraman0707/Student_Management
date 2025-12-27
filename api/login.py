from api.JWTtoken import get_token
from api.db import get_db

class Login():
    def __init__(self):
        self.db = get_db()
    def login(self,data):
        query ="select * from pr_mail where mail=%s and password=%s"
        values = (data.email, data.password)
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        self.db.close()
        if len(result)==0:
            return {"status":"fail","message":"incorrect password or incorrect email"}
        else:
            # user = result[0]
            token = get_token(data.email)

            return {"status": "success", "message":"verification completed","token":token}

