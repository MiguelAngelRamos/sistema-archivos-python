💻 Laboratorio Práctico: El Procesador de Datos Resiliente

**Contexto del Proyecto:**
Ustedes acaban de ser contratados como desarrolladores Backend para una academia. El sistema anterior exportaba las calificaciones de los alumnos en un archivo de texto plano (`calificaciones.txt`), pero el sistema tenía fallos y los datos a menudo vienen corruptos (letras en lugar de números, notas que no existen, etc.).

Su misión es construir un programa orientado a objetos que lea este archivo, calcule el promedio de cada alumno, maneje los errores elegantemente (sin que el programa se caiga) y genere un nuevo archivo llamado `reporte_final.txt` con los alumnos aprobados y un registro de los errores encontrados.

### 📄 Archivo de Entrada Simulado (`calificaciones.txt`)

Creen un archivo en su proyecto con exactamente este texto. Observen que tiene errores intencionales:

```text
Sofia Araya,85,90,78
Ana Torres,100,A,95
Luis Perez,105,80,90
Maria Gomez,60,70

```

*(Nota para el alumno: "Ana" tiene una letra en lugar de un número, "Luis" tiene una nota mayor a 100, y "Maria" tiene solo dos notas en lugar de tres).*

---

### 🎯 Requerimientos del Sistema

Deberán aplicar **Clean Code**, **POO**, **Gestión de Archivos** y **Manejo de Excepciones**.

**1. Dominio (POO):**

* Crea una clase `Estudiante` que tenga como atributos su `nombre` y una lista de `notas`.
* La clase debe tener un método `calcular_promedio()` que retorne el promedio de sus notas.

**2. Excepciones Personalizadas:**

* Crea una excepción llamada `NotaInvalidaError` (heredando de `Exception`). Esta debe lanzarse si al procesar las notas, alguna es menor a 0 o mayor a 100.

**3. Procesamiento y Manejo de Errores (El Core):**

* Crea una clase `ProcesadorCalificaciones`.
* Debe tener un método que lea el archivo usando el Context Manager (`with open`).
* Por cada línea leída, el sistema debe intentar instanciar un `Estudiante` y calcular su promedio.
* **Gestión de Errores Requerida:**
* Si el archivo no existe, captura el `FileNotFoundError` e imprime: *"Error crítico: El archivo de origen no fue encontrado."*
* Si al convertir la nota a entero falla (ej. la "A" de Ana), captura el `ValueError` y registra el error, pero **continúa con el siguiente alumno**.
* Si una nota es irreal (ej. el "105" de Luis), captura tu `NotaInvalidaError`, registra el error, y **continúa con el siguiente alumno**.
* Si el alumno no tiene exactamente 3 notas (ej. Maria), lanza y captura una excepción adecuada o manéjalo con lógica, indicando *"Faltan datos para evaluar"*.



**4. Persistencia de Salida:**

* Genera un archivo `reporte_final.txt` en modo escritura (`'w'`).
* Escribe en él solo a los estudiantes que fueron procesados exitosamente y cuyo promedio sea igual o mayor a 70.
