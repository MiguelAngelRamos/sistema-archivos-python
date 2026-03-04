"""
Excepcion cuando tenemos una nota fuera de rango (0-100)
"""
class NotaInvalidaError(Exception):
    """Excepción personalizada para notas inválidas."""
    def __init__(self, nombre_alumno:str, nota: int):
        super().__init__(f"Nota inválida ({nota}) detectada para el alumno {nombre_alumno}")