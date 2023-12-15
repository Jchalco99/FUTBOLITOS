import pymysql

class DAOTeams:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="", db="futbolitos")
    
    def read(self, id):
        con = DAOTeams.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM equipo ORDER BY id asc")
            else:
                cursor.execute("SELECT * FROM equipo WHERE id = %s ORDER BY id asc", id)
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()
    
    def insert(self, data):
        con = DAOTeams.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO equipo VALUES(%s, %s, %s, %s)", (data['id'], data['nombre'], data['estadio'], data['foto']))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def update(self, id, data):
        con = DAOTeams.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE equipo set id = %s, nombre = %s, idEstudio = %s", (data['id'], data['nombre'], data['estadio'], data['foto'], id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOTeams.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM equipo where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()