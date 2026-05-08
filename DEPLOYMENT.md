# Guía de Despliegue

## Requisitos del sistema

<!-- TODO: Python 3.x, versión CUDA si aplica, RAM mínima -->

## Instalación

```bash
git clone <repo-url>
cd RedesNeuronales-FJ2026
pip install -r requirements.txt
```

## Modelo

<!-- TODO: dónde obtener o cómo generar los pesos models/best_model.pt -->

## Lanzar el servidor

```bash
uvicorn server.main:app --host 0.0.0.0 --port 8000
```

## Acceder a la interfaz

<!-- TODO: abrir ui/index.html en el navegador o instrucciones de servidor estático -->

## Variables de entorno

<!-- TODO: listar variables si aplica (MODEL_PATH, etc.) -->

## Troubleshooting

<!-- TODO: errores comunes y soluciones -->
