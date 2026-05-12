# AI_LOG — Registro de uso de IA

## Entrada 1 — 2026-05-08

**Prompt:** Genera la estructura de archivos para este proyecto

**Respuesta resumida:** Claude propuso crear la estructura de carpetas definida en CLAUDE.md (`data_prep/`, `training/`, `inference/`, `models/`, `server/`, `ui/`) con archivos `.gitkeep` en cada directorio para que git los rastree, más los archivos raíz `requirements.txt`, `README.md`, `DEPLOYMENT.md` y este `AI_LOG.md` con contenido placeholder. En una primera propuesta incluyó esqueletos de código Python, pero al indicarle que solo se quería la estructura vacía, ajustó el alcance correctamente.

**Decisión tomada:** Decidí eliminar el contenido de `requirements.txt` para ir agregando las dependencias en el momento en el que se ocupen. Lo demás lo dejé igual.

**Reflexión crítica:** Como mejora le pediría que aún no agregara contenido a `DEPLOYMENT.md`, a `requirements.txt`, ni a `README.md`. Lo demás fue útil para ahorrar tiempo y dejar la estructura exactamente como lo necesita el proyecto.

## Entrada 2 — 2026-05-08

**Prompt:** ¿Dónde debería agregar mi dataset? / Ayúdame a crear las instrucciones sobre cómo descargarlo

**Respuesta resumida:** Claude sugirió organizar el dataset en `data_prep/raw/` con subcarpetas `train/`, `val/` y `test/`. Propuso crear un `.gitignore` para excluir los datos del repositorio y añadir instrucciones de descarga en el `README.md` con dos opciones: Kaggle CLI y descarga manual. También documentó la estructura esperada del dataset Chest X-Ray (Pneumonia) de Kaggle.

**Decisión tomada:** El único cambio realizado fue eliminar la parte de descarga con Kaggle CLI, ya que mi método fue la descarga manual.

**Reflexión crítica:** La sugerencia fue correcta, sin embargo, al haber utilizado la descarga manual preferí documentarlo de ésta manera.

## Entrada 3 — 2026-05-12

**Prompt:** Revisa si la semana 1 ya estaría completa / Genera el documento de definición en Markdown

**Respuesta resumida:** Claude identificó que el repositorio por sí solo no completaba la Semana 1, ya que faltaba el documento formal de definición y justificación técnica. Propuso una estructura de 5 secciones (descripción del problema, dataset, justificación técnica, stack tecnológico y plan de trabajo) y generó un borrador base en Markdown con los datos ya conocidos del proyecto, dejando marcados con `<!-- TODO -->` los apartados que requerían análisis propio.

**Decisión tomada:** Se aceptó el borrador como base. Se eliminaron las secciones 4 (stack tecnológico) y 5 (plan de trabajo) por decisión propia. Se redactó la motivación personal en la Sección 1 y la justificación del dataset en la Sección 3. El archivo se guardó como `DEFINICION.md` en el repositorio.

**Reflexión crítica:** El borrador fue útil como punto de partida ya que el contenido factual (estadísticas, ventajas, limitaciones) ya estaba estructurado, lo que me permitió enfocarme en los apartados que requieren criterio propio, como la motivación y la justificación del dataset. La sugerencia de incluir secciones de stack y plan de trabajo era válida, pero opté por omitirlas al considerarlas redundantes con la información ya documentada en otros archivos del proyecto.
