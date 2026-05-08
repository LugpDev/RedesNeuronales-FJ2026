# Clasificador de Imágenes con CNN

Proyecto individual de clasificación de imágenes con Redes Neuronales Convolucionales.
Programa: Servicio Becario | ITC | 4to semestre

## Dataset

<!-- TODO: describir el dataset elegido, número de clases, fuente -->

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
