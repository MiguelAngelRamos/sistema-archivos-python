"""
¿Para qué sirve este archivo?

Define el DOMINIO PURO de nuestra aplicación, es decir las entidades del mundo representados en código.

Principio (SRP) de los SOLID (Responsabilidad Única - Single Responsibility Principle)

  Esta clase SOLO sabe sobre estudiantes

     - Como se crean
     - Como se validan sus notas
     - Como se calculo su promedio

    Que NO hace esta clase ( Y NO DEBERIA HACER JAMAS!)
    - leer archivos .txt
    - Imprimir reportes en pantalla
    - Conectarse a una base de datos

    Ventaja práctica:
    - Si mañana hay un bug en el cálculo de promedio sabes exactamente donde ir: modelos.py Sin leer cientos y cientos de linea de código de otros archivos.
"""
from typing import List

from excepciones import NotaInvalidaError

class Estudiante:
    def __init__(self, nombre:str, notas:List[int]):
        self.nombre = nombre
        self.notas = notas
        # Llamamos al validador INMEDIATAMENTE
        self._validar_notas()

    def _validar_notas(self)-> None:
        ## AQUI voy a lanzar las excepciones personalizadas
        if len(self.notas) != 3:
            raise ValueError(f"El Alumno {self.nombre} no tiene exactamente 3 notas, tiene {len(self.notas)}")
        for nota in self.notas:
            if not (0 <= nota <= 100):
                raise NotaInvalidaError(self.nombre, nota)
    
    def calcular_promedio(self)-> float:
        return sum(self.notas) / len(self.notas)
