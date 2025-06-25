import sqlite3
import os
from Dominio.Materias.final import Final
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.materia import Materia

class Facade_Persistencia():
    def __conectar(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_folder = os.path.join(BASE_DIR, 'Repositorio')
        os.makedirs(db_folder, exist_ok=True)  # Asegura que la carpeta exista

        db_path = os.path.join(db_folder, 'repo.db')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def __desconectar(self):
        self.conn.close()

    def __existe_tabla(self, nombre_tabla):
        self.cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name=?;
        """, (nombre_tabla,))

        return self.cursor.fetchone() is not None

    def __crear_tabla_materia(self):
        if not self.__existe_tabla("Materia"):
            self.cursor.execute('''
                CREATE TABLE Materia (
                    id_materia INTEGER PRIMARY KEY,
                    nombre_materia TEXT NOT NULL,
                    nombre_docente TEXT NOT NULL,
                    nota_min_aprobar REAL NOT NULL,
                    es_promocionable BOOLEAN NOT NULL,
                    nota_min_promocion REAL,
                    cant_veces_final_rendible INTEGER NOT NULL,
                    cant_parciales INTEGER NOT NULL
                )
                '''
            )
            self.conn.commit()
    
    def __crear_tabla_parcial(self):
        if not self.__existe_tabla("Parcial"):
            self.cursor.execute('''
                CREATE TABLE Parcial (
                    id_nota INTEGER PRIMARY KEY,
                    id_materia INTEGER NOT NULL,
                    valor_nota REAL NOT NULL,
                    valor_recuperatorio REAL
                )
                '''
            )
            self.conn.commit()
    
    def __crear_tabla_final(self):
        if not self.__existe_tabla("Final"):
            self.cursor.execute('''
                CREATE TABLE Final (
                    id_nota INTEGER PRIMARY KEY,
                    id_materia INTEGER NOT NULL,
                    valor_nota REAL NOT NULL
                )
                '''
            )
            self.conn.commit()

    def crear_base(self):
        self.__conectar()
        self.__crear_tabla_materia()
        self.__crear_tabla_parcial()
        self.__crear_tabla_final()
        self.__desconectar()

    def eliminar_base(self):
        self.__conectar()
        for tabla in ["Materia", "Parcial", "Final"]:
            self.cursor.execute(f"DELETE FROM {tabla}")
            self.conn.commit()
        self.__desconectar()

    def obtener_materia(self, id):
        self.__conectar()
        self.cursor.execute("SELECT * FROM Materia WHERE id_materia = ?", (id,))
        tupla_materia = self.cursor.fetchone()
        self.__desconectar()
        
        datos = {
            "id_materia": tupla_materia[0],
            "nombre_materia": tupla_materia[1],
            "nombre_docente": tupla_materia[2],
            "nota_min_aprobar": tupla_materia[3],
            "es_promocionable": tupla_materia[4],
            "nota_min_promocion": tupla_materia[5],
            "cant_veces_final_rendible": tupla_materia[6],
            "cant_parciales": tupla_materia[7]
        }

        materia = Materia(datos)
        
        return materia
    
    def obtener_materias(self):
        self.__conectar()
        self.cursor.execute("SELECT * FROM Materia")
        tuplas_materias = self.cursor.fetchall()
        self.__desconectar()
        
        materias = []
        for tupla_materia in tuplas_materias:
            datos = {
                "id_materia": tupla_materia[0],
                "nombre_materia": tupla_materia[1],
                "nombre_docente": tupla_materia[2],
                "nota_min_aprobar": tupla_materia[3],
                "es_promocionable": tupla_materia[4],
                "nota_min_promocion": tupla_materia[5],
                "cant_veces_final_rendible": tupla_materia[6],
                "cant_parciales": tupla_materia[7]
            }
            materia = Materia(datos)
            materias.append(materia)
        return materias
    
    def agregar_materia(self, materia):
        self.__conectar()
        self.cursor.execute('''INSERT INTO Materia (
                id_materia,
                nombre_materia,
                nombre_docente,
                nota_min_aprobar,
                es_promocionable,
                nota_min_promocion,
                cant_veces_final_rendible,
                cant_parciales
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?) ''',
            (materia.get_id_materia(), 
                materia.get_nombre_materia(),
                materia.get_nombre_docente(),
                materia.get_nota_min_aprobar(),
                materia.get_es_promocionable(),
                materia.get_nota_min_promocion(),
                materia.get_cant_veces_final_rendible(),
                materia.get_cant_parciales())
            )

        self.conn.commit()
        self.__desconectar()

    def eliminar_materia(self, ID):
        self.__conectar()
        self.cursor.execute("DELETE FROM Materia WHERE id_materia = ?", (ID,))
        self.conn.commit()
        self.eliminar_parciales(ID)
        self.eliminar_finales(ID)
        self.__desconectar()

    def modificar_materia(self, ID, campo, valor):
        self.__conectar()
        print(type(campo), campo, type(valor), valor, type(ID), ID)
        self.cursor.execute(f"UPDATE Materia SET {campo} = ? WHERE id_materia = ?", (valor, ID))
        self.conn.commit()
        self.__desconectar()
    
    def obtener_parcial(self, id):
        self.__conectar()
        self.cursor.execute("SELECT * FROM Parcial WHERE id_nota = ?", (id,))
        tupla_parcial = self.cursor.fetchone()  # Tupla
        self.__desconectar()
        
        datos = {
            "id_nota": tupla_parcial[0],
            "id_materia": tupla_parcial[1],
            "valor_nota": tupla_parcial[2],
            "valor_recuperatorio": tupla_parcial[3]
        }
        parcial = Parcial(datos)
            
        return parcial
    
    def obtener_parciales(self, materia):
        self.__conectar()
        self.cursor.execute("SELECT * FROM Parcial WHERE id_materia = ?", (materia.get_id_materia(),))
        tuplas_parciales = self.cursor.fetchall()  # Lista de tuplas
        self.__desconectar()
        
        parciales = []
        for tupla_parcial in tuplas_parciales:
            datos = {
                "id_nota": tupla_parcial[0],
                "id_materia": tupla_parcial[1],
                "valor_nota": tupla_parcial[2],
                "valor_recuperatorio": tupla_parcial[3]
            }
            parcial = Parcial(datos)
            parciales.append(parcial)
        return parciales
    
    def agregar_parcial(self, parcial):
        self.__conectar()
        self.cursor.execute('''INSERT INTO Parcial (
                id_nota,
                id_materia,
                valor_nota
            ) VALUES (NULL, ?, ?) ''',
            (
                parcial.get_id_materia(),
                parcial.get_valor_nota())
            )

        self.conn.commit()
        self.__desconectar()

    def eliminar_parciales(self, ID):
        self.__conectar()
        self.cursor.execute("DELETE FROM Parcial WHERE id_materia = ?", (ID,))
        self.conn.commit()
        self.__desconectar()

    def modificar_parcial(self, ID, campo, valor):
        self.__conectar()
        self.cursor.execute(f"UPDATE Parcial SET {campo} = ? WHERE id_nota = ?", (valor, ID))
        self.conn.commit()
        self.__desconectar()

    def obtener_final(self, id):
        self.__conectar()
        self.cursor.execute("SELECT * FROM Final WHERE id_nota = ?", (id,))
        tupla_final = self.cursor.fetchone()  # Tupla
        self.__desconectar()
        
        datos = {
            "id_nota": tupla_final[0],
            "id_materia": tupla_final[1],
            "valor_nota": tupla_final[2]
        }
        final = Final(datos)
            
        return final

    def obtener_finales(self, materia):
        self.__conectar()
        self.cursor.execute("SELECT * FROM Final WHERE id_materia = ?", (materia.get_id_materia(),))
        tuplas_finales = self.cursor.fetchall()  # Lista de tuplas
        self.__desconectar()
        
        finales = []
        for tupla_final in tuplas_finales:
            datos = {
                "id_nota": tupla_final[0],
                "id_materia": tupla_final[1],
                "valor_nota": tupla_final[2]
            }
            final = Final(datos)
            finales.append(final)
        return finales
    
    def agregar_final(self, final):
        self.__conectar()
        self.cursor.execute('''INSERT INTO Final (
                id_nota,
                id_materia,
                valor_nota
            ) VALUES (NULL, ?, ?) ''',
            ( 
                final.get_id_materia(),
                final.get_valor_nota())
            )

        self.conn.commit()
        self.__desconectar()

    def eliminar_finales(self, ID):
        self.__conectar()
        self.cursor.execute("DELETE FROM Final WHERE id_materia = ?", (ID,))
        self.conn.commit()
        self.__desconectar()

    def modificar_final(self, ID, campo, valor):
        self.__conectar()
        self.cursor.execute(f"UPDATE Final SET {campo} = ? WHERE id_nota = ?", (valor, ID))
        self.conn.commit()
        self.__desconectar()

    def agregar_recuperatorio(self, id_materia, id_nota, valor):
        self.__conectar()
        self.cursor.execute("UPDATE Parcial SET valor_recuperatorio = ? WHERE id_materia = ? AND id_nota = ?", (valor, id_materia, id_nota))
        self.conn.commit()
        self.__desconectar()

    def eliminar_recuperatorio(self, ID):
        self.__conectar()
        self.cursor.execute("UPDATE Parcial SET valor_recuperatorio = NULL WHERE id_nota = ?", (ID,))
        self.conn.commit()
        self.__desconectar()

    def mover_notas(self, id_materia_vieja, id_materia_nueva):
        self.__conectar()
        self.cursor.execute(f"UPDATE Parcial SET id_materia = ? WHERE id_materia = ?", (id_materia_nueva, id_materia_vieja))
        self.cursor.execute(f"UPDATE Final SET id_materia = ? WHERE id_materia = ?", (id_materia_nueva, id_materia_vieja))
        self.conn.commit()
        self.__desconectar()