# 🧠 Kornia Kantenerkennung mit GPU-Tile-Modus (DexiNed + klassische Filter)

Dieses Projekt bietet eine **leistungsstarke, detailerhaltende Kantenerkennungslösung**, die klassische Algorithmen und ein Deep-Learning-Modell (DexiNed) kombiniert. Es ist optimiert für die GPU **NVIDIA Quadro T1000 (4 GB VRAM)** und ermöglicht die Verarbeitung **großer Bilder durch einen intelligenten Tile-Modus** mit Überlappung.

---

## 🔧 Anforderungen

Installiere alle benötigten Pakete mit:

```bash
pip install torch torchvision kornia opencv-python pillow

> Hinweis: Für CUDA-Unterstützung installiere torch mit GPU-Support:
https://pytorch.org/get-started/locally/




---

📂 Projektstruktur

kantenerkennung_gpu/
├── edge_gui_tiles_kornia.py    # GUI-Anwendung zur Ordnerauswahl und Fortschrittsanzeige
├── edge_processing.py          # Bildverarbeitung: klassische Filter + DexiNed
├── tile_utils.py               # Tile-basierte Verarbeitung und Zusammenbau für DexiNed
├── README.md                   # Diese Anleitung


---

🖥️ Anwendung starten

python edge_gui_tiles_kornia.py

1. Es öffnet sich ein GUI-Fenster.


2. Wähle einen Ordner mit Bildern (JPG, PNG, JPEG).


3. Alle Bilder im Ordner werden automatisch mit 4 Methoden verarbeitet:

Sobel

Laplacian

Canny

DexiNed (deep CNN) – mit GPU-optimiertem Tile-Modus



4. Fortschritt wird live angezeigt.


5. Die Ergebnisse landen im Unterordner output_edges.




---

🧪 Verwendete Filter (Details)

Filter	Typ	Beschreibung

Sobel	Klassisch	Detektiert vertikale und horizontale Kanten (1. Ableitung)
Laplacian	Klassisch	Zweite Ableitung, empfindlich auf kleine Details
Canny	Klassisch	Mehrstufige Methode mit Non-Maximum Suppression & Hysterese
DexiNed	Deep Learning	Dichtes CNN-Modell für feinste Konturen, trainiert auf mehreren Datensätzen



---

📦 DexiNed Modell

Wird automatisch bei erster Nutzung über Kornia heruntergeladen.

Architektur: DexiNed (Dense Extreme Inception Network)

Verwendung: from kornia.models import DexiNedBuilder



---

🧩 Tile-Modus für DexiNed (ohne Detailverlust)

Große Bilder werden in Kacheln zerlegt und nahtlos rekonstruiert:

Eigenschaft	Wert

Tile-Größe	512 × 512 Pixel
Überlappung	32 Pixel pro Seite
Verarbeitung	Einzelkachelweise auf GPU
Rekonstruktion	Überblendung mit Fensterfunktion zur Nahtvermeidung
Vorteil	Kein Speicherüberlauf, keine Kantenverluste bei DexiNed



---

📁 Ausgabeordnerstruktur

Nach Verarbeitung entsteht:

output_edges/
├── sobel/
│   ├── bild1.jpg
│   └── ...
├── laplacian/
├── canny/
├── dexined/

Alle Bilder behalten ihre Dateinamen bei.


---

🎯 Zielgruppe

Forschung & Technik

Künstlerische Kantenskizzen

Maschinenlernen / Vorverarbeitung

Large-Image-Processing auf GPUs mit begrenztem Speicher



---

⚠️ Hinweise

Eingabebilder sollten möglichst quadratisch oder groß genug für Tiles sein.

DexiNed erfordert CUDA-fähige GPUs – bei CPU-only läuft es sehr langsam.

Klassische Filter laufen auch ohne GPU.



---
