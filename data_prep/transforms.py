from torchvision import transforms

# Media y desviación estándar de ImageNet (RGB).
# Se usan como aproximación estándar incluso para imágenes médicas en escala de grises
# convertidas a RGB, ya que aceleran la convergencia del entrenamiento.
_MEAN = [0.485, 0.456, 0.406]
_STD = [0.229, 0.224, 0.225]

# Solo para train: augmentation ligero para reducir overfitting.
# Flip horizontal es válido en radiografías de tórax (no cambia el diagnóstico).
# Rotación ±10° simula variación en el posicionamiento del paciente.
train_transforms = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(degrees=10),
        transforms.ToTensor(),
        transforms.Normalize(mean=_MEAN, std=_STD),
    ]
)

# Val y test: sin augmentation para que la métrica refleje rendimiento real.
eval_transforms = transforms.Compose(
    [
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=_MEAN, std=_STD),
    ]
)
