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

## Entrada 4 — 2026-05-12

**Prompt:** ¿Qué estrategias de balanceo existen, y cuáles me serían útiles para este proyecto? / Redacta esta información en un documento markdown

**Respuesta resumida:** Claude explicó 5 estrategias de balanceo aplicables al desbalance 73% PNEUMONIA / 27% NORMAL del dataset: (1) pesos de clase en la función de pérdida (`BCEWithLogitsLoss` con `pos_weight`), (2) oversampling con `WeightedRandomSampler`, (3) data augmentation diferencial sobre la clase minoritaria, (4) ajuste del umbral de decisión post-entrenamiento vía curva ROC, y (5) undersampling (descartada por pérdida de datos injustificada). Recomendó combinar `class_weight` + `WeightedRandomSampler` como base de entrenamiento y ajustar el umbral al evaluar. Posteriormente generó el documento `data_prep/BALANCEO_CLASES.md` con código de ejemplo, tabla comparativa y sección de métricas prioritarias.

**Decisión tomada:** Acepté el documento sin cambios ya que únicamente es un documento de investigación y no requería un análisis crítico

## Entrada 5 — 2026-05-12

**Prompt:** ¿Qué debo hacer para la Semana 2? / Genera el script de preprocesamiento y el archivo de transformaciones

**Respuesta resumida:** Claude identificó que la entrega de Semana 2 requería un script de preprocesamiento documentado. Antes de generar código, propuso dos decisiones clave: (1) tamaño de imagen 224×224 usando CNN desde cero, con la justificación de que este tamaño es compatible con transfer learning en Semana 5 sin cambiar el preprocesamiento; (2) reparar el val set de Kaggle, que tiene solo 16 imágenes (8 por clase), redistribuyendo ~10% del train a val manteniendo la proporción de clases. Generó tres archivos: `data_prep/preprocess.py` (verifica integridad, redistribuye val, genera `splits.json`), `data_prep/transforms.py` (transformaciones de PyTorch para train y eval), y actualizó `requirements.txt` con las dependencias necesarias.

**Decisión tomada:** Revisé el código generado para verificar que cumpliera con lo esperado. Acepté los archivos `data_prep/transforms.py` y `requirements.txt` sin modificaciones. En `data_prep/preprocess.py` realicé un ajuste, ya que el script original de Claude omitía las imágenes del directorio `val/` original de Kaggle al redistribuir los splits, por lo que modifiqué la lógica para incorporarlas al nuevo conjunto de validación antes de aplicar la redistribución desde `train/`.

**Reflexión crítica:** La sugerencia fue sólida en cuanto a las decisiones de diseño previas al código: elegir 224×224 pensando en compatibilidad con transfer learning evita refactorizaciones futuras. Sin embargo, el script presentó un error al ignorar el directorio `val/` original de Kaggle, lo que hubiera resultado en datos descartados sin justificación. La corrección fue sencilla una vez identificado el problema, pero evidencia la importancia de validar el código generado contra la estructura real del dataset antes de aceptarlo.

## Entrada 6 — 2026-05-13

**Prompt:** Propón 2 arquitecturas CNN baseline para clasificación de pneumonia. Explica las diferencias y qué esperar de cada una en términos de accuracy y tiempo de entrenamiento.

**Respuesta resumida:** Claude propuso dos arquitecturas para el entregable de Semana 3: (A) CNN pequeña de 3 bloques Conv simples (~6–8 M parámetros, ~78–84% acc esperado), útil para verificar el pipeline rápidamente; (B) CNN moderada estilo VGG con bloques dobles de convoluciones + BatchNorm + GlobalAveragePooling (~1.5–2 M parámetros, ~85–90% acc esperado), adecuada para el reporte formal. Recomendó una estrategia en dos pasos: primero Arq. A para validar el flujo, luego Arq. B para el entrenamiento formal. Generó el documento `training/CNN_BASELINE_ARQUITECTURAS.md` con tablas comparativas y señales de alerta durante el entrenamiento.

**Decisión tomada:** Implementé directamente la Arquitectura B, saltándome el paso intermedio de validar el pipeline con la Arquitectura A. Esto porque ya había verificado previamente un pipeline equivalente al revisar un ejemplo en YouTube con una arquitectura similar a la A, por lo que repetir esa validación me pareció redundante.

**Reflexión crítica:** Haber encontrado previamente un ejemplo similar a la Arquitectura A en YouTube me ahorró tiempo de desarrollo y validación, lo que me permitió enfocar el esfuerzo directamente en construir la Arquitectura B, que era la que realmente importaba para obtener un buen resultado en el reporte formal. Tras investigar un poco más sobre el diseño propuesto, confirmé que la sugerencia de Claude era sólida, por lo que la implementé sin modificaciones.

## Entrada 7 — 2026-06-17

**Prompt:** ¿Cómo funciona una matriz de confusión? / Explícame mi matriz de confusión / ¿Qué es una curva ROC? / ¿Qué se interpreta de las curvas de entrenamiento?

**Respuesta resumida:** Claude explicó los cuatro conceptos de evaluación de modelos aplicados al proyecto de neumonía: (1) Estructura de la matriz de confusión (TP, TN, FP, FN) y métricas derivadas; (2) Análisis de la matriz real del modelo: 7 FN, 92 FP, 84.1% accuracy, 98.2% recall en PNEUMONIA — modelo sesgado hacia predecir neumonía por desbalance de clases; (3) Curva ROC: traza TPR vs FPR a todos los umbrales posibles, el AUC mide la separabilidad global entre clases; (4) Curvas de entrenamiento: permiten detectar overfitting (val loss sube mientras train loss baja), underfitting (ambas estancadas) e inestabilidad (oscilaciones por learning rate alto).

**Reflexión crítica:** Las explicaciones de Claude fueron claras y, al tener contexto del proyecto, pudo aterrizar los conceptos directamente sobre mis resultados (p. ej., interpretar los 92 FP y el sesgo hacia PNEUMONIA en mi propia matriz de confusión), lo cual facilitó mucho la comprensión frente a una explicación genérica de manual.
