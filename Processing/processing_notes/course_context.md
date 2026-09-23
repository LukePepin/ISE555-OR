# Contexto de la asignatura — ISE 555

Actualizado en la iteración 004 mediante lectura visual por IA del syllabus local.
Fuentes: `raw/syllabus/IMG_7842.jpeg` y `IMG_7843.jpeg`; extracción en
`work/syllabus/material_review.md`. Pendiente de revisión humana; no se consultó el libro.

- Asignatura: ISE 555 — Advanced Deterministic Systems Optimization.
- Institución: University of Rhode Island. Semestre: Fall 2026; 3 créditos.
- Profesor: Dr. James Houghton.
- Libro indicado: Bhunia, Sahoo, Shaikh, Advanced Optimization and Operations
  Research, Springer, 2019; opcional y suplementario según el syllabus.
- Software de clase: principalmente Julia y Excel; software de elección permitido.
- Temas del calendario tentativo: introducción; factibilidad y optimalidad;
  programación lineal; simplex; revised/dual simplex; post-optimality;
  redes; transporte/asignación; job shop; knapsack/dynamic programming.
- Idioma final: inglés académico sencillo. Transcripción: idiomas originales.
- Notación observada: x_i, f(x), Z/z; x∈R^N o Z^N; conjunto factible S;
  g_i(x)=0 para i∈E, g_i(x)≥0 para i∈J; P_i,Q_i,R_i y t para cargas de trabajo.
- Preferencias: conservar orden y fuentes; marcar añadidos, correcciones e ilegibles.

## Procedencia y fechas

- `raw/notes/14_09_2026/`: lote de 9 imágenes; IMG_7831–7834 muestran 14/9;
  IMG_7839 muestra 16/09/2026; IMG_7835–7838 del 16/09/2026, confirmado por el usuario en iteración 005.
  No atribuir todo el lote al 14. Se mantiene la ruta original.
- `raw/assignments/assignment1/`: material separado, no transcrito ni resuelto.
- `raw/syllabus/`: 4 imágenes inspeccionadas para extraer contexto; no transcripción integral.

El contexto no autoriza a rellenar palabras ilegibles ni a atribuir ampliaciones
al profesor. La plantilla original sugería Hillier & Lieberman sin verificar;
se retiró esa sugerencia al identificar el libro real. Las copias previas están
archivadas en `work/archive/context/iteration-004/`.

## Confirmaciones y criterio didáctico — iteración 005

- Trabajador 4, tarea P: coeficiente 19, confirmado por el usuario.
- Bases de planteamiento: datos/unidades → variables/dominio → objetivo → restricciones → supuestos → validación e interpretación.
- Figuras solo si explican el modelo; generadas con código y claramente etiquetadas.


## Formato definitivo — iteración 007 (sustituye regla diaria)

Una carpeta de entrada equivale siempre a un único documento completo de estudio:
un notes.tex y un notes.pdf con TODAS las imágenes, aunque haya fechas distintas.
Las fechas pueden ser secciones internas; nunca fragmentan la entrega. El compañero
traceability.tex/pdf conserva fuentes, ampliaciones, correcciones, fechas y revisión
para todo el mismo lote. Estudio limpio, explicaciones integradas, sin etiquetas editoriales.
Rutas: work/batches/RUTA_RELATIVA/ y final/RUTA_RELATIVA/ reflejan raw/RUTA_RELATIVA/.
No usar lectures/ ni documentos acumulativos antiguos. Todas las migraciones quedan
en CHANGELOG y README. Datos confirmados: P4=19 y fotos 7835–7838 del 16/09.
