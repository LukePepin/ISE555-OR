# Historial de cambios

Todas las modificaciones se registran aquí y se reflejan en README.md.
Para nuevas entradas: fecha, iteración, motivo, archivos, comportamiento,
validación, pendientes y migraciones (anterior → nueva, o «ninguna»).

## 2026-09-23: Iteración 012, entregas trasladadas a Homework/Notes en la raíz

- Motivo: el usuario organizó el repositorio en tres carpetas de nivel superior
  (`Homework/`, `Notes/`, `Processing/`); las entregas ya no deben vivir dentro
  de la herramienta interna.
- Archivos: `final/assignments/assignment1/Lopez_Juan_Assignment_1_21092026.pdf`
  y `traceability.pdf` → `Homework/HW1/`; `final/notes/14_09_2026/notes.pdf` y
  `traceability.pdf` → `Notes/14_09_2026/`. `final/` quedó vacío y se eliminó.
- README actualizado con los nuevos enlaces relativos (`../../Homework/HW1/…`,
  `../../Notes/14_09_2026/…`) y nota explicando la convención.
- Sin cambios en `raw/`, `work/`, scripts o pruebas. `process_notes.py --deliver`
  sigue escribiendo en `final/RUTA_RELATIVA/` (lo recrea con `mkdir(parents=True,
  exist_ok=True)`); una entrega futura debe volver a moverse manualmente a
  `Homework/` o `Notes/` tras verificarla.
- Validación: no se repitieron las pruebas ni la compilación, ningún LaTeX ni
  script cambió. Migraciones: ver «Archivos» arriba (rutas anterior → nueva).

## 2026-09-21: Iteración 011, límites nutricionales separados

- notes.md del assignment: cuatro desigualdades dobles del ejercicio 2 pasan a
  ocho líneas: mínimos >= P_j N y máximos <= u_j N. Sin cambios matemáticos.
- traceability.md, prompts 03/04 y copias, README y review actualizados.
- Fuentes previas en work/archive/iteration-010-assignment1/; entregas anteriores
  archivadas automáticamente. Rutas finales sin cambios.
- Regenerados ambos PDFs y LaTeX. Verificación de página y restricciones del ejercicio 2.

## 2026-09-21: Iteración 010, presentación y ejercicio 6 aportado

- Autor Juan Lopez Olivan y fecha 21/09/2026 en metadata y encabezado. Títulos
  sin guiones largos; build_batch usa dos puntos y transmite author al renderer.
- render_notes admite encabezados ###, autor y espacio entre párrafos para assignments.
- notes.md: variables explícitas en 1/2/5; tabla de demandas D y costes CI con
  unidades en 5, almacenamiento y stocks; conserva balances matemáticos correctos.
- Incorporado texto íntegro del ejercicio 6 recibido por chat. Selección metadata
  1/2/5/6, exclusiones 3/4. Superada la exclusión previa del 6 por nueva instrucción.
- traceability registra procedencia del texto y notación; prompts 03/04 y copias
  reflejan presentación, costes, autor/fecha y nueva selección. README y review actualizados.
- Archivo de fuentes/código/documentación previos en work/archive/iteration-009-assignment1/;
  PDFs previos archivados automáticamente. Sin migración de rutas.
- Compilaciones iniciales fallaron por fuentes cmmi6/cmmi7 ausentes sin red; se
  simplificó subíndice CI y se descargó cmmi7 con acceso autorizado. Entrega final
  compilada: cuatro páginas principales, una por ejercicio; ambos PDFs regenerados.
- Inspección visual de las cuatro páginas, extracción de texto sin guiones largos,
  ocho pruebas automatizadas superadas. Sin envío externo.

## 2026-09-21 — Iteración 009: un ejercicio por página

- Petición: eliminar apartados de interpretación/comprobación y soluciones añadidas.
- notes.md de assignment1: retirados rótulos repetitivos, interpretaciones extensas,
  óptimos y tabla de solución; conservados enunciados, variables y formulaciones.
- metadata.json añade layout one_problem_per_page. scripts/render_notes.py genera
  ejercicios en páginas independientes sin portada/índice ni doble numeración;
  scripts/build_batch.py aplica este formato solo al documento principal.
- traceability.md registra revisión y conserva evidencia numérica por separado.
- Prompts 03/04 y copias del lote actualizados; README documenta configuración,
  procedimiento y entrega; review.md recoge verificación de esta iteración.
- Fuentes anteriores en work/archive/iteration-008-assignment1/; entregas previas
  conservadas por el compilador en work/archive/deliveries/.
- Regenerados ambos PDFs y LaTeX/logs/informes. Principal: 3 páginas (1,2,5),
  inspeccionadas visualmente y mediante extracción de texto; compañero: 3 páginas.
  Ejercicio 6 sigue excluido. Compilación correcta y 8 pruebas superadas.
- Sin migraciones: final/assignments/assignment1/ mantiene la pareja de PDFs.

## 2026-09-21 — Iteración 008: Assignment 1 en LaTeX y PDF

- Usuario solicita revisar soluciones aportadas y enunciados, claridad dentro de cada
  ejercicio, sin apartado final de teoría; excluye expresamente el ejercicio 6.
- Inventario visual: IMG_7828/7829/7830 enunciados; IMG_7897/7898/7899 soluciones
  de 1,2,5. Se trabaja esa selección de tres ejercicios; no se inventan soluciones 3/4.
- Nuevas fuentes en work/batches/assignments/assignment1/: notes.md, traceability.md,
  metadata.json, manifest.json (seis hashes), transcription.md estructurada,
  academic_review.md, numerical_check.json, review.md y copias de contexto/prompts.
- Ejercicio 1: corregida capacidad de forja a 90000 y formalizado objetivo; chequeo
  y solver confirman 45000 ensamblajes/año. Ejercicio 2: índices/unidades/límites u_j
  consistentes y no negatividad explícita. Ejercicio 5: balances de inventario
  completos, no negatividad, I4=0; óptimo 92750 validado algebraicamente y por solver.
- Enunciados fielmente reescritos, no transcripción literal de toda la hoja. Ejercicio 6
  permanece sin redactar; obligatorio según fuente pero excluido por el usuario.
- scripts/build_batch.py: título configurable mediante document_title; resto del
  contrato de carpeta y par de documentos sin cambios.
- Prompts 03/04: criterio para assignments, explicaciones dentro de cada ejercicio,
  sin apéndice de teoría, respetar selección y exclusiones explícitas.
- README: enlaces, comando, alcance, correcciones y regla de assignments.
- Entregas final/assignments/assignment1/notes.pdf (4 páginas) y traceability.pdf
  (3 páginas); LaTeX único autónomo en build/notes.tex. Sin figuras innecesarias.
- Validación: revisión visual de las 7 páginas, compilación y comprobaciones numéricas.
  Sin envío a plataforma docente. Rutas: ninguna migración, nuevo lote en estructura vigente.

## 2026-09-17 — Iteración 007: la carpeta define el documento

- Instrucción explícita: todas las imágenes de una carpeta deben ir siempre en
  un mismo LaTeX/PDF, aunque contengan varias fechas; mantener compañero documental.
  El usuario autoriza borrar lectures/ si no se usa y exige la regla en todos los prompts.
- Reunificadas las nueve imágenes de raw/notes/14_09_2026: notes.md y traceability.md
  completos en work/batches/notes/14_09_2026/. Fechas solo como secciones internas.
  Metadata con carpeta exacta, nueve imágenes, fechas y display_date. Copias de
  transcripción, revisión, manifiesto y confirmaciones para conservar evidencia.
- Entrega vigente: final/notes/14_09_2026/notes.pdf y traceability.pdf, 8 páginas cada uno.
  Un notes.tex y un traceability.tex completos en build/ de la sesión.
- scripts/build_daily.py → scripts/build_batch.py: identidad por ruta relativa a raw,
  validación de inventario íntegro sin subconjuntos por día, rechazo de duplicados,
  selección de carpeta hoja, salidas y archivo por misma ruta; fechas descriptivas.
- process_notes.py: preparación en work/batches/RUTA; --deliver recibe carpeta,
  no fecha; retiradas funciones/argumentos históricos de publicación y acumulativo.
- Eliminada lectures/ vacía; main.tex y lectures.tex retirados de raíz con copia
  histórica. No quedan consumidores activos de lectures/.
- Cuatro prompts actualizados: gestión/transcripción, revisión, fabricación y
  documentación obligan a procesar toda la carpeta, fuentes separadas del estudio
  y registro de decisiones/migraciones. Copias vigentes en la sesión activa.
- course_context.md y copia activa: agrupación por carpeta sustituye regla diaria.
- .vscode/tasks.json: tarea por carpeta. README reescrito con contrato, comandos,
  LaTeX único, enlaces, estructura, migraciones, dependencias y validación.
- tests/test_daily.py → tests/test_batches.py; tests/test_workflow.py adaptado al
  nuevo contrato y eliminado comportamiento obsoleto. 8 pruebas superadas, incluida
  una carpeta con dos fechas que produce un solo par y rechazo de foto omitida.
- Archivo work/archive/iteration-006/: README/código/tests/prompts/plantillas previos,
  fuentes work/days y las dos carpetas final por fecha retiradas de la entrega vigente.
  work/2026-09-14/DELIVERY_MOVED.md apunta ahora al lote unificado.
- Validación: compilación local de ambos PDFs sin avisos, extracción de texto confirma
  ambos modelos y ausencia de etiquetas editoriales; inspección visual de 16 páginas.
- Migraciones: final/FECHA → final/notes/14_09_2026; work/days → work/batches/RUTA;
  build_daily → build_batch; --deliver FECHA → --deliver raw/RUTA. Originales intactos.
- Pendientes previos conservados en trazabilidad; P4=19 y fechas del 16/09 resueltos.

## 2026-09-17 — Iteración 006: dos PDFs definitivos por día

- Preferencia explícita: apuntes de estudio correctos e integrados, sin fuentes,
  etiquetas de añadidos/correcciones ni errores originales; segundo PDF separado
  conserva toda la trazabilidad. Entregas por fecha, no preview.pdf mixto.
- `work/days/2026-09-14/` y `work/days/2026-09-16/`: nuevos notes.md limpios,
  traceability.md completos y metadata.json con fechas y fuentes por día; copia
  de contexto vigente. Día 14: IMG_7831–7834; día 16: IMG_7835–7839.
- Limpieza semántica: se integran ampliaciones; se enseñan únicamente fórmulas
  corregidas; comparación original/corrección, referencias a imágenes, dudas y
  recordatorios administrativos pasan a trazabilidad. Se conservan supuestos.
  La comparación producción/fracciones se sitúa en el día 16, tras ambos modelos.
- `final/2026-09-14/notes.pdf` (5 páginas) y traceability.pdf (4 páginas).
  `final/2026-09-16/notes.pdf` (4 páginas) y traceability.pdf (4 páginas).
  Exactamente dos archivos de entrega por día; fuentes/logs fuera de final/.
- `scripts/render_notes.py`: refactorización a biblioteca sin fecha fija, plantilla
  diaria con portada/índice, sin entornos editoriales visibles; rutas de código
  ajustables, figuras relativas y trazabilidad alineada a izquierda para evitar
  problemas de justificación de rutas largas.
- `scripts/build_daily.py`: validación de fecha y compañero obligatorio, rechazo
  de marcadores de fuentes/ilegibles en estudio, hashes de originales/entradas/salidas,
  compilación temporal de ambos PDFs antes de sustituir entregas, archivo de versiones
  anteriores con fuentes de compilación cuando existen. Limitación: sin bloqueo
  concurrente ni transacción resistente a fallos de disco.
- Ajustes durante compilación: descarga de fuente lmr12.pfb en caché local tras
  restricción de red; copia de figuras a staging para resolver rutas portables;
  ajuste de paths y alineación elimina desbordamientos/avisos de los complementos.
- `process_notes.py`: nuevo --deliver FECHA; --preview y --publish retirados de CLI
  con indicación del reemplazo. Funciones históricas y --build acumulativo conservados
  como legado; no sincronizan entregas diarias. Preparación de raw compatible.
- `.vscode/tasks.json`: tarea Build both daily PDFs con fecha solicitada.
- Prompts 03/04 y copias del lote: contrato de dos documentos, sin etiquetas en
  estudio, evidencia/correcciones en compañero, revisión de ambos y autorización
  existente suficiente para generar. Curso/contextos diarios reflejan la preferencia.
- `README.md`: guía reescrita con reglas vigentes, rutas, comandos, regeneración,
  limitaciones, dependencias, copias de seguridad, migraciones y cuatro enlaces.
- `tests/test_daily.py`: cuatro pruebas nuevas (fecha/matemáticas, etiquetas y
  compañero, fallo del segundo PDF, archivo de fuentes anteriores). Total 14 pasan.
- `review.md` por día: revisión visual de todas las 17 páginas, sin avisos en logs.
  Extracción de texto confirma ausencia de IMG_/Source/Documented Correction/
  Additional Explanation/Information en los dos PDFs limpios. Hashes comprobados.
- `build_report.json` por día: resultados de compilación, hashes y páginas.
- Archivo del README/renderer/prompts previos en work/archive/iteration-005/.
  PDF/TeX/log de preview trasladados allí; lote de work/2026-09-14 conservado como
  evidencia y marcado mediante DELIVERY_MOVED.md. Regeneraciones de esta iteración
  archivadas automáticamente en work/archive/deliveries/FECHA/TIMESTAMP/.
- Migraciones: raíz preview.pdf/preview.tex → work/archive/iteration-005/;
  salida de estudio mixta → final/FECHA/{notes,traceability}.pdf;
  fuentes de redacción activa → work/days/FECHA/{notes,traceability}.md.
  No se movió ni modificó ninguna foto original. No se subieron apuntes a servicios.
- Pendientes: recordatorio HW1, abreviaturas, introducción recortada y unidades no
  especificadas; detallados en trazabilidad. Fecha y coeficiente 19 resueltos.

## 2026-09-17 — Iteración 005: PDF, confirmaciones y bases de formulación

- Usuario confirma coeficiente P del trabajador 4 = 19 y fechas IMG_7835–7838 =
  16/09/2026; solicita PDF real y figuras solo si ayudan a entender el planteamiento.
- Archivo de notas/revisión/contexto/preview anteriores en
  `work/archive/2026-09-14/iteration-004/`; originales intactos.
- `notes.md` y `draft.tex`: fechas y coeficiente corregidos; ampliación de siete pasos
  para formular problemas, unidades y dominios, dirección de restricciones,
  producción frente a fracciones, validación del modelo y errores habituales.
- `transcription.md` y `academic_review.md`: addendum con confirmaciones, conservando
  lecturas originales históricas. `user_confirmations.json`: evidencia estructurada.
  `manifest.json`: fechas por fotografía sin cambiar origen ni hashes.
- Contextos raíz y sesión actualizados con fechas, dato y criterio pedagógico.
- `scripts/generate_figures.py`: dos figuras reproducibles Matplotlib/NumPy.
  `figures/2026-09-14-feasible-region.{pdf,png}`: región y líneas de objetivo.
  `figures/2026-09-16-workload-model.{pdf,png}`: tareas, cargas y cota t.
- `scripts/render_notes.py`: renderer del Markdown del piloto, antes temporal;
  soporte de figuras, comprobación de existencia, numeración y comillas corregidas.
  Genera fragmento draft.tex y documento preview.tex; no conversor general.
- `main.tex`/`preview.tex`: inputenc condicionado al motor; margen de ajuste de
  párrafos para eliminar un desbordamiento de 10 pt. Formato revisado visualmente.
- `process_notes.py`: --preview; compilación compartida con --build; fallback a
  Tectonic local/PATH si falta latexmk; caché dentro del proyecto.
- Instalación sudo no realizada: requiere contraseña. Descargado Tectonic 0.17.0
  del repositorio oficial a `.tools/`; primera compilación descargó paquetes y
  fuentes, posteriores compilaciones usan caché local. No se subieron apuntes.
- `.gitignore`: .tools/ excluido. `.vscode/tasks.json`: tarea para PDF de estudio.
- Prompts 03/04 y sus copias de sesión: método de formulación y criterio de figuras,
  validación matemática y revisión visual del PDF.
- `verification.md/json`, `numerical_check.json`: estado actualizado; dudas P4 y
  fechas resueltas; quedan recordatorios incompletos, introducción cortada y unidad
  temporal no indicada. No aprobación humana integral inferida.
- `build_report.json`: compilador, comando, hash y validación de PDF.
- `README.md`: enlaces, estado actual, comandos de regeneración, dependencias,
  límites del renderer, archivo anterior y criterios didácticos.
- Validación: 10 pruebas superadas; `python3 process_notes.py --preview` produce
  preview.pdf (8 páginas), compilación final sin avisos/desbordamientos. Renderizadas
  y revisadas visualmente las 8 páginas y ambas figuras. Recompilación con caché exitosa.
- Rutas: ninguna migración; se mantienen las fotos y el lote mixto en sus ubicaciones.

## 2026-09-17 — Iteración 004: primeros apuntes reales

- Solicitud: entregar los apuntes, no limitarse a preparar carpetas.
- Inspección visual de las 9 fotografías de notas y las 4 del syllabus; ninguna
  foto editada, movida o renombrada. Assignment fuera de esta entrega.
- `work/2026-09-14/transcription.md`: transcripción con bloques por fotografía,
  fórmulas originales, descripción de dibujos, fragmentos ilegibles/cortados.
- `academic_review.md` en esa sesión: correcciones de signos, dominio binario,
  definiciones de mínimos y explicación de modelos; sin correcciones silenciosas.
- `notes.md`: primera versión de lectura inglesa, nueve secciones, tablas,
  ejemplos, demostraciones añadidas etiquetadas y pendientes explícitos.
- `draft.tex`: versión LaTeX; `preview.tex`: entrada separada para visualizar el
  borrador sin publicarlo. Conversión local puntual; se corrigieron escapes de
  reemplazos y tratamiento de comillas durante su generación, antes de entregar.
- `verification.md` y `verification.json`: revisión por IA (no independiente ni
  humana), hash actual, discrepancias y aprobación falsa. No publicación.
- `numerical_check.json`: SciPy/HiGHS confirma óptimo de muebles 62500 en
  (375,0,0,62.5); sustitución y cota dual también verificadas. Seguro sin resolver:
  coeficiente P4 ambiguo 15/19, conservado como a4 en el desarrollo.
- `work/syllabus/material_review.md`: extracción selectiva con fuentes y límites;
  no se afirma transcripción completa ni verificación humana del syllabus.
- `course_context.md`: identificación ISE 555, profesor y libro fotografiado;
  retirada sugerencia provisional Hillier & Lieberman. Sin consultar libro o web.
- Archivo de contexto previo en `work/archive/context/iteration-004/` y actualización
  explícita de copias de contexto en sesiones de apuntes y syllabus. Copia del
  assignment sin cambios, documentado para su procesamiento futuro.
- `main.tex`: título real de la asignatura. `lectures.tex` permanece vacío.
- `.gitignore`: exclusión adicional de preview.pdf. README actualizado con enlaces,
  uso directo, compilación opcional, estado real y listado de todos los artefactos.
- Fechas: se detecta 16/09/2026 en IMG_7839 dentro del lote nominal del 14;
  fechas de IMG_7835–7838 pendientes. Borrador rotulado September 14–16.
- Validación: hashes originales coinciden; cobertura de 9 fotos; delimitadores
  LaTeX equilibrados. Sin motor pdflatex/latexmk/tectonic: PDF no generado ni
  compilación validada. Código Python del workflow sin cambios; pruebas no repetidas.
- Rutas: ninguna migración; nuevas salidas de borrador y archivo documentadas arriba.

## 2026-09-17 — Iteración 003: clasificación por procedencia

- Motivo: el usuario organizó originales en notes, assignments y syllabus; el
  script anterior rechazaba estas rutas y las fechas DD_MM_YYYY.
- Inventario: 9 imágenes en `raw/notes/14_09_2026/`, 3 en
  `raw/assignments/assignment1/` y 4 en `raw/syllabus/`.
- `process_notes.py`: clasificación de fuentes, normalización de fechas,
  manifiesto con source_type y ruta real; publicación verifica esa ruta en vez
  de reconstruirla desde la fecha. Compatibilidad con entradas y manifiestos
  anteriores. Materiales no lectivos reciben dos prompts y no se publican.
- Prompt de revisión de materiales generado por el script: conservar enunciados
  sin resolverlos y extraer datos del syllabus sin inventarlos ni cambiar contexto.
- `course_context.md`: procedencia de los tres tipos y datos académicos pendientes
  de confirmar; contenido de las fotos todavía no revisado.
- `tests/test_workflow.py`: tres pruebas nuevas de estructura anidada/publicación,
  separación de materiales y rechazo de fechas inválidas/rutas fuera de raw.
- `README.md`: árbol, comandos, inventario, salidas, revisión de materiales,
  copias de contexto, compatibilidad y archivo de versiones actualizados.
- Cambio de convención: `raw/FECHA/` → `raw/notes/FECHA/`; no se trasladó ni
  renombró ningún original. `14_09_2026` → `2026-09-14` solo en fechas internas
  y salidas. Las salidas de apuntes permanecen en `work/FECHA_ISO/` y `lectures/`.
- Nuevas rutas de trabajo: `work/assignments/ID/` y `work/syllabus/`.
- Preparadas las tres sesiones reales con manifiestos, hashes, contexto y prompts;
  la sesión de apuntes incluye aprobación inicialmente falsa. Ninguna transcripción,
  solución, clase publicada o PDF se generó en esta iteración.
- Validación: 9 pruebas superadas y preparación correcta de las 16 imágenes.
  Compilación no repetida: no hubo cambios en LaTeX y sigue pendiente instalar latexmk.

## 2026-09-17 — Iteración 001: implementación inicial

- Punto de partida: carpeta vacía, sin código ni apuntes existentes.
- Decisión: piloto manual para 3–4 clases antes de automatizar llamadas a un modelo.
- `process_notes.py`: preparación de sesiones, fechas ISO, listado ordenado de
  imágenes, hashes de originales, copia de prompts/contexto, aprobación humana
  vinculada al hash del borrador, rechazo de dudas y discrepancias, publicación
  sin sobrescritura, índice cronológico, recibo y compilación con latexmk.
- `prompts/01_transcribe.md`: transcripción fiel con fuentes y `[UNCLEAR]`.
- `prompts/02_review.md`: revisión separada con ampliaciones y correcciones trazables.
- `prompts/03_edit.md`: inglés y LaTeX, preservación del orden y origen.
- `prompts/04_verify.md`: comparación independiente de matemáticas contra fotos.
- `course_context.md`: contexto provisional editable, sin referencias inventadas.
- `main.tex`: plantilla estable, entornos definition/example/remark/correction.
- `lectures.tex`: índice inicialmente vacío; `references.bib`: bibliografía vacía.
- Directorios `raw/`, `work/`, `lectures/`, `figures/`, `prompts/`, `tests/`:
  separación entre originales, evidencia, publicación y recursos.
- `.vscode/tasks.json`: tarea de compilación; `.gitignore`: exclusión de originales,
  intermedios locales, cachés Python y productos de compilación.
- `README.md`: instalación, rutas, cuatro pasadas, aprobación, publicación,
  compilación, revisión, archivo de versiones y plan de evolución.
- Rutas: ninguna migración. Se añade `work/` para evidencia y `lectures.tex` como
  índice generado en lugar de editar main.tex después de cada clase.
- Pendiente: fotos reales, confirmar contexto y evaluar las primeras cuatro clases.

## 2026-09-17 — Iteración 002: validación local

- `tests/test_workflow.py`: pruebas aisladas de preparación/publicación, índice
  cronológico, rechazo de hash obsoleto, fotos modificadas, aprobación incompleta,
  contenido ilegible y sobrescritura.
- `README.md`: comando de pruebas, límites de validación, registro del piloto.
- Rutas: ninguna migración.
- Resultado: `python3 -m unittest discover -s tests -v`, 6 pruebas superadas.
- Compilación intentada con `python3 process_notes.py --build`: bloqueada por
  ausencia de `latexmk`; no se generó PDF ni se validó la plantilla con un motor
  LaTeX. No se instalaron dependencias del sistema.
- Cierre: README actualizado con el resultado y la limitación; pendiente validar
  PDF tras instalar LaTeX y calidad visual cuando haya fotografías reales.
