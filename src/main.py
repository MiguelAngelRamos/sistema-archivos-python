"""
¿Para que sirve este archivo?

Es el PUNTO DE ENTRADA de la aplicación

Regla de oro: 
    main.py debe ser tan simple que cualquiera lo entienda en 10 segundos. 
    Toda complejidad vive en otros módulos
"""
from pathlib import Path
from procesador import ProcesadorCalificaciones

def main():
    BASE = Path(__file__).parent.parent # BASE es la ruta absoluta del archivo main.py
    RUTA_ENTRADA = BASE/'data'/'input'/'calificaciones.txt'
    RUTA_SALIDA = BASE/'data'/'output'/'reporte_final.txt'

    # ejercicio/data/output es lo que hace RUTA_SALIDA.parent
    RUTA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
    print("Iniciando procesamiento de calificaciones...")
    sistema = ProcesadorCalificaciones(RUTA_ENTRADA, RUTA_SALIDA)
    sistema.procesar()
if __name__ == "__main__":
    main()

# C:\Users\Miguel\Desktop\ejercicio\src\main.py -> es la ruta absoluta del archivo main.py
# C:\Users\Miguel\Desktop\ejercicio