"""
¿Para qué sirve este archivo?

 Contiene las clase ProcesadorCalificaciones, es el "motor" del sistema, Es la que se "Ensucia las manos" con el disco duro: abrir los archivos, lee lineas, manejar errores y escribir reportes.

 Principio SOLID -> SRP (Responsabilidad Única - Single Responsibility Principle)

    Cuales son las responsabilidades de esta clase?
    - ProcesadorCalficaciones -> sabe sobre archivos e I/O (Input/Output)
    - Estudiante              -> sabe sobre notas y promedios
"""
from pathlib import Path
from modelos import Estudiante
from typing import List, Optional
from excepciones import NotaInvalidaError

class ProcesadorCalificaciones:
    def __init__(self, ruta_entrada: Path, ruta_salida: Path):
        """ Parámetros:
            ruta_entrada: Ruta al archivo de calificaciones
            ruta_salida: Ruta para el reporte de salida
        """
        self.ruta_entrada = ruta_entrada
        self.ruta_salida = ruta_salida
        self.errores_log: List[str] = []  # Lista para almacenar errores encontrados durante el procesamiento

    def procesar(self) -> None:
        """
        Método Principal: Ejecuta el flujo completo de procesamiento:

        Maneja:
            FileNotFoundError: Si el archivo de entrada no existe
            PermissionError: Si el Sistema Operativo (SO) Bloquea el acceso al archivo
        """
        # Lista donde acumularemos los estudiantes tuplas (nombre, promedio)
        # Una tupla es una pareja de valores inmuetable : ("Sofia", 85.5)
        # Empieza vacia por que se va ir llenando con los alumnos que aprueban
        estudiantes_aprobados: List[tuple] = []

        try:
            with open(self.ruta_entrada, 'r', encoding='utf-8') as archivo_in:
                for num_linea, linea in enumerate(archivo_in, start=1):
                    estudiante = self._procesar_linea(linea.strip(), num_linea)

        except FileNotFoundError:
            print(f"Error critico: El archivo '{self.ruta_entrada}' no existe", f"Terminando proceso.")

    
    # Optional[Estudiante] el valor puede ser una instancia de Estudiante o None
    def _procesar_linea(self, linea: str, num_linea: int) -> Optional[Estudiante]:
        """
        Parámetros: 
            linea (str): Texto de una linea
                         Ejemplo: "Sofia Araya,85,90,78"

            num_linea (int): Número de linea del archivo.
        """
        # "not linea" es True cuando la linea es "" (string vacio)
        if not linea:
            return None
        
        partes = linea.split(',')
        nombre = partes[0].strip() # con esto obtengo el nombre del alumno

        try:
           notas = [int(nota) for nota in partes[1:]] # con esto obtengo las notas del alumno
           return Estudiante(nombre, notas)
        except ValueError as e:
            mensaje = (f"Linea {num_linea} [{nombre}]: {e}")
            self.errores_log.append(mensaje)
            return None
        except NotaInvalidaError as e:
            mensaje = (f"Linea {num_linea} [{nombre}]: {e}")
            self.errores_log.append(mensaje)
            return None
