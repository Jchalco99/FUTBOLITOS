import pymysql

class DAOPlayers:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="", db="futbolitos")

    def read(self, idEquipo):
        con = DAOPlayers.connect(self)
        cursor = con.cursor()

        try:
            if idEquipo == None:
                cursor.execute("SELECT * FROM jugadores ORDER BY id asc")
            else:
                cursor.execute("SELECT * FROM jugadores WHERE idEquipo = %s", (idEquipo,))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()
    
    def insert(self, data):
        con = DAOPlayers.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO equipo(apellido, nombre, posicion, nacionalidad, goles, asistencias, idEquipo) VALUES(%s, %s, %s, %s, %s, %s, %s)", (data['apellido'], data['nombre'], data['posicion'], data['nacionalidad'], data['goles'], data['asistencias'], data['idEquipo'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    
    def readUpdate(self, id):
        con = DAOPlayers.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM jugadores ORDER BY id asc")
            else:
                cursor.execute("SELECT * FROM jugadores WHERE id = %s", (id,))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()
    
    def update(self, id, data):
        con = DAOPlayers.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE jugadores SET apellido = %s, nombre = %s, posicion = %s, nacionalidad = %s, goles = %s, asistencias = %s, idEquipo = %s WHERE id = %s", (data['apellido'], data['nombre'], data['posicion'], data['nacionalidad'], data['goles'], data['asistencias'], data['idEquipo'], id))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self, id):
        con = DAOPlayers.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM jugadores WHERE id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()