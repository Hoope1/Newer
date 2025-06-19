AGENTS.md

Project Structure

kantenerkennung_gpu/
├── edge_gui_tiles_kornia.py    # GUI interface for selecting folders and showing progress
├── edge_processing.py          # Image processing logic: classic filters + DexiNed
├── tile_utils.py               # Tiling and merging logic for large images
├── README.md                   # Usage instructions and project overview
├── output_edges/               # Generated output (created at runtime)
│   ├── sobel/
│   ├── laplacian/
│   ├── canny/
│   └── dexined/

Modules:

edge_gui_tiles_kornia.py: Launches a Tkinter GUI for folder selection and executes full processing pipeline.

edge_processing.py: Applies classical filters and DexiNed on images.

tile_utils.py: Handles tile-based GPU processing with overlapping windows to support large image sizes on limited VRAM.


Coding Conventions

Python Version: 3.10+

Formatting: black (black .)

Linting: flake8 for PEP8 and import checks

Typing: mypy is used for static type checking

Naming:

Functions: snake_case

Classes: PascalCase

Constants: UPPER_SNAKE_CASE

Modules/files: lower_snake_case.py


Imports: Standard lib -> third-party -> local, separated by blank lines

Logging: Use print() only in GUI or CLI contexts; prefer logging for core logic


Testing Requirements

Testing Framework: pytest

Test Directory: tests/ (not yet present; should be created for expansion)

Test Strategy:

Unit tests for tile handling and edge detection logic in tile_utils.py and edge_processing.py

GUI is manually tested for now; automated GUI tests TBD


Sample Test Command:

pytest tests/


PR Guidelines

Each PR must:

Be named with context (e.g., feat: add laplacian postprocessing)

Include a description with:

Purpose

Affected files

Test coverage notes

Manual verification steps if applicable



All code must:

Pass flake8, mypy, and black formatting

Be accompanied by relevant unit tests if new logic is added



Programmatic Checks

The following checks must pass before merging:

# Formatting
black --check .

# Static type checking
mypy .

# Linting
flake8 .

# Unit tests
pytest tests/

Optional pre-commit hook setup is recommended:

pre-commit install


---

This project is optimized for NVIDIA Quadro T1000 (4GB VRAM) and targets high-fidelity edge detection across large images using a tile-based approach. The integration of classical filters with DexiNed (Kornia) ensures compatibility with both GPU and CPU processing paths.

AI agents are expected to respect VRAM constraints, tile dimensions (512x512 with 32px overlap), and the hybrid classical/ML filter pipeline during code generation.
