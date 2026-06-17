# CNN Baseline — Propuestas de Arquitectura

**Contexto:** Clasificación binaria de neumonía (Normal vs Pneumonia) sobre el dataset Chest X-Ray de Kaggle.
**Semana:** 3 | **Entregable:** Notebook con modelo CNN baseline

---

## Arquitectura A — CNN Pequeña (3 bloques Conv)

```
Input (224×224×3)
  → Conv2d(3→32, 3×3) + ReLU + MaxPool(2×2)
  → Conv2d(32→64, 3×3) + ReLU + MaxPool(2×2)
  → Conv2d(64→128, 3×3) + ReLU + MaxPool(2×2)
  → Flatten
  → Linear(128×28×28 → 256) + ReLU + Dropout(0.5)
  → Linear(256 → 2)
```

**Propósito:** Verificar que el pipeline completo funciona antes de añadir complejidad.

| Aspecto | Estimado |
|---|---|
| Parámetros | ~6–8 M |
| Accuracy esperado | 78–84% (val) |
| Tiempo / época (CPU) | ~8–12 min |
| Tiempo / época (GPU) | ~45–90 seg |
| Riesgo principal | Underfitting si el dataset tiene mucha varianza |

---

## Arquitectura B — CNN Moderada estilo VGG (bloques dobles)

```
Input (224×224×3)
  → [Conv2d(3→32) + Conv2d(32→32)] + ReLU + MaxPool + BatchNorm
  → [Conv2d(32→64) + Conv2d(64→64)] + ReLU + MaxPool + BatchNorm
  → [Conv2d(64→128) + Conv2d(128→128)] + ReLU + MaxPool + BatchNorm
  → GlobalAveragePooling2d
  → Linear(128 → 256) + ReLU + Dropout(0.4)
  → Linear(256 → 2)
```

**Propósito:** Baseline real para reportar métricas formales en la entrega de Semana 3.

| Aspecto | Estimado |
|---|---|
| Parámetros | ~1.5–2 M (gracias al GAP) |
| Accuracy esperado | 85–90% (val) |
| Tiempo / época (CPU) | ~12–18 min |
| Tiempo / época (GPU) | ~60–120 seg |
| Riesgo principal | Overfitting posible con >20 épocas sin regularización |

---

## Comparativa

| | Arq. A | Arq. B |
|---|---|---|
| Capas conv | 3 (simples) | 6 (pareadas) |
| Regularización | Solo Dropout | BatchNorm + Dropout |
| Capacidad representacional | Baja-media | Media-alta |
| Parámetros | ~6–8 M | ~1.5–2 M |
| Tiempo de debug | Rápido | Moderado |
| Uso recomendado | Verificar pipeline | Entregable formal |

---

## Señales esperadas durante entrenamiento

- `train_loss` debe bajar consistentemente en las primeras 5–10 épocas.
- `val_accuracy` debe subir y estabilizarse — si sigue subiendo siempre, puede haber data leakage.
- Si `train_acc − val_acc > 10 puntos`, hay overfitting: subir Dropout o añadir augmentation.

---

## Estrategia de implementación sugerida

1. Implementar **Arquitectura A** y correr 1–2 épocas para validar el pipeline.
2. Una vez confirmado el flujo, cambiar a **Arquitectura B** para el entrenamiento formal.
3. Reportar métricas obligatorias: Accuracy, Precision, Recall, F1, Matriz de confusión, curvas de loss/accuracy.
