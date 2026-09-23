# ISE 555 — Una carpeta, un documento completo

**Regla vigente (iteración 007): TODO lo que esté en una misma carpeta de entrada
va siempre en el mismo LaTeX y PDF de apuntes.** Las fechas o temas pueden ser
secciones internas; nunca dividen automáticamente las entregas.

Se conserva la separación solicitada entre estudio y evidencia: por cada carpeta,
un `notes.pdf` limpio y un `traceability.pdf` complementario, cada uno con un único
LaTeX que abarca el lote completo. Esto sustituye el criterio anterior «por día».

## Entrega actual

Carpeta original: `raw/notes/14_09_2026/`, con **las nueve fotografías**, incluidas
las del 16/09. No se ha movido ni renombrado ninguna foto.

- [Apuntes completos — 8 páginas](../../Notes/14_09_2026/notes.pdf)
- [Trazabilidad completa — 8 páginas](../../Notes/14_09_2026/traceability.pdf)
- [LaTeX único de apuntes](work/batches/notes/14_09_2026/build/notes.tex)
- [LaTeX único de trazabilidad](work/batches/notes/14_09_2026/build/traceability.tex)

**Nota (iteración 012):** los PDF entregados ya no permanecen en `final/`; tras cada
entrega se trasladan a la carpeta `Notes/` en la raíz del repositorio (una subcarpeta
por lote, con la misma ruta relativa a `raw/`). `final/` queda vacío entre entregas;
`process_notes.py --deliver` lo recrea automáticamente en cada build.

## Contrato de contenido

`notes.pdf` contiene teoría correcta, definiciones, formulación de problemas,
explicaciones integradas, ejemplos, tablas y figuras. No muestra nombres de fotos,
Source, Documented Correction, Additional Explanation/Information ni historial
editorial. Enseña directamente las fórmulas correctas. Los supuestos y límites
matemáticos necesarios sí permanecen en el texto.

`traceability.pdf` cubre todas las imágenes del mismo lote: fuentes por sección,
original/corrección/motivo, ampliaciones, confirmaciones, fechas, figuras, verificación,
recordatorios excluidos y dudas. Limpiar apuntes no significa eliminar explicaciones
útiles ni perder evidencia. Incertidumbres esenciales se comunican por el chat;
no se inventan datos ni se presentan revisiones humanas que no han ocurrido.

La base didáctica común es: alcance → datos/unidades → variables/dominio → objetivo →
restricciones justificadas → supuestos → comprobación e interpretación.

## Estructura e identidad del lote

La ruta relativa a `raw/` se conserva íntegra. Así no colisionan carpetas de notes,
assignments y syllabus ni nombres parecidos. No se normalizan nombres de carpeta
como si fueran fechas: `14_09_2026` y `2026-09-14` son carpetas distintas.

```text
raw/notes/14_09_2026/                todas las fotos del lote, originales
work/batches/notes/14_09_2026/
  manifest.json                     inventario y hashes al preparar
  transcription.md                  transcripción fiel interna
  academic_review.md                revisión interna
  notes.md                          contenido limpio editable de todo el lote
  traceability.md                    evidencia editable de todo el lote
  metadata.json                     ruta exacta e inventario completo
  course_context.md                 contexto de referencia
  build/
    notes.tex                       único LaTeX completo de estudio
    traceability.tex                 único LaTeX completo de trazabilidad
    figures/                        recursos locales para compilar
    inputs/                         copia de entradas de la última compilación
    *.log                           logs
  build_report.json                 hashes de entradas, originales y PDFs
  review.md                         revisión visual/editorial
final/notes/14_09_2026/
  notes.pdf                         entrega de estudio
  traceability.pdf                  entrega documental
figures/                            gráficos reproducibles (PDF y PNG)
work/archive/                       versiones anteriores
```

La misma correspondencia se aplica a `raw/assignments/assignment1/` y `raw/syllabus/`.
No se mezclan carpetas distintas. Seleccionar una carpeta hoja: el sistema rechaza
carpetas que contengan otras carpetas, para evitar omisiones por recursión implícita.

## Cómo usarlo

Coloca las fotos y pide al asistente «procesa esta carpeta». El asistente hace
transcripción, revisión, redacción de ambos documentos y verificación. El script
organiza y compila; **no llama a una API ni transcribe imágenes por sí solo**.

Para preparar una carpeta nueva:

```bash
python3 process_notes.py raw/notes/OTRO_LOTE
```

Se admiten JPG/JPEG, PNG y WebP. Convierte HEIC/HEIF o PDF primero. Ordena los
nombres de archivo para reflejar el orden deseado; no se usa EXIF. La preparación
rechaza sobrescribir una sesión existente. Assignments y syllabus tienen revisión
de material separada; no se resuelven ejercicios automáticamente.

Para regenerar el lote actual completo:

```bash
python3 process_notes.py --deliver raw/notes/14_09_2026
```

Equivalente: `python3 scripts/build_batch.py raw/notes/14_09_2026`.
En VS Code, la tarea **Build complete folder PDFs** solicita la carpeta, no una fecha.

## Etapas y responsabilidades

1. **01_transcribe.md:** todas las imágenes de la carpeta, una transcripción interna;
   conservar orden, fechas, idiomas, fórmulas y `[UNCLEAR]` sin adivinar.
2. **02_review.md:** revisar todo el lote; registrar ampliaciones y correcciones
   con fuente y motivo. No sobrescribir el original ni separar por fechas.
3. **03_edit.md:** fabricar `notes.md` limpio y `traceability.md` completo en la misma
   sesión. Integrar explicaciones, enseñar formulaciones correctas, conservar
   evidencia fuera del texto de estudio. Crear metadata con todas las imágenes.
4. **04_verify.md:** cotejar ambos documentos y el inventario completo, comprobar
   matemáticas/figuras, compilar y revisar todas las páginas. Guardar review.md,
   actualizar README/CHANGELOG y entregar los dos enlaces.

La regla de agrupación está explícita en los cuatro prompts, incluidos redacción,
fabricación y documentación. Copias de los prompts vigentes están en la sesión activa.

Ejemplo de `metadata.json` (listar todas las imágenes reales, no un subconjunto):

```json
{
  "source_batch": "raw/notes/MI_LOTE",
  "course": "ISE 555: Advanced Deterministic Systems Optimization",
  "images": ["001.jpg", "002.jpg"],
  "display_date": "September 14 and 16, 2026",
  "image_dates": {"001.jpg": "2026-09-14", "002.jpg": "2026-09-16"}
}
```

`display_date` e `image_dates` son información descriptiva; no determinan particiones
ni rutas. El compilador rechaza omitir/duplicar una imagen aunque corresponda a otro día.

## Compilación, figuras y versiones

`scripts/build_batch.py` valida la carpeta exacta, cobertura de todas sus imágenes,
existencia de ambos contenidos y ausencia de etiquetas editoriales conocidas en estudio.
Genera cada LaTeX completo con `scripts/render_notes.py` y compila ambos en staging.
Solo sustituye los PDFs vigentes cuando ambas compilaciones tienen éxito.

Antes de sustituir, archiva PDFs anteriores, entradas previas disponibles e informe
en `work/archive/deliveries/RUTA_RELATIVA/TIMESTAMP/`. No hay bloqueo concurrente ni
transacción resistente a cortes de energía: ejecutar una entrega cada vez.
Los controles automáticos no sustituyen la comparación semántica con las fotos.

El renderer admite el subconjunto Markdown del proyecto (títulos, listas simples,
tablas, matemáticas y figuras); no es un conversor general. Editar los Markdown,
no el LaTeX generado. `build/` incluye figuras relativas para poder compilar el
LaTeX desde esa carpeta. Las referencias Markdown dependen de su ubicación; aquí
se usa `../../../../figures/NOMBRE.png` desde la sesión activa.

Figuras solo si aclaran geometría, objetivos, restricciones o estructura del modelo.
Código reproducible, PDF vectorial para LaTeX y PNG para Markdown; pie limpio y
procedencia en trazabilidad. Para las dos figuras existentes:

```bash
python3 scripts/generate_figures.py
```

Ese generador es específico de los ejemplos actuales, no interpreta fotos nuevas.

Dependencias: Python 3.10+ y Tectonic o latexmk/LaTeX; Matplotlib/NumPy para regenerar
figuras. Aquí se usa `.tools/tectonic` 0.17.0 y `.tools/cache`. El builder prioriza
Tectonic local, luego PATH, luego latexmk, sin habilitar shell escape. Nuevos paquetes
pueden necesitar red; los actuales están cacheados. No se subieron apuntes a servicios.

`raw/`, `work/` y `.tools/` están excluidos de Git: necesitan copia de seguridad
independiente. `final/` y `figures/` no están excluidos.

## Migración y retirada del flujo anterior

| Antes | Ahora |
|---|---|
| `final/2026-09-14/` y `final/2026-09-16/` | Unificados en `final/notes/14_09_2026/`; salidas antiguas archivadas |
| `work/days/FECHA/` | `work/batches/notes/14_09_2026/`; fuentes anteriores en archivo |
| `scripts/build_daily.py` | `scripts/build_batch.py` |
| `--deliver FECHA` | `--deliver raw/RUTA_RELATIVA` |
| `lectures/` | Eliminada: estaba vacía y ya no se usa |
| `main.tex`, `lectures.tex`, funciones antiguas publish/build | Retirados; archivos históricos conservados en archivo |

Archivo de esta migración: `work/archive/iteration-006/`, con README, prompts,
código, tests y entregas anteriores. `preview.pdf` sigue archivado en iteration-005.
Los documentos intermedios antiguos se conservan como evidencia, no como fuentes
vigentes. Los comandos --build/--preview/--publish ya no existen.
No se movieron originales. Ningún código activo genera o utiliza lectures/.

**Tras cada cambio o iteración:** actualizar CHANGELOG con motivo, archivos,
validaciones, pendientes y rutas anterior→nueva; actualizar README con el procedimiento
vigente. Archivar salidas reemplazadas para que final/ muestre solo lo actual.

## Validación actual

8 pruebas enfocadas al contrato vigente superadas: cobertura completa incluso con
fechas mixtas, identidad de carpeta, compañero obligatorio, limpieza de etiquetas,
conservación de la pareja anterior ante fallo, archivo de fuentes y preparación.

```bash
python3 -m unittest discover -s tests -v
```

Compilación de los dos PDFs unificados: 8 páginas cada uno, 16 páginas inspeccionadas
visualmente, logs sin avisos/desbordamientos. El estudio contiene ambos días y ambas
figuras sin etiquetas de trazabilidad. P4=19 y fechas confirmadas conservados.
Pendientes administrativos/contextuales permanecen en el PDF complementario.


## Assignment 1: iteración 011, 2026-09-21

- [PDF de ejercicios 1, 2, 5 y 6](../../Homework/HW1/Lopez_Juan_Assignment_1_21092026.pdf)
- [LaTeX completo](work/batches/assignments/assignment1/build/notes.tex)
- [Trazabilidad](../../Homework/HW1/traceability.pdf)

Ver la nota de la iteración 012 arriba: la entrega vive en `Homework/HW1/` en la
raíz del repositorio, no en `final/assignments/assignment1/`.

Un ejercicio por página, cuatro páginas en el mismo PDF/LaTeX. Autor:
Juan Lopez Olivan; fecha: 21/09/2026. Sin guiones largos ni apartados de
interpretación/comprobación, sin teoría final. El usuario ha aportado el texto
íntegro del ejercicio 6 y autorizado incluirlo: sustituye la exclusión anterior.
Los ejercicios 3 y 4 siguen fuera de la selección. Las seis fotos originales
permanecen en raw y el texto recibido queda en notes.md con procedencia en trazabilidad.

Variables explícitas y separación entre enunciado y formulación mediante encabezados
`###`. En el ejercicio 5, tabla de demandas D1..D4 y costes de producción CI1..CI4,
unidades, coste de inventario, stocks inicial/final y variables de producción/stock.
Se mantienen los balances completos corregidos. El texto del 6 se conserva tal como
lo aportó el usuario. Comprobaciones numéricas solo en el compañero documental.

```bash
python3 process_notes.py --deliver raw/assignments/assignment1
```

metadata.json admite document_title, author, display_date y
`layout: "one_problem_per_page"`. Este formato solo afecta a notes: cada `##`
inicia un ejercicio en página independiente, sin portada/índice; cada `###`
separa datos/variables del enunciado. Comprobar visualmente que nada desborde.
El LaTeX es autónomo. Mantener actualizados prompts y sus copias en el lote.
Tectonic descarga fuentes que falten en caché; esta iteración requirió cmmi7.pfb.
Si falla la compilación, se conserva la pareja anterior. No se envía a plataformas.

Fuentes anteriores: work/archive/iteration-009-assignment1/; entregas anteriores
archivadas automáticamente en work/archive/deliveries/. Rutas vigentes sin cambios.
Validación de esta entrega: cuatro páginas principales inspeccionadas, ambos PDFs
compilados, sin guiones largos en el texto extraído; ocho pruebas superadas.

Iteración 011: ejercicio 2 con ocho restricciones nutricionales explícitas,
una línea por mínimo y otra por máximo, manteniendo una página por ejercicio.
Modelo y datos sin cambios. Fuentes anteriores en work/archive/iteration-010-assignment1/.
