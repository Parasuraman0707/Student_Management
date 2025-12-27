from db import get_db

class Create:
    def __init__(self):
        self.db = get_db()
    def create(self,data):
        query="insert into  pr_mail (mail,password) values (%s,%s)"
        values=(data.email,data.password)
        cursor=self.db.cursor()
        cursor.execute(query,values)
        self.db.commit()
        cursor.close()
        self.db.close()
        return {"status":"created","message":values}

