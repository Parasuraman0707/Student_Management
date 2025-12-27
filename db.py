import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="srv1834.hstgr.io",
        user="u651328475_batch_11",
        password="Batch_11",
        database="u651328475_batch_11",
    )    

