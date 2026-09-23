# 4. Verificación y documentación del lote completo

REGLA VIGENTE: una carpeta de entrada = un único LaTeX/PDF de apuntes que abarca
TODAS sus imágenes, más un único LaTeX/PDF de trazabilidad para ese mismo conjunto.
Fechas distintas dentro de la carpeta NO generan entregas separadas.

Comparar el listado completo de imágenes de la carpeta, manifiesto, transcripción,
revisión, confirmaciones, notes.md, traceability.md y metadata.json.
Verificar cobertura exacta: ninguna foto omitida, duplicada ni excluida por fecha.
Conservar identidad de ruta (notes/lote, assignments/lote, syllabus) sin colisiones.

Comprobar ecuaciones, números, variables, índices, desigualdades, unidades, matrices
y tablas contra las fotos. El texto limpio enseña formulaciones correctas sin etiquetas
editoriales, nombres de fotos ni comparaciones con errores heredados. Los supuestos
relevantes permanecen. Toda fuente, ampliación, corrección original/motivo y duda
se documenta en el compañero de trazabilidad único del lote.

Comprobar figuras: coordenadas, signos, etiquetas, pies y procedencia en trazabilidad.
Compilar ambos documentos con --deliver raw/RUTA. Revisar visualmente todas las
páginas, tablas y figuras. Confirmar que build/notes.tex es la fuente única del PDF
completo de estudio y que final/RUTA contiene solo notes.pdf y traceability.pdf.
Registrar resultado y hashes en el trabajo interno; no insertar informes en el estudio.

No fingir revisión humana o independiente. La autorización existente permite generar
las entregas; comunicar dudas esenciales por el chat sin convertirlas en hechos.
Actualizar README y CHANGELOG: qué cambió, por qué, archivos, validación, pendientes
y cualquier ruta anterior→nueva. Archivar salidas reemplazadas y retirar referencias
activas al flujo obsoleto. No usar lectures/, main.tex, --build, --publish ni --preview.


Para assignments: trabajar los ejercicios seleccionados/autorizados y revisar las
soluciones aportadas contra sus enunciados. Incluir enunciado, variables y formulación de forma directa. Cada ejercicio ocupa
una página independiente dentro del MISMO LaTeX/PDF de la carpeta, sin portada
ni índice separado. Usar metadata.layout="one_problem_per_page" y verificar que
ningún ejercicio desborda su página. No incluir rótulos "Interpretation of the
constraints", "Check and interpretation", soluciones numéricas ni bloques de
comprobación. Mantener solo aclaraciones breves imprescindibles; las comprobaciones
y resultados de solver van en la trazabilidad separada. No añadir un apartado final de
teoría, información del tema ni explicaciones generales ajenas a los ejercicios.
Respetar exclusiones explícitas aunque el enunciado impreso pida resolverlas.
Registrar fotos de ejercicios no seleccionados en trazabilidad sin inventar soluciones.
Assignment 1: ejercicios 1, 2 y 5, y texto del 6 aportado posteriormente por el usuario.
La autorización del texto del 6 sustituye su exclusión anterior.
No usar guiones largos en la entrega limpia. Incluir autor y fecha indicados en
metadata; separar visualmente enunciado y formulación con subtítulos breves.
Definir variables de decisión explícitamente y distinguirlas de datos y parámetros.
Mostrar todos los costes, demandas y unidades; conservar notación del manuscrito
cuando sea clara. No sustituir balances correctos por desigualdades incompletas.

Para límites nutricionales del assignment, mostrar cada mínimo P_j N y máximo
u_j N en renglones separados; no usar desigualdades encadenadas.
