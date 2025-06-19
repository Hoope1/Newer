# edge_processing.py – Teil 2/4
import torch
import torchvision.transforms as T
import kornia as K
import cv2
import numpy as np
from pathlib import Path
from PIL import Image
from tile_utils import process_with_dexined_tiles

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def invert_image(tensor_img):
    img_np = tensor_img.squeeze().detach().cpu().numpy()
    img_inv = 1.0 - img_np
    return (img_inv * 255).astype(np.uint8)

def process_classic_filters(img_tensor, output_base, img_name):
    methods = {
        'sobel': K.filters.sobel(img_tensor),
        'laplacian': K.filters.laplacian(img_tensor, kernel_size=5),
        'canny': K.filters.canny(img_tensor)[0],
    }

    for name, edge_tensor in methods.items():
        edge_img = invert_image(edge_tensor)
        out_dir = output_base / name
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / img_name
        cv2.imwrite(str(out_path), edge_img)

def process_image(img_path, model_dexined, output_dir):
    img = Image.open(img_path).convert("RGB")
    img_tensor = T.ToTensor()(img).unsqueeze(0).to(device)

    # Klassische Filter
    process_classic_filters(img_tensor, output_dir, Path(img_path).name)

    # DexiNed mit Tile-Modus
    dexined_out = process_with_dexined_tiles(img_tensor, model_dexined)
    dex_img = invert_image(dexined_out)
    out_path = output_dir / "dexined" / Path(img_path).name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(out_path), dex_img)

def load_dexined_model():
    from kornia.models import DexiNedBuilder
    return DexiNedBuilder.build(pretrained=True).to(device).eval()

def process_folder(folder_path, progress_callback):
    images = list(Path(folder_path).rglob("*.png")) + \
             list(Path(folder_path).rglob("*.jpg")) + \
             list(Path(folder_path).rglob("*.jpeg"))

    total = len(images)
    if total == 0:
        raise ValueError("Keine Bilder im Ordner!")

    model = load_dexined_model()
    output_dir = Path(folder_path) / "output_edges"

    for i, img_path in enumerate(images):
        process_image(img_path, model, output_dir)
        progress_callback(i + 1, total)
