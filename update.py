from db import get_db

class Update:
    def __init__(self):
        self.db = get_db()
    def update(self,data):
        query="update  pr_details set name=%s,course=%s,college=%s,number=%s where id=%s "
        values=(data.name,data.course,data.college,data.number,data.id)
        cursor = self.db.cursor()
        cursor.execute(query,values)
        self.db.commit()
        cursor.close()
        self.db.close()

        return {"status": "success","Message":values}
