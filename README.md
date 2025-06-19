📂 Empfohlene Projektstruktur

📁 kantenerkennung_gpu/
├── edge_gui_tiles_kornia.py        # Teil 1/4 – GUI
├── edge_processing.py              # Teil 2/4 – Klassische Filter & DexiNed-Aufruf
├── tile_utils.py                   # Teil 3/4 – Tile-Logik für DexiNed
├── README.md                       # Teil 4/4 – Anleitung


---

🧾 README.md – (Teil 4/4)

# Kornia Kantenerkennung (GPU-optimiert mit Tile-Modus für DexiNed)

## 🔧 Voraussetzungen

```bash
pip install torch torchvision kornia opencv-python pillow

> ⚠️ Falls du PyTorch ohne CUDA hast, installiere die passende Version hier:
https://pytorch.org/get-started/locally/




---

🚀 Verwendung

python edge_gui_tiles_kornia.py

Wähle einen Ordner mit Bildern (PNG, JPG, JPEG).

Alle Bilder werden verarbeitet mit:

🧠 DexiNed (CNN, via Tile-Modus)

🧮 Sobel, Laplacian, Canny (klassische Filter)


Ausgabe landet im Unterordner: output_edges/ inkl.:

sobel/

laplacian/

canny/

dexined/




---

⚙️ Tile-Modus (für große Bilder)

Tilegröße: 512×512 px

Überlappung: 32 px

✅ Vermeidet GPU-Überlauf & Kanteneffekte

🧠 Speziell getestet für: NVIDIA Quadro T1000 (4 GB VRAM)



---

📦 Modelle

Das DexiNed-Modell wird beim ersten Start automatisch aus Kornia geladen.



---

🖼 Beispiel

Wenn du 3 Bilder im Ordner hast, erscheint danach:

📁 output_edges/
├── sobel/
│   └── bild1.jpg, bild2.jpg, ...
├── laplacian/
├── canny/
├── dexined/


---
