# 🧠 PLAN DE SERVICIO BECARIO (MODALIDAD INDIVIDUAL)
## Desarrollo de Sistema de Clasificación de Imágenes con CNN
### Con Servidor Local, Interfaz y Uso Obligatorio de IA como Asistente

---

# 📌 Información General

**Programa:** Servicio Becario  
**Carrera:** ITC (4to semestre)  
**Duración:** 12 semanas  
**Modalidad:** Proyecto individual  
**Número de estudiantes:** 5  

---

# 🎯 Objetivo General

Cada estudiante desarrollará de manera individual un sistema completo de clasificación de imágenes utilizando Redes Neuronales Convolucionales (CNN), integrando:

- Selección de base de datos
- Entrenamiento y optimización del modelo
- Evaluación formal
- Implementación de servidor local
- Desarrollo de interfaz de usuario
- Documento reproducible de despliegue
- Uso obligatorio de herramientas de IA generativa como asistente técnico

---

# 🤖 Uso Obligatorio de IA Generativa

Durante todo el proyecto, cada estudiante deberá utilizar herramientas de IA generativa (ej. ChatGPT, Copilot, Gemini u otra equivalente) como asistente de apoyo técnico.

### Reglas:

1. La IA puede:
   - Sugerir arquitecturas
   - Ayudar a depurar código
   - Proponer mejoras
   - Explicar conceptos
   - Generar ejemplos de implementación

2. La IA NO sustituye:
   - El análisis crítico del estudiante
   - La interpretación de métricas
   - La justificación de decisiones

3. Todo uso de IA debe ser documentado.

---

# 📓 Bitácora Obligatoria de Uso de IA

Cada estudiante deberá mantener un archivo:
```cpp
AI_LOG.md
```


Este documento debe incluir:

- Fecha
- Prompt utilizado
- Respuesta resumida
- Decisión tomada
- Reflexión crítica (¿fue correcta la sugerencia?, ¿se modificó?, ¿por qué?)

Este documento será evaluado.

---

# 🧠 Elección de Base de Datos (Obligatorio)

Cada estudiante deberá seleccionar una base de datos pública de imágenes para clasificación.

Ejemplos permitidos:

- ISIC (lesiones cutáneas)
- PlantVillage
- CIFAR-10 / CIFAR-100
- Pneumonia X-ray
- Mask detection
- Traffic signs
- Garbage classification
- Dataset propio (previa aprobación)

**Requisitos mínimos:**
- Al menos 2 clases
- 1,000 imágenes totales (o justificar menor tamaño)
- Uso académico permitido

**Entregable Semana 1:** Documento justificando elección del dataset.

---

# 📅 Cronograma de Trabajo (12 Semanas)

---

## 🔹 Semana 1 – Definición del Problema
- Selección del dataset.
- Justificación técnica.
- Uso de IA para:
  - Analizar posibles enfoques.
  - Sugerir arquitectura inicial.
- Inicio de AI_LOG.md.

**Entregable:** Documento de definición + registro de IA.

**Feche de Entrega:** 03 de marzo, 2026

---

## 🔹 Semana 2 – Preprocesamiento
- Limpieza de datos.
- División train/val/test.
- Data augmentation.
- Consultar IA sobre estrategias de balanceo.

**Entregable:** Script documentado + reflexión sobre sugerencias de IA.

**Feche de Entrega:** 10 de marzo, 2026

---

## 🔹 Semana 3 – Modelo Baseline
- Implementación CNN desde cero.
- Entrenamiento inicial.
- Uso de IA para revisar arquitectura.

**Entregable:** Notebook + análisis crítico de sugerencias de IA.

**Feche de Entrega:** 17 de marzo, 2026

---

## 🔹 Semana 4 – Evaluación Formal
- Matriz de confusión.
- Precision, Recall, F1.
- Análisis de errores.
- Consultar IA para interpretar métricas y contrastar conclusiones.

**Entregable:** Reporte técnico con reflexión crítica.

**Feche de Entrega:** 24 de marzo, 2026

---

## 🔹 Semana 5 – Transfer Learning
- Implementación modelo preentrenado.
- Comparación contra baseline.
- Solicitar a IA posibles mejoras.

**Entregable:** Tabla comparativa + decisión justificada.

**Feche de Entrega:** 07 de abril, 2026

---

## 🔹 Semana 6 – Optimización
- Ajuste de hiperparámetros.
- Regularización.
- Uso de IA para sugerir mejoras.
- Validar experimentalmente cada sugerencia.

**Entregable:** Reporte antes/después + análisis crítico.

**Feche de Entrega:** 14 de abril, 2026

---

## 🔹 Semana 7 – Análisis Crítico
- Estudio de falsos positivos y negativos.
- Identificación de sesgos.
- Discusión con apoyo de IA.
- Reflexión sobre limitaciones.

**Entregable:** Documento de análisis (2–3 páginas).

**Feche de Entrega:** 21 de abril, 2026

---

## 🔹 Semana 8 – Pipeline de Inferencia
- Guardado del modelo.
- Función `predict(image)`.
- Validación.

**Entregable:** Carpeta `/inference`.

**Feche de Entrega:** 28 de abril, 2026

---

## 🔹 Semana 9 – Servidor Local
- Implementación API (FastAPI).
- Endpoint `/predict`.
- Manejo de errores.
- Uso de IA para estructurar API.

**Entregable:** Backend funcional.

**Feche de Entrega:** 05 de mayo, 2026

---

## 🔹 Semana 10 – Interfaz
- Desarrollo UI.
- Conexión con servidor.
- Validación.
- Mejora UX con apoyo de IA.

**Entregable:** UI funcional.

**Feche de Entrega:** 12 de mayo, 2026

---

## 🔹 Semana 11 – Documentación Reproducible
- Organización final del repositorio.
- Creación de:
  - `README.md`
  - `DEPLOYMENT.md`
  - `AI_LOG.md`

**Entregable principal:** Documento reproducible de despliegue.

**Feche de Entrega:** 19 de mayo, 2026

---

## 🔹 Semana 12 – Presentación Final
- Instalación en máquina distinta.
- Defensa técnica individual.
- Explicación de:
  - Decisiones técnicas
  - Uso de IA
  - Limitaciones
  - Aprendizajes

**Entregables finales:**
- Repositorio completo (GitHub).
- Modelo entrenado.
- Servidor funcional.
- Interfaz funcional.
- Documentación reproducible.
- Bitácora de uso de IA.
- Video demo.


**Feche de Entrega:** 26 de mayo, 2026

---

# 📊 Métricas Obligatorias

- Accuracy
- Precision
- Recall
- F1-score
- Matriz de confusión
- ROC-AUC (si aplica)

---

# 📁 Estructura Esperada
project/ <br>
│<br>
├── data_prep/<br>
├── training/<br>
├── inference/<br>
├── models/<br>
├── server/<br>
├── ui/<br>
├── requirements.txt<br>
├── README.md<br>
├── DEPLOYMENT.md<br>
├── AI_LOG.md<br>
└── PLAN_SERVICIO_BECARIO.md<br>


---

# 🧾 Criterios de Evaluación

| Criterio | Peso |
|----------|------|
| Calidad del modelo | 25% |
| Rigor experimental | 20% |
| Implementación técnica (API + UI) | 20% |
| Documentación reproducible | 15% |
| Uso crítico de IA (AI_LOG.md) | 15% |
| Presentación técnica | 5% |

---

# 🔎 Enfoque Formativo

Este proyecto no solo evalúa la capacidad de programar modelos, sino:

- Pensamiento crítico frente a sugerencias de IA
- Capacidad de validar experimentalmente
- Razonamiento técnico
- Documentación profesional
- Desarrollo end-to-end

---

# 🏁 Resultado Esperado

Al finalizar, cada estudiante habrá desarrollado:

- Un sistema completo de clasificación de imágenes.
- Experiencia real en despliegue local.
- Capacidad de usar IA como asistente técnico de manera crítica.
- Habilidades de documentación reproducible profesional.

---

**Responsable del Proyecto:**  
Atoany Fierro

Servicio Becario – Área de Inteligencia Artificial
