from db import get_db
from JWTtoken import verify_token

class UpdatePut():
    def __init__(self):
        self.db = get_db()
    def update(self,data):
        # get_token=data.email
        # token2=JWTtoken.get_token(get_token)
        # return {"token":token2, 'status' : "success"}
        # # return "pass"
        query = "UPDATE pr_mail SET password=%s WHERE mail = %s"
        values = (data.password,data.email)
        cursor = self.db.cursor()
        cursor.execute(query,values)
        self.db.commit()
        cursor.close()
        self.db.close()
        return {"status": "success","Message":values}


