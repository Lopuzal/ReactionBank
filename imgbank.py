import sqlite3
from pathlib import Path

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

class Imgbank:
    def __init__(self):
        conn = sqlite3.connect('database.db')
        with open('schema.sql') as f:
            conn.executescript(f.read())

        conn.commit()
        conn.close()


        conn.close()
    
    #Changes the path of a folder
    def change_folder_path(self,id_folder,new_path):
        conn = get_db_connection()
        conn.execute("UPDATE Folders SET folderPath = ? WHERE idFolder = ?", (new_path, id_folder))
        conn.commit()
        conn.close()
    

    #Takes a list of tags, returns a list of the corresponding image paths matching the tags
    def tags_list_to_image_paths_list(self,tags_list):
        conn = get_db_connection()
        conn.row_factory = lambda cursor, row: row[0] + "/" + row[1]
        return conn.execute("SELECT folderPath,filePath FROM Images JOIN Tags ON Images.id=idImage JOIN Folders ON idFolder = Folders.id WHERE tag IN ({0})".format(', '.join('?' for _ in tags_list)), tags_list).fetchall()

    #Takes a string of tags separated by a space, returns a list of tags
    def tags_str_to_tags_list(self,tags_str):
        pass
    
