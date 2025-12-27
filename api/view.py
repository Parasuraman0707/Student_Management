from api.db import get_db
from JWTtoken import verify_token

class View():
    def __init__(self):
        self.db = get_db()
    def view(self,data):
        ok = data.token
        yes1 = verify_token(ok)

        if data.email == yes1['email']:
            query="select * from pr_details"
            cursor = self.db.cursor(dictionary=True)
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            self.db.close()
            return {"status": "success","Message":results}
        else:
            return {"status": "error","Message":"Invalid token","yes": yes1}



