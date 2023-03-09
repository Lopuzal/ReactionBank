import sqlite3
from pathlib import Path


class Imgbank:
    def __init__(self,db_path="database.db"):
        self._db_path = db_path

    def get_db_connection(self):
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        conn = self.get_db_connection()
        with open('schema.sql') as f:
            conn.executescript(f.read())

        conn.commit()
        conn.close()

    #Takes a list of tags, returns a list of the corresponding image paths matching the tags
    def tags_list_to_image_paths_list(self,tags_list):
        conn = self.get_db_connection()
        conn.row_factory = lambda cursor, row: row[0]
        return conn.execute("SELECT filePath FROM Images JOIN Tags ON Images.id=idImage WHERE tag IN ({0})".format(', '.join('?' for _ in tags_list)), tags_list).fetchall()

    #Takes a string of tags separated by a space, returns a list of tags
    def tags_str_to_tags_list(self,tags_str):
        return tags_str.split(" ")
    
    def add_entry(self,img_path,tags):
        conn = self.get_db_connection()

        #Insert image
        conn.execute("INSERT INTO Images (filePath) VALUES (?)", (img_path,))
        idimg = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
        
        #Insert tags
        for tag in tags:
            conn.execute("INSERT INTO Tags VALUES (?,?)", (tag,idimg))

        conn.commit()
        conn.close()

    def delete_entry(self,id_img):
        conn = self.get_db_connection()
        conn.execute("DELETE FROM Tags WHERE idImage = ?",(id_img,))
        conn.execute("DELETE FROM Images WHERE id = ?",(id_img,))
        conn.commit()
        conn.close()
