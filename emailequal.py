import JWTtoken
from db import get_db
from JWTtoken import verify_token
#
#
# class Equal():
#     def __init__(self):
#         self.db = get_db()
#     def equal(self,data):
#         # return data
#         # get_token=data.email
#         # token2=JWTtoken.get_token(get_token)
#         # return {"token":token2, 'status' : "success"}
#         # return get_token
#         query="select * from mail where mail=%s"
#         values=(data.email)
#         cursor=self.db.cursor(dictionary=True)
#         # return '13'
#         cursor.execute(query,values)
#         results=cursor.fetchall()
#         cursor.close()
#         self.db.close()
#         if len(results)==0:
#             return {"status":"fail","message":"incorrect password and incorrect email"}
#         else:
#             jwt = JWTtoken.get_token(data.email)
#             return {"status":"success","data":"results", "token" : jwt}

class Equal():
    def __init__(self):
        self.db = get_db()
    def equal(self,data):
        query ="select * from mail where mail=%s"
        values = [data.email]
        cursor = self.db.cursor(dictionary=True)
        cursor.execute(query, values)
        result = cursor.fetchall()
        cursor.close()
        self.db.close()
        # return "success"
        if len(result)==0:
            return {"status":"fail","message":"incorrect password or incorrect email"}
        else:
            # return {"status":"success"}
            # user = result[0]
            # token = get_token(data.email)
            jwt = JWTtoken.get_token(data.email)
            return {"status": "success", "message":"verification completed","token":jwt}
