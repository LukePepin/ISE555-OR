# 3. Redacción y fabricación: una carpeta, un documento completo

REGLA VIGENTE: todas las imágenes de una misma carpeta de entrada forman SIEMPRE
un único documento de apuntes, un único LaTeX y un único PDF de estudio. Nunca
separar entregas por fecha, página o tema. Fechas distintas pueden organizarse
como secciones internas. La carpeta, no la fecha, identifica el lote.

Lee transcripción, revisión, contexto, manifiesto y confirmaciones del usuario.
Para raw/RUTA_RELATIVA crea en work/batches/RUTA_RELATIVA/:

1. notes.md: apuntes definitivos completos, en inglés sencillo, con explicaciones
   integradas y fórmulas correctas. Sin nombres de fotos, Source, Documented Correction,
   Additional Explanation/Information ni historia editorial. No eliminar explicaciones
   útiles al quitar etiquetas. Mantener supuestos y límites matemáticos relevantes.
2. traceability.md: UN compañero para TODO el lote, con correspondencia sección→foto,
   ampliaciones/motivos, original/corrección/justificación, confirmaciones, fechas,
   figuras, verificación y material administrativo excluido del texto de estudio.
3. metadata.json: source_batch (ruta completa raw/...), course, images (TODAS las
   imágenes de esa carpeta, una vez cada una), display_date opcional, image_dates
   opcional. Las fechas informan el contenido, nunca dividen la entrega.

Fabricación: python3 process_notes.py --deliver raw/RUTA_RELATIVA
Entrega: final/RUTA_RELATIVA/notes.pdf y traceability.pdf.
LaTeX: work/batches/RUTA_RELATIVA/build/notes.tex y traceability.tex.
Un solo notes.tex debe contener TODO el contenido de la carpeta. El segundo tex/pdf
es únicamente la trazabilidad separada autorizada por el usuario, no otra partición
académica del lote. No usar preview.pdf, work/days, main.tex ni lectures/.

Bases de formulación: alcance → datos/unidades → variables/dominio → objetivo →
restricciones justificadas → supuestos → validación e interpretación. Distinguir
cantidades, fracciones y variables binarias. Ante datos esenciales dudosos, preguntar
por el chat; no inventar. Conservar los pendientes y las decisiones en trazabilidad.

Figuras solo si explican geometría, objetivo, restricciones o estructura del modelo.
Código reproducible, PDF vectorial y PNG para Markdown. Pies académicos limpios;
fuente y carácter añadido en traceability.md. No figuras decorativas ni soluciones
no calculadas. Resolver rutas relativas desde la carpeta de trabajo efectiva.

Registrar cada cambio, iteración y migración en CHANGELOG.md y actualizar README.md.
Archivar entregas anteriores, sin mover originales ni dejar salidas viejas como vigentes.


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
