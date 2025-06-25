import sqlite3
import os
from Dominio.Materias.final import Final
from Dominio.Materias.parcial import Parcial
from Dominio.Materias.materia import Materia

class Facade_Persistencia():
    def __init__(self):
        self
        self.cursor = None
        self.conn = None

    def conectar(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_folder = os.path.join(BASE_DIR, 'Plantilla')
        os.makedirs(db_folder, exist_ok=True)  # Asegura que la carpeta exista

        db_path = os.path.join(db_folder, 'plantilla.db')
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def desconectar(self):
        self.conn.close()

    def existe_tabla(self, nombre_tabla):
        self.cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name=?;
        """, (nombre_tabla,))
    
        return self.cursor.fetchone() is not None

    def crear_tabla_materia(self):
        if not self.existe_tabla("Materia"):
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
                ''' #es_promocionable es BOOLEAN
            )
            self.conn.commit()
    
    def crear_tabla_parcial(self):
        if not self.existe_tabla("Parcial"):
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
    
    def crear_tabla_final(self):
        if not self.existe_tabla("Final"):
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
        self.crear_tabla_materia()
        self.crear_tabla_parcial()
        self.crear_tabla_final()

    def eliminar_base(self):
        for tabla in ["Materia", "Parcial", "Final"]:
            self.cursor.execute(f"DELETE FROM {tabla}")
            self.conn.commit()

    def obtener_materias(self):
        self.cursor.execute("SELECT * FROM Materia")
        tuplas_materias = self.cursor.fetchall()
        
        materias = []
        for tupla in tuplas_materias:
            materia = Materia(tupla)
            materias.append(materia)
        return materias
    
    def agregar_materia(self, materia):
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

    def eliminar_materia(self, ID):
        self.cursor.execute("DELETE FROM Materia WHERE id_materia = ?", (ID,))
        self.conn.commit()
        self.eliminar_parciales(ID)
        self.eliminar_finales(ID)

    def modificar_materia(self, ID, campo, valor):
        print(type(campo), campo, type(valor), valor, type(ID), ID)
        self.cursor.execute(f"UPDATE Materia SET {campo} = ? WHERE id_materia = ?", (valor, ID))
        self.conn.commit()
    
    def obtener_parciales(self, materia):
        self.cursor.execute("SELECT * FROM Parcial WHERE id_materia = ?", (materia.get_id_materia(),))
        tuplas_parciales = self.cursor.fetchall()  # Lista de tuplas
        
        parciales = []
        for tupla in tuplas_parciales:
            parcial = Parcial(tupla)
            parciales.append(parcial)
        return parciales
    
    def agregar_parcial(self, parcial):
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

    def eliminar_parciales(self, ID):
        self.cursor.execute("DELETE FROM Parcial WHERE id_materia = ?", (ID,))
        self.conn.commit()

    def modificar_parcial(self, ID, campo, valor):
        self.cursor.execute(f"UPDATE Parcial SET {campo} = ? WHERE id_nota = ?", (valor, ID))
        self.conn.commit()

    def obtener_finales(self, materia):
        self.cursor.execute("SELECT * FROM Final WHERE id_materia = ?", (materia.get_id_materia(),))
        tuplas_finales = self.cursor.fetchall()  # Lista de tuplas
        
        finales = []
        for tupla in tuplas_finales:
            final = Final(tupla)
            finales.append(final)
        return finales
    
    def agregar_final(self, final):
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

    def eliminar_finales(self, ID):
        self.cursor.execute("DELETE FROM Final WHERE id_materia = ?", (ID,))
        self.conn.commit()

    def modificar_final(self, ID, campo, valor):
        self.cursor.execute(f"UPDATE Final SET {campo} = ? WHERE id_nota = ?", (valor, ID))
        self.conn.commit()

    def agregar_recuperatorio(self, ID, valor):
        self.cursor.execute("UPDATE Parcial SET valor_recuperatorio = ? WHERE id_nota = ?", (valor, ID))
        self.conn.commit()

    def eliminar_recuperatorio(self, ID):
        self.cursor.execute("UPDATE Parcial SET valor_recuperatorio = NULL WHERE id_nota = ?", (ID,))
        self.conn.commit()

    def mover_notas(self, id_materia_vieja, id_materia_nueva):
        self.cursor.execute(f"UPDATE Parcial SET id_materia = ? WHERE id_materia = ?", (id_materia_nueva, id_materia_vieja))
        self.cursor.execute(f"UPDATE Final SET id_materia = ? WHERE id_materia = ?", (id_materia_nueva, id_materia_vieja))
        self.conn.commit()