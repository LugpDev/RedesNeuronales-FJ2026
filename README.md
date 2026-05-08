# Clasificador de Imágenes con CNN

Proyecto individual de clasificación de imágenes con Redes Neuronales Convolucionales.
Programa: Servicio Becario | ITC | 4to semestre

## Dataset

**Chest X-Ray Images (Pneumonia)** — [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)  
Clasificación binaria de radiografías de tórax: `NORMAL` vs `PNEUMONIA`  
~5,856 imágenes | Train: ~5,216 | Val: 16 | Test: 624

### Descarga

1. Ve a https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
2. Haz clic en **Download**
3. Descomprime el archivo en `data_prep/raw/`

La estructura resultante debe ser:

```
data_prep/raw/
├── test/
│   ├── NORMAL/
│   └── PNEUMONIA/
├── train/
│   ├── NORMAL/
│   └── PNEUMONIA/
└── val/
    ├── NORMAL/
    └── PNEUMONIA/
```

## Estructura del proyecto

```
.
├── data_prep/     # Scripts de limpieza, splits y augmentation
├── training/      # Notebooks y scripts de entrenamiento
├── inference/     # Función predict(image) y pipeline de inferencia
├── models/        # Pesos guardados del modelo (.pt)
├── server/        # API FastAPI con endpoint /predict
├── ui/            # Interfaz de usuario
├── requirements.txt
├── README.md
├── DEPLOYMENT.md
└── AI_LOG.md
```

## Instalación

```bash
pip install -r requirements.txt
```

## Entrenamiento

<!-- TODO: instrucciones para ejecutar training/train.py -->

## Servidor

<!-- TODO: instrucciones para lanzar server/main.py con uvicorn -->

## Interfaz

<!-- TODO: instrucciones para abrir ui/index.html -->
