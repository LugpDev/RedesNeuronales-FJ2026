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
