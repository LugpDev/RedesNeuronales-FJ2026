# Estrategias de Balanceo de Clases

## Contexto del dataset

**Chest X-Ray Images (Pneumonia)** presenta un desbalance de clases notable:

| Clase | Imágenes (train) | Proporción |
|---|---|---|
| PNEUMONIA | ~3,875 | 73% |
| NORMAL | ~1,341 | 27% |

Un modelo entrenado sin corrección tenderá a predecir PNEUMONIA por defecto, lo que infla el accuracy pero degrada el Recall de NORMAL y puede enmascarar errores clínicamente relevantes.

---

## Estrategias disponibles

### 1. Pesos de clase en la función de pérdida (`class_weight`)

Penaliza más los errores cometidos en la clase minoritaria (NORMAL) durante el cálculo del gradiente.

```python
# PyTorch — para clasificación binaria
pos_weight = torch.tensor([73 / 27])  # ≈ 2.7
criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
```

**Ventaja:** Cero modificación sobre los datos; impacto inmediato y predecible.  
**Limitación:** No cambia la distribución real de los batches.

---

### 2. Oversampling con `WeightedRandomSampler`

El DataLoader muestrea imágenes de NORMAL con mayor frecuencia para que cada batch sea aproximadamente balanceado.

```python
# Asignar peso inverso a la frecuencia de cada clase
weights = [1 / count_per_class[label] for label in all_labels]
sampler = WeightedRandomSampler(weights, num_samples=len(weights), replacement=True)

loader = DataLoader(dataset, batch_size=32, sampler=sampler)
```

**Ventaja:** Los batches llegan balanceados al modelo sin descartar datos.  
**Limitación:** Las imágenes de NORMAL se repiten más, lo que puede inducir overfitting si no se acompaña de augmentation.

---

### 3. Data augmentation diferencial

Aplicar transformaciones más agresivas exclusivamente a la clase minoritaria para generar variantes sintéticas adicionales.

```python
augment_normal = transforms.Compose([
    transforms.RandomRotation(20),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
])

augment_pneumonia = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
])
```

**Ventaja:** Aumenta la diversidad real de NORMAL, reduciendo overfitting del oversampling.  
**Limitación:** Requiere un Dataset personalizado que aplique la transformación correcta según la etiqueta.

---

### 4. Ajuste del umbral de decisión (post-entrenamiento)

En lugar del umbral por defecto (0.5), se busca el valor óptimo sobre la curva ROC que minimice falsos negativos (PNEUMONIA no detectada).

```python
from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_true, y_scores)

# Maximizar TPR - FPR (índice de Youden) o maximizar F1
optimal_idx = (tpr - fpr).argmax()
optimal_threshold = thresholds[optimal_idx]
```

**Ventaja:** No requiere reentrenar; ajusta el balance precision-recall según el costo clínico asumido.  
**Cuándo usarla:** Siempre en problemas médicos donde un tipo de error es más costoso que otro.

---

### 5. Undersampling de la clase mayoritaria

Eliminar imágenes de PNEUMONIA aleatoriamente hasta igualar el número de NORMAL.

**Ventaja:** Balanceo inmediato y sencillo.  
**Por qué NO aplicarla aquí:** Con ~1,341 imágenes de NORMAL, descartar ~2,500 de PNEUMONIA supone una pérdida de información significativa en un dataset ya de tamaño moderado.

---

## Comparativa y recomendación

| Estrategia | Prioridad | Justificación |
|---|---|---|
| `class_weight` | **Alta** | Primer ajuste; sin costo de implementación |
| `WeightedRandomSampler` | **Alta** | Batches balanceados sin descartar datos |
| Augmentation diferencial | **Media** | Reduce overfitting del oversampling |
| Ajuste de umbral | **Alta** | Crítico en diagnóstico médico |
| Undersampling | **No aplicar** | Pérdida de datos injustificada |

### Combinación recomendada

```
class_weight  +  WeightedRandomSampler  →  Entrenamiento
                                        ↓
                              Ajuste de umbral óptimo  →  Evaluación final
```

Esta combinación ataca el desbalance tanto a nivel de gradiente como a nivel de distribución de batches, y culmina con un umbral de decisión alineado al contexto clínico del problema.

---

## Métricas a observar con desbalance

Con clases desbalanceadas, el **accuracy no es suficiente**. Las métricas prioritarias son:

- **Recall de PNEUMONIA** — mide cuántas neumonías reales se detectan (falsos negativos = riesgo clínico)
- **Precision de NORMAL** — mide cuántos casos normales se clasifican correctamente
- **F1-score por clase** — balance entre precision y recall
- **AUC-ROC** — rendimiento global independiente del umbral
- **Matriz de confusión** — distribución completa de errores por clase
