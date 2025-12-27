from db import get_db
from JWTtoken import verify_token


class Delete():
    def __init__(self):
        # verify_token()
        self.db = get_db()
    def delete(self,data):

        query = "delete from  pr_details where id=%s"
        value = (data,)
        cursor = self.db.cursor()
        cursor.execute(query,value)
        # result = cursor.fetchall()
        self.db.commit()
        cursor.close()
        self.db.close()
        return {"status":"success","message":value}





