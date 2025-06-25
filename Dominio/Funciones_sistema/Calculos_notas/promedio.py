from Dominio.Materias.nota import Nota

class Promedio():
    def promediar(self, notas: list[Nota]) -> float:
        cant_notas: int = len(notas)
        if cant_notas == 0:
            return 0
        
        suma_notas: float = 0
        for nota in notas:
            suma_notas += nota.get_valor_nota()
        return suma_notas / cant_notas
