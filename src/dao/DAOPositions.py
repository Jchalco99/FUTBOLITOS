import pymysql

class DAOPositions:
    def connect(self):
        return pymysql.connect(host="localhost", user="root", password="", db="futbolitos")
    
    def read(self, idEquipo):
        con = DAOPositions.connect(self)
        cursor = con.cursor()

        try:
            if idEquipo == None:
                cursor.execute("SELECT * FROM clasificacion ORDER BY puntos desc")
            else:
                cursor.execute("SELECT * FROM clasificacion WHERE idEquipo = %s ORDER BY puntos desc", (idEquipo,))
            return cursor.fetchall()
        except:
            return()
        finally:
            con.close()
    
    def update(self, idEquipo, data):
        con = DAOPositions.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE clasificacion SET posicion = %s, pjugados = %s, pganados = %s, pempatados = %s, pperdidos = %s, gfavor = %s, gcontra = %s, diferencia = %s, puntos = %s WHERE idEquipo = %s", (data['posicion'], data['pjugados'], data['pganados'], data['pempatados'], data['pperdidos'], data['gfavor'], data['gcontra'], data['diferencia'], data['puntos'], idEquipo))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()