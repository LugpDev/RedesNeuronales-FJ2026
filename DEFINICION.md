# Documento de Definición del Proyecto

**Clasificación de Radiografías de Tórax con CNN**

**Estudiante:** Luis Cervantes  
**Programa:** Servicio Becario
**Responsable académico:** Atoany Fierro  
**Fecha:** 03 de marzo de 2026  

---

## 1. Descripción del problema

La neumonía es una infección pulmonar que afecta a millones de personas cada año y cuyo
diagnóstico temprano es crítico para reducir la mortalidad. Una herramienta de apoyo
automatizado que analice radiografías de tórax puede asistir a profesionales de salud,
especialmente en contextos con recursos diagnósticos limitados.

Personalmente, me interesa aplicar la tecnología en un campo tan importante como la salud, y este proyecto representa una implementación concreta de esa motivación.

Este proyecto aborda la clasificación binaria de radiografías de tórax en dos categorías:

- **NORMAL** — paciente sin neumonía
- **PNEUMONIA** — paciente con neumonía bacteriana o viral

---

## 2. Dataset seleccionado

**Nombre:** Chest X-Ray Images (Pneumonia)  
**Fuente:** Kaggle — Paul Mooney  
**URL:** <https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia>  
**Licencia:** CC BY 4.0  

### Estadísticas

| Subconjunto | NORMAL | PNEUMONIA | Total |
|-------------|--------|-----------|-------|
| Train       | 1,341  | 3,875     | 5,216 |
| Val         | 8      | 8         | 16    |
| Test        | 234    | 390       | 624   |
| **Total**   | 1,583  | 4,273     | 5,856 |

Las imágenes son radiografías en escala de grises en formato JPEG, con resoluciones variables.

El dataset presenta un desbalance de clases notable: aproximadamente 73% PNEUMONIA vs 27% NORMAL en el conjunto de entrenamiento. Esto deberá considerarse durante el entrenamiento mediante técnicas como pesos de clase o augmentation diferencial.
Adicionalmente, el conjunto de validación es inusualmente pequeño (16 imágenes), por lo que se evaluará si conviene redistribuir los datos para obtener una validación más representativa.

---

## 3. Justificación técnica del dataset

El dataset es adecuado para un proyecto de esta magnitud: el tamaño es manejable, cuenta con múltiples variables de referencia y la detección precisa de este tipo de enfermedad sigue siendo altamente relevante hoy en día.

**Ventajas identificadas:**

- Dataset ampliamente usado en literatura académica, lo que permite comparar resultados
- Imágenes etiquetadas por médicos especialistas (alta confiabilidad del ground truth)
- Tamaño manejable para entrenamiento en hardware local
- Formato estándar compatible con las bibliotecas del stack tecnológico elegido

**Limitaciones conocidas:**

- Desbalance de clases que puede sesgar el modelo hacia PNEUMONIA
- Conjunto de validación muy pequeño (16 imágenes) — requiere estrategia de validación alternativa
- No distingue entre neumonía bacteriana y viral en la etiqueta principal
- Las imágenes provienen de un solo centro médico (Hospital Guangzhou), lo que limita
  la generalización geográfica
