from Manejo_consola.interfaces.input import Interfaz_Input
from Manejo_consola.interfaces.output import Interfaz_Output
from Dominio.Funciones_sistema.Logica_negocio.enum_estado import Estado
from Dominio.Materias.materia import Materia

class CLI(Interfaz_Input, Interfaz_Output):
    def __init__(self):
        super().__init__()

    def obtener_entero(self, entero_a_obtener):
        while True:
            ingreso = input(f'Ingrese {entero_a_obtener}: ')
            try:
                ingreso = int(ingreso)
                return ingreso
            except Exception:
                self.mostrar_advertencia("no_entero")
    
    def obtener_decimal(self, decimal_a_obtener):
        while True:
            ingreso = input(f'Ingrese {decimal_a_obtener}: ')
            try:
                ingreso = float(ingreso)
                return ingreso
            except Exception:
                self.mostrar_advertencia("no_decimal")

    def obtener_cadena(self, cadena_a_obtener):
        ingreso = input(f'Ingrese {cadena_a_obtener}: ')
        return ingreso

    def obtener_booleano(self, booleano_a_obtener):
        while True:
            ingreso = input(f'{booleano_a_obtener} (S/N): ').upper()
            if ingreso == "S":
                return True
            elif ingreso == "N":
                return False
            else:
                self.mostrar_advertencia("no_booleano")
    
    def seleccionar_opcion(self, opciones_disponibles):
        print("\t-- Opciones disponibles --")
        for opcion in opciones_disponibles:
            print(f"\t{opcion} => {opciones_disponibles[opcion][1]}")
        while True:
            opcion_elegida = input("Ingrese Opción: ").upper()
            if opcion_elegida in opciones_disponibles:
                return opciones_disponibles[opcion_elegida]
            else:
                self.mostrar_advertencia("opcion_invalida")
    
    def mostrar_advertencia(self, id_advertencia):
        print(self.ADVERTENCIAS[id_advertencia])
    
    def mostrar_tabla(self, materias: list[Materia], service):
        print("-------------------------------------------------")
        if len(materias) > 0:
            print(
                "ID",
                "Estado\t",
                "Materia",
                sep="\t"
            )

            for materia in materias:
                estado = service.determinar_resultados(materia)["estado"]

                print(
                    materia.get_id_materia(),
                    estado.name,
                    materia.get_nombre_materia(),
                    sep="\t"
                )
        else:
            print("No hay materias registradas.")
        print("-------------------------------------------------")
    
    def mostrar_notas(self, notas, recu=False, id=False):
        print(
            "ID" if id else "",
            "Nota",
            "Recuperatorio" if recu else "",
            sep="\t"
        )

        for nota in notas:
            print(
                nota.get_id_nota() if id else "",
                nota.get_valor_nota(),
                nota.get_valor_recuperatorio() if recu and nota.get_valor_recuperatorio() else "",
                sep="\t"
            )

    def mostrar_info_materia(self, materia_seleccionada: Materia, service):
        print("-------------------------------------------------")

        print(f"ID: {materia_seleccionada.get_id_materia()}")

        print(f"Materia: {materia_seleccionada.get_nombre_materia()}")

        print(f"Docente: {materia_seleccionada.get_nombre_docente()}")

        print(f"Nota minima para Aprobar: {materia_seleccionada.get_nota_min_aprobar()}")

        print(f"¿Es promocionable?: {"Sí" if materia_seleccionada.get_es_promocionable() else "No"}")
        
        if materia_seleccionada.get_es_promocionable():
            print(f"Nota minima para Promocionar: {materia_seleccionada.get_nota_min_promocion()}")

        print(f"Cantidad de oportunidades de final: {materia_seleccionada.get_cant_veces_final_rendible()}")

        print(f"Cantidad de Parciales: {materia_seleccionada.get_cant_parciales()}")

        parciales = service.obtener_parciales(materia_seleccionada.get_id_materia())

        if len(parciales) > 0:
            print("\t-- PARCIALES --")
            self.mostrar_notas(parciales, recu=True)
        else:
            print("No hay parciales registrados de esta materia.")

        finales = service.obtener_finales(materia_seleccionada.get_id_materia())

        if len(finales) > 0:
            print("\t-- FINALES --")
            self.mostrar_notas(finales)
        else:
            print("No hay finales registrados de esta materia.")

        print("----------")

        resultados = service.determinar_resultados(materia_seleccionada)

        print(f"ESTADO: {resultados["estado"].name}")

        if resultados["estado"] == Estado.REGULARIZADO:
            print(f"Oportunidades de final restantes: {resultados["intentos_final_restantes"]}")
        elif resultados["estado"] == Estado.APROBADO or resultados["estado"] == Estado.PROMOCIONADO:
            print(f"Nota final de la materia: {resultados["nota_final"]}")
        
        print("-------------------------------------------------")