# Proyecto CNN — Servicio Becario

## Contexto general
Proyecto individual de clasificación de imágenes con Redes Neuronales Convolucionales (CNN).
Programa: Servicio Becario | Carrera: ITC (4to semestre) | Duración: 12 semanas
Responsable académico: Atoany Fierro — Área de Inteligencia Artificial

## Objetivo
Desarrollar un sistema completo end-to-end que incluya:
- Selección y preprocesamiento de dataset público de imágenes
- Entrenamiento y optimización de modelo CNN
- Evaluación formal con métricas estándar
- Servidor local con API (FastAPI) y endpoint `/predict`
- Interfaz de usuario conectada al servidor
- Documentación reproducible de despliegue

## Stack tecnológico
- **Lenguaje:** Python 3.x
- **Deep Learning:** PyTorch (preferido) o TensorFlow/Keras
- **Servidor:** FastAPI + Uvicorn
- **Visión:** torchvision, albumentations, Pillow, OpenCV
- **Métricas y análisis:** scikit-learn, matplotlib, seaborn
- **Entorno:** pip + requirements.txt (no conda)

## Estructura de carpetas esperada
```
project/
├── data_prep/        # Scripts de limpieza, splits, augmentation
├── training/         # Notebooks y scripts de entrenamiento
├── inference/        # Función predict(image) y pipeline de inferencia
├── models/           # Pesos guardados del modelo (.pt o .h5)
├── server/           # API FastAPI con endpoint /predict
├── ui/               # Interfaz de usuario
├── requirements.txt
├── README.md
├── DEPLOYMENT.md
├── AI_LOG.md
└── CLAUDE.md
```

## Reglas de colaboración (IMPORTANTE)
1. **Siempre sugiere, no decidas por mí.** Propón opciones con sus tradeoffs; yo elijo.
2. **Explica el razonamiento.** Por qué esa arquitectura, por qué ese hiperparámetro, qué esperar.
3. **No implementes todo de golpe.** Avanza en pasos pequeños y verificables.
4. **Si propones código, indica qué métricas o resultados debería ver** al ejecutarlo.
5. **El análisis crítico y la justificación final siempre son míos**, no tuyos.
6. **Antes de modificar un archivo existente**, muéstrame qué cambiarás y por qué.

## Métricas obligatorias
Todo modelo entrenado debe reportar:
- Accuracy, Precision, Recall, F1-score (por clase y promedio)
- Matriz de confusión
- ROC-AUC (cuando aplique)
- Curvas de loss y accuracy durante entrenamiento

## AI_LOG.md — registro obligatorio
Después de cada sugerencia técnica importante, recuérdame registrar en `AI_LOG.md`:
```
## Entrada N — [fecha]
**Prompt:** (lo que yo escribí)
**Respuesta resumida:** (lo que tú sugeriste)
**Decisión tomada:** (lo que yo decidí hacer)
**Reflexión crítica:** (¿fue correcta la sugerencia? ¿la modifiqué? ¿por qué?)
```
Este documento vale 15% de mi calificación. Recuérdamelo si lo estoy omitiendo.

## Cronograma de entregas
| Semana | Fecha       | Entregable                                      |
|--------|-------------|------------------------------------------------|
| 1      | 03/mar/2026 | Documento de definición + dataset elegido       |
| 2      | 10/mar/2026 | Script de preprocesamiento documentado          |
| 3      | 17/mar/2026 | Notebook con modelo CNN baseline                |
| 4      | 24/mar/2026 | Reporte de evaluación formal                    |
| 5      | 07/abr/2026 | Tabla comparativa baseline vs transfer learning |
| 6      | 14/abr/2026 | Reporte de optimización con análisis crítico    |
| 7      | 21/abr/2026 | Documento de análisis de sesgos (2–3 páginas)  |
| 8      | 28/abr/2026 | Carpeta `/inference` funcional                  |
| 9      | 05/may/2026 | Backend FastAPI con `/predict` funcional        |
| 10     | 12/may/2026 | UI funcional conectada al servidor              |
| 11     | 19/may/2026 | README.md, DEPLOYMENT.md y AI_LOG.md completos |
| 12     | 26/may/2026 | Repositorio GitHub + video demo + defensa       |

## Criterios de evaluación (referencia)
| Criterio                        | Peso |
|---------------------------------|------|
| Calidad del modelo              | 25%  |
| Rigor experimental              | 20%  |
| Implementación API + UI         | 20%  |
| Documentación reproducible      | 15%  |
| Uso crítico de IA (AI_LOG.md)   | 15%  |
| Presentación técnica            | 5%   |

## Contexto de la semana actual
<!-- Actualiza esto cada semana para que yo sepa en qué etapa estás -->
**Semana actual:** 1
**Tarea en curso:** Selección y justificación del dataset
**Dataset elegido:** (pendiente de definir)
**Próxima entrega:** 03 de marzo, 2026