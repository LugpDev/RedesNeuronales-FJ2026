import json
import random
from pathlib import Path
from PIL import Image

SEED = 42
VAL_FRACTION = 0.10
RAW_DIR = Path("data_prep/raw")
OUTPUT_PATH = Path("data_prep/splits.json")
LABEL_MAP = {"NORMAL": 0, "PNEUMONIA": 1}


def collect_paths(split: str) -> dict[str, list[Path]]:
    # Devuelve {"NORMAL": [...], "PNEUMONIA": [...]} para un split dado.
    result = {}
    for class_name in LABEL_MAP:
        folder = RAW_DIR / split / class_name
        paths = (
            sorted(folder.glob("*.jpeg"))
            + sorted(folder.glob("*.jpg"))
            + sorted(folder.glob("*.png"))
        )
        result[class_name] = paths
    return result


def check_corruption(paths: list[Path]) -> list[str]:
    # Intenta abrir cada imagen y retorna las rutas que fallan.
    corrupt = []
    for p in paths:
        try:
            with Image.open(p) as img:
                img.verify()
        except Exception:
            corrupt.append(str(p))
    return corrupt


def build_entries(paths: list[Path], label: int) -> list[dict]:
    return [{"path": str(p), "label": label} for p in paths]


def main():
    random.seed(SEED)

    # --- 1. Cargar imágenes de train originales ---
    train_raw = collect_paths("train")
    test_raw = collect_paths("test")
    val_raw = collect_paths("val")

    raw_data = [
        ("train", train_raw),
        ("test", test_raw),
        ("val", val_raw),
    ]

    print("=== Estadísticas del dataset original ===")
    for split_name, data in raw_data:
        for cls, paths in data.items():
            print(f"  {split_name}/{cls}: {len(paths)} imágenes")

    # --- 2. Redistribuir val desde train (~10% por clase) ---
    new_train = {}
    new_val = {}

    for class_name, paths in train_raw.items():
        shuffled = paths.copy()
        random.shuffle(shuffled)
        n_val = max(
            1, int(len(paths) * VAL_FRACTION) - len(val_raw[class_name])
        )  # 10% de la muestra
        new_val[class_name] = val_raw[class_name] + shuffled[:n_val]
        new_train[class_name] = shuffled[n_val:]

    print("\n=== Splits corregidos ===")
    for cls in LABEL_MAP:
        print(f"  train/{cls}: {len(new_train[cls])} | val/{cls}: {len(new_val[cls])}")
    for cls in LABEL_MAP:
        print(f"  test/{cls}: {len(test_raw[cls])}")

    # --- 3. Verificar imágenes corruptas ---
    print("\n=== Verificando integridad de imágenes ===")
    all_paths = (
        [p for paths in new_train.values() for p in paths]
        + [p for paths in new_val.values() for p in paths]
        + [p for paths in test_raw.values() for p in paths]
    )
    corrupt = check_corruption(all_paths)
    if corrupt:
        print(f"  ADVERTENCIA: {len(corrupt)} imágenes corruptas:")
        for c in corrupt:
            print(f"    {c}")
    else:
        print(f"  OK — ninguna imagen corrupta en {len(all_paths)} archivos")

    # --- 4. Construir y guardar splits.json ---
    splits = {
        "train": [],
        "val": [],
        "test": [],
        "stats": {},
    }

    for class_name, label in LABEL_MAP.items():
        splits["train"].extend(build_entries(new_train[class_name], label))
        splits["val"].extend(build_entries(new_val[class_name], label))
        splits["test"].extend(build_entries(test_raw[class_name], label))

    splits["stats"] = {
        "train": {cls: len(new_train[cls]) for cls in LABEL_MAP},
        "val": {cls: len(new_val[cls]) for cls in LABEL_MAP},
        "test": {cls: len(test_raw[cls]) for cls in LABEL_MAP},
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(splits, f, indent=2)

    print(f"\n=== splits.json guardado en {OUTPUT_PATH} ===")
    print(f"  train: {len(splits['train'])} entradas")
    print(f"  val:   {len(splits['val'])} entradas")
    print(f"  test:  {len(splits['test'])} entradas")


if __name__ == "__main__":
    main()
